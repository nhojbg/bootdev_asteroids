import pygame, math
from constants import (PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED,
                       PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS)
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 135
        self.shoot_cooldown = 0
    
    # shape draw geometry (handed down code)
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        self.screen = pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
                        #pygame.draw.polygon(surface, color, points, width)
    
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1) # Vectors uin python3 read L>R, top\/bottom, so this is a downwards vector.
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt) # negative dt value to reverse direction of rotation
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
            
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.shoot_cooldown -= dt

    def shoot(self) -> None:
        if self.shoot_cooldown <= 0:
            shot = Shot(x = self.position[0], y = self.position[1])
            shot_velocity = pygame.Vector2(0,1)
            rotated_shot_velocity = shot_velocity.rotate(self.rotation)
            rotated_shot_velocity_with_speed = rotated_shot_velocity * PLAYER_SHOOT_SPEED
            shot.velocity = rotated_shot_velocity_with_speed
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        
