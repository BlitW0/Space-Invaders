import random
import pygame


class Alien():

    def __init__(self, display, image, x, y, time):
        self.image = image
        self.display = display
        self.x = x
        self.y = y
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pygame.Rect(x, y, width, height)
        self.spawn_time = time

    def draw(self):
        self.display.blit(self.image, (self.x, self.y))
