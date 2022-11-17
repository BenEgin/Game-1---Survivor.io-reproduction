import pygame
from math import sqrt
from pygame.sprite import Sprite
from settings import settings

class character(Sprite):

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.settings = settings()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height

        image1 = pygame.image.load('Sprites/character.png')
        image2 = pygame.image.load('Sprites/character 2.png')
        
        self.image1 = pygame.transform.scale(image1, (100,100))
        self.image2 = pygame.transform.scale(image2, (100,100))
        self.rect = self.image1.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right_arrow = False
        self.moving_right_mouse = False
        self.moving_left_arrow = False
        self.moving_left_mouse = False
        self.moving_up = False
        self.moving_down = False
        self.prev_m_x_pos = 0
        self.prev_m_x_pos = 0
        self.right_lerp = 0
        self.left_lerp = 0
        self.up_lerp = 0
        self.down_lerp = 0


    def update_pos(self,x,speed):
        if x == True:
            self.moving_left_mouse = False
            self.moving_right_mouse = False
            image_rect = self.image1.get_rect()
            image_rect.centerx = self.image1.get_rect().centerx
            image_rect.centery = self.image1.get_rect().centery
            if speed == True:
                self.settings.character_speed = 18
            else:
                self.settings.character_speed = 6
            if self.moving_right_arrow and self.rect.right < self.screen_rect.right - 100:
                self.x += self.settings.character_speed
                self.right_lerp = self.settings.character_speed
            if self.moving_left_arrow and self.rect.left > 100:
                self.x -= self.settings.character_speed
                self.left_lerp = self.settings.character_speed
            if self.moving_up and self.rect.top > 100:
                self.y -= self.settings.character_speed
                self.up_lerp = self.settings.character_speed
            if self.moving_down and self.rect.bottom <self.screen_rect.bottom - 100:
                self.y += self.settings.character_speed
                self.down_lerp = self.settings.character_speed
            print(self.settings.character_speed)
            if self.right_lerp > 0 and self.moving_right_arrow == False:
                self.x += self.right_lerp
                self.right_lerp -= 1
            elif self.left_lerp > 0 and self.moving_left_arrow == False:
                self.x -= self.left_lerp
                self.left_lerp -= 1
            if self.up_lerp > 0 and self.moving_up == False:
                self.y -= self.up_lerp
                self.up_lerp -= 1
            if self.down_lerp > 0 and self.moving_down == False:
                self.y += self.down_lerp
                self.down_lerp -= 1
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.moving_left_arrow = False
            self.moving_right_arrow = False
            m_x_pos, m_y_pos = pygame.mouse.get_pos()
            if speed == True:
                self.x = m_x_pos
                self.y = m_y_pos
            else:
                dx = m_x_pos - self.x
                dy = m_y_pos - self.y
                calc_base = dx*dx + dy*dy 
                distance_m_c = sqrt(calc_base)
                if abs(dx) > 5 or abs(dy) > 5:
                    self.x += dx * self.settings.character_speed / distance_m_c
                    self.y += dy * self.settings.character_speed / distance_m_c
                if dx < -1:
                    self.moving_right_mouse = False
                    self.moving_left_mouse = True
                elif dx > 1:
                    self.moving_left_mouse = False
                    self.moving_right_mouse = True
            if self.x < 100:
                self.x = 100
            elif self.x > self.screen_rect.right - 100:
                self.x = self.screen_rect.right - 100
            if self.y < 150:
                self.y = 150
            elif self.y > self.screen_rect.bottom - 100:
                self.y = self.screen_rect.bottom - 100

            self.rect.centerx = self.x 
            self.rect.centery = self.y


    def blitme(self):
        if self.moving_left_arrow == True or self.moving_left_mouse:
            self.screen.blit(self.image2, self.rect)
        else:
            self.screen.blit(self.image1, self.rect)


    def menu_blitme_left(self):
        self.screen.blit(self.image2, self.rect)
    
    def menu_blitme_right(self):
        self.screen.blit(self.image1, self.rect)




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
        self.rect.centerx = self.settings.starting_pos_character
        self.rect.centery = self.settings.main_menu_y
