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
    background_frame = Frame(height = 110, width = 56, background = background, sprite_type = "flower")
    background_frame.set_align(align = "bottom", align_x = 200, align_y = 180)
    # watering_can_frame = Frame(height = 80, width = 100, background = background, sprite_type = "watering can")
    # watering_can_frame.set_align()
    flower = Flower("img/flower_1.png", background_frame, size_in_frame = 1.15, attach_x = 2 * 16/25)
    flower.set_water_zone(y_upper = 473 - 155, y_lower = 473 - 115, x_left = 145, x_right = 265)
    test = pygame.image.load("img/test.png")

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
                    print((x, y))
                    print(flower.in_water_zone(x, y))
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print((x, y))
                    print(flower.in_water_zone(x, y))

        x = x + x_change
        y = y + y_change

        gameDisplay.fill(BACKGROUND_COLOR)
        gameDisplay.blit(background.img, background.get_initial_display_coordinates())
        gameDisplay.blit(flower.img, flower.get_initial_display_coordinates())
        gameDisplay.blit(test, (x, y))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()