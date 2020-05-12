import pygame
import random
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT

# all resizing looks at display_height
class Sprite:
    def __init__(self, img, frame, size_in_frame, attach_x, attach_y):
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
    
    def get_display_coordinates(self):
        frame_align = self.frame.align
        if frame_align == "bottom":
            self.display_x = self.frame.align_x - (self.display_width/2 * self.attach_x)
            self.display_y = self.frame.align_y - (self.display_height * self.attach_y)
        return (self.display_x, self.display_y)

# Contained by a Background
class Flower(Sprite):   
    def __init__(self, img, frame, size_in_frame, attach_x = 1, attach_y = 1):
        Sprite.__init__(self, img, frame, size_in_frame, attach_x, attach_y)

# Contained by the screen frame
# Has frames for Flower
class Background(Sprite):
    def __init__(self, img, frame, size_in_frame, num_frames, attach_x = 1, attach_y = 1):
        Sprite.__init__(self, img, frame, size_in_frame, attach_x, attach_y)
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
    def __init__(self, name, img):
        Sprite.__init__(self, name, img)
        self.frame = background
