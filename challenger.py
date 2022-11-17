from random import randint
from character import character
import pygame
from pygame.sprite import Sprite
from character import character
from settings import settings
from buttons import main_menu_tips


class Challenger(Sprite):


    def __init__(self, ai_game):
        
        super().__init__()
        self.character = character(ai_game)
        self.settings = settings()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.mm_tips = main_menu_tips(self)

        # red challengers
        challenger_red_right = pygame.image.load('Sprites/challenger right.png')
        challenger_red_left = pygame.image.load('Sprites/challenger left.png')
        challenger_red_down = pygame.image.load('Sprites/challenger down.png')
        challenger_red_up = pygame.image.load('Sprites/challenger up.png')

        self.image_red_looking_right = pygame.transform.scale(challenger_red_right, (50,50))
        self.image_red_looking_left = pygame.transform.scale(challenger_red_left, (50,50))
        self.image_red_looking_up = pygame.transform.scale(challenger_red_up, (50,50))
        self.image_red_looking_down = pygame.transform.scale(challenger_red_down, (50,50))


        challenger_blue_right = pygame.image.load('Sprites/blue_right.png')
        challenger_blue_left = pygame.image.load('Sprites/blue_left.png')
        challenger_blue_down = pygame.image.load('Sprites/blue_down.png')
        challenger_blue_up = pygame.image.load('Sprites/blue_up.png')
        self.image_blue_looking_right = pygame.transform.scale(challenger_blue_right, (50,50))
        self.image_blue_looking_left = pygame.transform.scale(challenger_blue_left, (50,50))
        self.image_blue_looking_up = pygame.transform.scale(challenger_blue_up, (50,50))
        self.image_blue_looking_down = pygame.transform.scale(challenger_blue_down, (50,50))

        challenger_orange_right = pygame.image.load('Sprites/orange_right.png')
        challenger_orange_left = pygame.image.load('Sprites/orange_left.png')
        challenger_orange_down = pygame.image.load('Sprites/orange_down.png')
        challenger_orange_up = pygame.image.load('Sprites/orange_up.png')
        self.image_orange_looking_right = pygame.transform.scale(challenger_orange_right, (50,50))
        self.image_orange_looking_left = pygame.transform.scale(challenger_orange_left, (50,50))
        self.image_orange_looking_up = pygame.transform.scale(challenger_orange_up, (50,50))
        self.image_orange_looking_down = pygame.transform.scale(challenger_orange_down, (50,50))

        challenger_pink_right = pygame.image.load('Sprites/pink_right.png')
        challenger_pink_left = pygame.image.load('Sprites/pink_left.png')
        challenger_pink_down = pygame.image.load('Sprites/pink_down.png')
        challenger_pink_up = pygame.image.load('Sprites/pink_up.png')
        self.image_pink_looking_right = pygame.transform.scale(challenger_pink_right, (50,50))
        self.image_pink_looking_left = pygame.transform.scale(challenger_pink_left, (50,50))
        self.image_pink_looking_up = pygame.transform.scale(challenger_pink_up, (50,50))
        self.image_pink_looking_down = pygame.transform.scale(challenger_pink_down, (50,50))

        challenger_scared = pygame.image.load('Sprites/scared_ghost.png')
        self.image_scared = pygame.transform.scale(challenger_scared, (50,50))

        self.rect = self.image_red_looking_right.get_rect()

        self.rect.x = randint(0,self.settings.screen_width)
        self.rect.y = randint(0,self.settings.screen_height)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y


    def draw_challenger(self):
        if self.moving_left:
            self.screen.blit(self.image_red_looking_left, self.rect)
        elif self.moving_down:
            self.screen.blit(self.image_red_looking_down, self.rect)
        elif self.moving_up:
            self.screen.blit(self.image_red_looking_up, self.rect)
        else:
            self.screen.blit(self.image_red_looking_right, self.rect)


    def menu_movement_right(self):
        if self.rect.centerx > self.width + 200:
            self.rect.centerx = -200
        else:
            self.rect.centerx += 7


    def menu_movement_left(self):
        if self.rect.centerx < -200:
            self.rect.centerx = self.width + 200
        else:
            self.rect.centerx -= 7


    def main_menu_setup(self):
        self.rect.centerx = self.settings.starting_pos_challenger
        self.rect.centery = self.settings.main_menu_y


    def main_menu_blitme_left(self):
        self.screen.blit(self.image_scared, self.rect)

