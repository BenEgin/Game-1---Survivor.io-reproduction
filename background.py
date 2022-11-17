import pygame
from pygame.sprite import Sprite
from settings import settings
from character import character

class game_background(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.settings = settings()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.character = character(self)

        image = pygame.image.load('Sprites/PygameBackground1.png')
        self.bgimage = pygame.transform.scale(image, (self.width * 2, self.height * 2))
        self.background_rect = self.bgimage.get_rect()

    def background_mover(self,x):
        self.settings.background_move_x = self.width/2 - x.centerx
        self.settings.background_move_y = self.height/2 - x.centery

    def display_background(self,x):
        self.background_mover(x)
        self.background_rect.centerx = self.width/2 + self.settings.background_move_x
        self.background_rect.centery = self.height/2 + self.settings.background_move_y
        self.screen.blit(self.bgimage, self.background_rect)


class menu_background(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.settings = settings()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height

        image1 = pygame.image.load('Sprites/menu_background.png')
        self.bgimage = pygame.transform.scale(image1, (self.width, self.height))
        self.background_rect = self.bgimage.get_rect()
        
        image2 = pygame.image.load('Sprites/menu_background_lower.png')
        self.bgimage_lower = pygame.transform.scale(image2, (self.width, self.height))
        self.background_rect_lower = self.bgimage.get_rect()

    def display_background(self):
        self.screen.blit(self.bgimage, self.background_rect)
    
    
    
    def display_background_lower(self):
        self.screen.blit(self.bgimage_lower, self.background_rect_lower)


class options_background(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.settings = settings()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height

        image1 = pygame.image.load('Sprites/options_background.png')
        self.bgimage = pygame.transform.scale(image1, (self.width, self.height))
        self.background_rect = self.bgimage.get_rect()

    
    def display_background(self):
        self.screen.blit(self.bgimage, self.background_rect)

