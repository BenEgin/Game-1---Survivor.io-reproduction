import pygame
import pygame.font
from pygame.sprite import Sprite
from settings import settings
from character import character


class forcefield(Sprite):
    def __init__(self, ai_game):
        super(Sprite, self).__init__()
        self.settings = settings()
        self.character = character(ai_game)
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (255, 255, 255)

        self.image = pygame.image.load('Sprites/forcefield.png')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.angle = 0
        self.rotated_image_rect = self.image.get_rect()
        self.radius = self.image_width / 2
        self.size_decreaser = 0
        self.size_increaser = 0
        self.red_var = 0
        self.green_var = 255


    """def display_forcefield_charge(self,mode):
        percentage_str = str(int(self.settings.forcefield_charge / self.settings.forcefield_charge_limit * 100))
        display_str = (f"Forcefield Power: {percentage_str}%")
        if mode == True:
            self.text_color = (255, 255, 255)
        else:
            self.text_color = (255,0,0)
        self.score_image = self.font.render(display_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.right / 4
        self.score_rect.centery = 20
        self.screen.blit(self.score_image, self.score_rect)"""

    def display_forcefield_charge(self,mode):
        display_str = ("Forcefield Power: ")
        self.score_image = self.font.render(display_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.right / 4
        self.score_rect.centery = 20
        #colorful rect
        self.bar_width = 250 * self.settings.forcefield_charge / self.settings.forcefield_charge_limit
        self.green_var = 255 * self.settings.forcefield_charge / self.settings.forcefield_charge_limit
        self.red_var = 255 - (255 * self.settings.forcefield_charge / self.settings.forcefield_charge_limit)
        color = (self.red_var,self.green_var,0)
        pygame.draw.rect(self.screen, color, pygame.Rect(self.score_rect.right, self.score_rect.top, self.bar_width, self.score_rect.height))

        self.screen.blit(self.score_image, self.score_rect)

    def update(self):
        self.rect = self.rotated_image_rect


    def blitme(self, powerup_size, charrectcen):
        if powerup_size:
            self.size = 500
            self.size_decreaser_step = 20
            self.size_increaser_step = 40
        else:
            self.size = 250
            self.size_decreaser_step = 10
            self.size_increaser_step = 20
        if self.settings.forcefield_smaller:
            self.smaller_width_height = self.size - self.size_decreaser
            if self.smaller_width_height < 0:
                self.smaller_width_height = 10
            self.scaled_image = pygame.transform.scale(self.image, (self.smaller_width_height, self.smaller_width_height))
            self.scaled_image_width = self.scaled_image.get_width()
            self.radius = self.scaled_image_width / 2
            self.size_decreaser += self.size_decreaser_step
            if self.smaller_width_height < 50:
                self.settings.display_forcefield = False
                self.settings.forcefield_active = False
                self.settings.forcefield_smaller = False
                self.size_decreaser = 0
        elif self.settings.forcefield_bigger:
            self.bigger_width_height = 0 + self.size_increaser
            self.scaled_image = pygame.transform.scale(self.image, (self.bigger_width_height, self.bigger_width_height))
            self.scaled_image_width = self.scaled_image.get_width()
            self.radius = self.scaled_image_width / 2
            self.size_increaser += self.size_increaser_step
            if self.bigger_width_height > self.size:
                self.settings.forcefield_bigger = False
                self.settings.forcefield_normal = True
                self.size_increaser = 0
        elif self.settings.forcefield_normal:
            self.scaled_image = pygame.transform.scale(self.image, (self.size,self.size))
            self.scaled_image_width = self.scaled_image.get_width()
            self.radius = self.scaled_image_width / 2
            self.size_decreaser = 0
        if self.settings.forcefield_smaller or self.settings.forcefield_bigger or self.settings.forcefield_normal:
            self.angle += 10
            self.rot_center(self.scaled_image,self.angle,charrectcen)
            self.screen.blit(self.rotated_image,self.rotated_image_rect)
            if self.angle > 360:
                self.angle = 0


    def rot_center(self, image, angle,charrectcen):
        self.rotated_image = pygame.transform.rotate(image, angle)
        self.rotated_image_rect = self.rotated_image.get_rect()
        self.rotated_image_rect.center = charrectcen 

    
    def forcefield_determine_charge(self,x):
        if self.settings.forcefield_charge > self.settings.forcefield_charge_limit * 0.2 and self.settings.forcefield_min == True:
            self.settings.forcefield_min = False
        elif self.settings.forcefield_active == True and self.settings.forcefield_charge > 0 and self.settings.forcefield_min == False and self.settings.powerup_forcefield_size == False:
            self.decrease_forcefield_charge(x)
            self.settings.display_forcefield = True
        elif self.settings.forcefield_active == False:
            if self.settings.forcefield_charge < self.settings.forcefield_charge_limit:
                self.increase_forcefield_charge(x)
        elif self.settings.forcefield_min == True:
            if self.settings.forcefield_charge < self.settings.forcefield_charge_limit:
                self.increase_forcefield_charge(x)
        elif self.settings.forcefield_charge < 1:
            self.settings.forcefield_min = True
            self.increase_forcefield_charge(x)
        elif self.settings.forcefield_active == True and self.settings.forcefield_charge > 0 and self.settings.forcefield_min == False and self.settings.powerup_forcefield_size == True:
            self.settings.display_forcefield = True


    def decrease_forcefield_charge(self,x):
            if x == False:
                self.settings.forcefield_charge -= 2
            else:
                self.settings.forcefield_charge -= 1
            self.settings.display_forcefield = True


    def increase_forcefield_charge(self,x):
            if self.settings.powerup_forcefield_size == True:
                self.settings.forcefield_charge = self.settings.forcefield_charge_limit
            else:
                if x == False:
                    self.settings.forcefield_charge += 0.3
                else:
                    self.settings.forcefield_charge +=1