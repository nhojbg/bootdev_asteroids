import pygame, math, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        self.screen = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
  
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            vector_mod = random.uniform(20, 50)
            new_velocities = self.velocity.rotate(vector_mod), self.velocity.rotate(-vector_mod)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for velocity in new_velocities:
                asteroid_fragment = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid_fragment.velocity = velocity * 1.2
#            new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
#            new_asteroid_2.velocity = new_velocity_2 * 1.2
            