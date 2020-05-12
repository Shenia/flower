import pygame
import random

# Constants
FLOWERS = {
    "Orchid": {
        "name": "Orchid",
        "x": 75,
        "y": 40,
        "img": "img/flower_1.png",
        "water_range_x_lower": 175,
        "water_range_x_upper": 200,
        "water_range_y_lower": 10,
        "water_range_y_upper": 30,
        "is_tree": False,
        "size": 55
    },
    "Calla Lily": {
        "name": "Calla Lily",
        "x": 85,
        "y": 40,
        "img": "img/flower_2.png",
        "water_range_x_lower": 175,
        "water_range_x_upper": 200,
        "water_range_y_lower": 10,
        "water_range_y_upper": 30,
        "is_tree": False,
        "size": 55
    },
    "Gardenia": {
        "name": "Gardenia",
        "x": 80,
        "y": 45,
        "img": "img/flower_3.png",
        "water_range_x_lower": 175,
        "water_range_x_upper": 200,
        "water_range_y_lower": 10,
        "water_range_y_upper": 30,
        "is_tree": False,
        "size": 55
    },
    "Ficus": {
        "name": "Ficus",
        "x": 30,
        "y": 50,
        "img": "img/flower_16.png",
        "water_range_x_lower": 155,
        "water_range_x_upper": 195,
        "water_range_y_lower": 65,
        "water_range_y_upper": 85,
        "is_tree": True,
        "size": 75
    }
}
FLOWER_LIST = list(FLOWERS.keys())
BACKGROUND_COLOR = (204, 255, 102)

DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 300

# Helpers
def display_image(image, x, y):
    gameDisplay.blit(image, (x,y))

def get_flower(n = -1):
    if n == -1:
        n = random.randint(0, 3)
    flower = FLOWER_LIST[n]
    return FLOWERS[flower]

# Global Variables
flower_position_x = 0
flower_position_y = 0
table_position_x = 0
table_position_y = 0

x = 225
y = 195
x_change = 0
y_change = 0

pygame.init()

# Set up window 
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Flower")

# Set table
table_img = pygame.image.load('img/table.png')
table_img = pygame.transform.scale(table_img, (int(DISPLAY_WIDTH*66/100), int(DISPLAY_HEIGHT*60/100)))
table_position_x = DISPLAY_WIDTH/6
table_position_y = DISPLAY_HEIGHT*2/5

# Get flower
flower = get_flower(0)

# Set watering can
watering_can_img = pygame.image.load('img/watering_can_pink.png')
watering_can_img = pygame.transform.scale(watering_can_img, (int(DISPLAY_WIDTH*30/100), int(DISPLAY_HEIGHT*30/100)))

# Set watering image
watering_img = pygame.image.load('img/watering_pink.png')
watering_img = pygame.transform.scale(watering_img, (int(DISPLAY_WIDTH*30/100), int(DISPLAY_HEIGHT*60/100)))

clock = pygame.time.Clock()
crashed = False
water = False
water_count = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
            elif event.key == pygame.K_RETURN:
                water = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                print(x)
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
                print(y)
            elif event.key == pygame.K_RETURN:
                water = False
                print(water_count)
                water_count = 0

    gameDisplay.fill(BACKGROUND_COLOR)

    if not flower["is_tree"]:
        display_image(image = table_img, x = table_position_x, y = table_position_y)
    
    display_image(image = pygame.transform.scale(pygame.image.load(flower["img"]), (int(DISPLAY_WIDTH*flower["size"]/100), int(DISPLAY_HEIGHT*flower["size"]/100))), x = flower["x"], y = flower["y"])

    if water_count >= 250:
        print("start")
        # Get new flower
        flower = get_flower()
        # Reset water count
        water_count = 0
        # Sequence
        clock.tick(1000000)
        print("end")
    
    x += x_change
    y += y_change

    if water:
        display_image(image = watering_img, x = x, y = y)
        if (x >= flower["water_range_x_lower"] and x <= flower["water_range_x_upper"] and y >= flower["water_range_y_lower"] and y <= flower["water_range_y_upper"]):
            water_count += 1
    else:
        display_image(image = watering_can_img, x = x, y = y)

    pygame.display.update()
    clock.tick(100)

pygame.quit()
quit()