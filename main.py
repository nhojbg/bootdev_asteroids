import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
#from circleshape import collides_with

def main():
    print(f"Hello from asteroids!\nStarting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    # Screen initialisation
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Clock and framerate
    game_clock = pygame.time.Clock()
    dt = 0.0
    
    #Containers setup
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Assign class containers (inherited from CircleShape as tuple of pygame.sprite.Group)
    Player.containers = (updatable, drawable)
    # To handle multiple insances of Asteroid(?)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    # To handle multiple instances of shots
    Shot.containers = (shots, updatable, drawable)
    
    # Player initialisation
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        #print(dt)


if __name__ == "__main__":
    main()
