import pygame
import random
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT

# all resizing looks at display_height
class Sprite:
    def __init__(self, img, frame, size_in_frame, attach_x, attach_y, movable):
        self.frame = frame
        self.size_in_frame = size_in_frame
        self.img = pygame.image.load(img)
        self.scale = self.frame.height / self.img.get_height() * size_in_frame
        self.display_height = int(self.img.get_height() * self.scale)
        self.display_width = int(self.img.get_width() * self.scale)
        self.img = pygame.transform.scale(self.img, (self.display_width, self.display_height))
        self.frame.sprite = self
        self.attach_x = attach_x
        self.attach_y = attach_y
        self.movable = movable
        self.x = self.get_initial_display_coordinates()[0]
        self.y = self.get_initial_display_coordinates()[1]
    
    def get_initial_display_coordinates(self):
        frame_align = self.frame.align
        if frame_align == "bottom":
            self.display_x = self.frame.align_x - (self.display_width/2 * self.attach_x)
            self.display_y = self.frame.align_y - (self.display_height * self.attach_y)
        return (self.display_x, self.display_y)

# Contained by a Background
class Flower(Sprite):   
    water = 0

    def __init__(self, img, frame, size_in_frame, attach_x = 1, attach_y = 1):
        Sprite.__init__(self, img, frame, size_in_frame, attach_x, attach_y, False)
    
    def set_water_zone(self, y_upper, y_lower, x_left, x_right):
        self.water_zone_y_upper = y_upper
        self.water_zone_y_lower = y_lower
        self.water_zone_x_left = x_left
        self.water_zone_x_right = x_right
        self.set_display_water_zone()       

    def set_display_water_zone(self):
        if self.frame.align == "bottom":
            self.display_water_zone_y_upper = self.frame.align_y - (self.display_height * self.attach_y) + (self.water_zone_y_upper * self.scale)
            self.display_water_zone_y_lower = self.frame.align_y - (self.display_height * self.attach_y) + (self.water_zone_y_lower * self.scale)
            self.display_water_zone_x_left = self.frame.align_x - (self.display_width/2 * self.attach_x) + (self.water_zone_x_left * self.scale)
            self.display_water_zone_x_right = self.frame.align_x - (self.display_width/2 * self.attach_x) + (self.water_zone_x_right * self.scale)
        return (self.display_water_zone_y_upper, self.display_water_zone_y_lower, self.display_water_zone_x_left, self.display_water_zone_x_right)
    
    def in_water_zone(self, x, y):
        if x <= self.display_water_zone_x_right and x >= self.display_water_zone_x_left and y <= self.display_water_zone_y_lower and y >= self.display_water_zone_y_upper:
            return True
        else:
            return False

# Contained by the screen frame
# Has frames for Flower
class Background(Sprite):
    frames = []
    def __init__(self, img, frame, size_in_frame, num_frames, attach_x = 1, attach_y = 1):
        Sprite.__init__(self, img, frame, size_in_frame, attach_x, attach_y, False)
        self.num_frames = num_frames

# A frame pins a sprite at one point using the properties "align", "x", "y"
# align in ["bottom", "top", "left", "right"]
# One Sprite per Frame
# Normal frame: attached to a Background, contains a Flower
# Screen frame: attached to nothing, contains a Background
class Frame:
    # ratios to background width, height
    align_x = 1
    align_y = 1

    sprite = None

    def __init__(self, height, width, background, sprite_type):
        self.height = height
        self.width = width
        self.background = background
        if sprite_type != "background":
            self.background.frames.append(self)
        self.type = sprite_type

    def set_align(self, align, align_x, align_y):
        self.align = align
        self.align_x = align_x
        self.align_y = align_y

    def set_object(self, sprite):
        self.sprite = sprite
        sprite.frame = self

# can move
class WateringCan(Sprite):
    def __init__(self, img, frame, size_in_frame, attach_x = 1, attach_y = 1):
        Sprite.__init__(self, img, frame, size_in_frame, attach_x, attach_y, True)
        
