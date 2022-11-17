import pygame
from character import character
from settings import settings

class forcefield_size_powerup(pygame.sprite.Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Sprites/powerup_1.png')
        self.forcefield_powerup_image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.forcefield_powerup_image.get_rect()
        self.character = character(self)
        self.settings = settings()
        self.display = False
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

    def update_initial(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y
        self.display = True


    def display_powerup_charge(self,x,counter,counterlimit):
        if x == True:
            score_str = str(int(100 - counter/counterlimit*100))
            display_str = str(f"Power-Up Charge: {score_str}%")

            self.charge_image = self.font.render(display_str, True, self.text_color, None)
            self.charge_rect = self.charge_image.get_rect()
            self.charge_rect.left = self.screen_rect.right / 4
            self.charge_rect.centery = 60
            self.screen.blit(self.charge_image, self.charge_rect)

class speed_character_powerup(pygame.sprite.Sprite):

    def __init__(self,ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Sprites/lightning.png')
        self.speed_character_powerup_image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.speed_character_powerup_image.get_rect()
        self.character = character(self)
        self.settings = settings()
        self.display = False
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.y_pos_decider = 40


    def display_powerup_charge(self,x,counter,counterlimit,y):
        if x == True:
            score_str = str(int(100 - counter/counterlimit*100))
            display_str = str(f"Speed Charge: {score_str}%")
            self.get_y_pos(y)
  
            self.charge_image = self.font.render(display_str, True, self.text_color, None )
            self.charge_rect = self.charge_image.get_rect()
            self.charge_rect.left = self.screen_rect.right / 4
            self.charge_rect.centery = self.y_pos
            self.screen.blit(self.charge_image, self.charge_rect)

    def get_y_pos(self,x):
        self.y_pos = 60
        if x == True:
            self.y_pos = 100
        