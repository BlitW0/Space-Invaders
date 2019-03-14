import pygame


class Missile():

    def __init__(self, display, image, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.image = image
        self.display = display
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        self.display.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.v

    def hit(self, alien):
        if alien.rect.left < self.rect.centerx < alien.rect.right:
            if self.y <= alien.rect.bottom:
                return True
        if self.rect.centerx < alien.rect.left:
            if self.rect.right > alien.rect.left:
                if self.y <= alien.rect.bottom:
                    return True
        if self.rect.centerx > alien.rect.right:
            if self.rect.left < alien.rect.right:
                if self.y <= alien.rect.bottom:
                    return True
