from circleshape import *
from constants import *
from player import *
import pygame


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color = "black"
    game_clock = pygame.time.Clock()
    dt = 0
    sprites = pygame.sprite.Group()
    player_sprite = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(background_color)
        player_sprite.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
