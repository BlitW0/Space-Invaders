import pygame
from globalVariables import *


class Ship():

    def __init__(self, display, image):
        self.image = image
        self.display = display
        self.x = display.get_width() / 2 - self.image.get_width() / 2
        self.y = display.get_height() - self.image.get_height() - 50
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.x_change = 0
        self.hit_count = 0

    def draw(self):
        self.display.blit(self.image, (self.x, self.y))

    def move(self):
        if self.x + self.x_change > 10 and self.x + self.x_change < self.display.get_width() - self.image.get_width() - 10:
            self.x += self.x_change
            self.rect.centerx += self.x_change

    def display_score(self):
        font = pygame.font.SysFont(None, 50)
        text = font.render("Score: " + str(self.hit_count), True, white)
        text_rect = text.get_rect()
        text_rect.center = (self.display.get_width() / 2, 50)
        self.display.blit(text, text_rect)
