import pygame
import random
from classes import Flower, Background, Frame
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT, BACKGROUND_COLOR

pygame.init()

# set frame
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Flower")
clock = pygame.time.Clock()

def main():
    screen_frame = Frame(height = DISPLAY_HEIGHT, width = DISPLAY_WIDTH, background = None, sprite_type = "background")
    screen_frame.set_align(align = "bottom", align_x = DISPLAY_WIDTH/2, align_y = DISPLAY_HEIGHT * 6/7)
    background = Background("img/table.png", screen_frame, size_in_frame = 0.325, num_frames = 2)
    background_frame = Frame(height = 110, width = 56, background = None, sprite_type = "flower")
    background_frame.set_align(align = "bottom", align_x = 200, align_y = 180)
    flower = Flower("img/flower_1.png", background_frame, size_in_frame = 1.15, attach_x = 2 * 16/25)
    x = 0
    y = 0
    x_change = 0
    y_change = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print(x)
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print(y)

        x = x + x_change
        y = y + y_change

        gameDisplay.fill(BACKGROUND_COLOR)
        gameDisplay.blit(background.img, background.get_display_coordinates())
        gameDisplay.blit(flower.img, flower.get_display_coordinates())
        # gameDisplay.blit(flower.img, (x, y))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()