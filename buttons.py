import random
import pygame
from settings import settings
from character import character


class Start_Game():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.settings = settings()
        self.character = character(self)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)


    def display_start_game(self,x,y,mx,my):
        if x == False:
            text_str = "Start New Game"
        else:
            text_str = "Continue Game"
        if y == False:
            self.text_color = (255, 0,0)
        else:
            self.text_color = (255, 255, 255)
        self.image = self.font.render(text_str, True, self.text_color, None)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.width / 2
        self.image_rect.centery = self.height / 4
        if mx>self.image_rect.left and mx < self.image_rect.right and my > self.image_rect.top and my < self.image_rect.bottom or self.settings.pause_menu == True:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(180)
        self.screen.blit(self.image, self.image_rect)

    def mouseclick(self,x,y):
        if x > self.image_rect.left and x < self.image_rect.right and y > self.image_rect.top and y< self.image_rect.bottom:
            return True
        else:
            return False


class options():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.settings = settings()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)



    def display_options(self,y,mx,my):
        text_str = "Options"
        if y == False:
            self.text_color = (255, 0,0)
        else:
            self.text_color = (255, 255, 255)
        self.image = self.font.render(text_str, True, self.text_color, None)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.width / 2
        self.image_rect.centery = self.height / 2
        if mx>self.image_rect.left and mx < self.image_rect.right and my > self.image_rect.top and my < self.image_rect.bottom or self.settings.pause_menu == True:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(180)
        self.screen.blit(self.image, self.image_rect)



    def mouseclick(self,x,y):
        if x > self.image_rect.left and x < self.image_rect.right and y > self.image_rect.top and y< self.image_rect.bottom:
            return True
        else:
            return False




class quit():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.settings = settings()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)



    def display_quit(self,x,y,mx,my):
        if x == False:
            text_str = "Quit"
        else:
            text_str = "Return to main menu"
        if y == False:
            self.text_color = (255, 0,0)
        else:
            self.text_color = (255, 255, 255)
        self.image = self.font.render(text_str, True, self.text_color, None)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.width / 2
        self.image_rect.centery = self.height / 4 * 3
        if mx>self.image_rect.left and mx < self.image_rect.right and my > self.image_rect.top and my < self.image_rect.bottom or self.settings.pause_menu == True:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(180)
        self.screen.blit(self.image, self.image_rect)


    
    def mouseclick(self,x,y,):
        if x > self.image_rect.left and x < self.image_rect.right and y > self.image_rect.top and y< self.image_rect.bottom:
            return True
        else:
            return False

    
class main_menu_tips():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.settings = settings()
        self.character = character(self)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.hint = str
        self.determine_hint_text()

    
    def determine_hint_text(self):
        myFile = open("hints.txt", "r")
        x = myFile.readlines()
        self.hint_initial = random.choice(x)
        self.hint = self.hint_initial.rstrip(self.hint_initial[-1])
        myFile.close()
    
    
    def display_hint_text(self,x):
        text_str = ("Hint: ")
        display_str = text_str + x 
        self.score_image = self.font.render(display_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.width / 2
        self.score_rect.centery = self.height/9 * 8
        self.screen.blit(self.score_image, self.score_rect)



###########
###########
###########
# Options Buttons

class steering():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.settings = settings()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)


    def update_steering_options(self,x,mx,my):
        if x == False:
            text_str = "Mouse Control"
            self.image = self.font.render(text_str, True, self.text_color, None)
        else:
            text_str = "Arrow Control"
            self.image = self.font.render(text_str, True, self.text_color, None)
            
        
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.width / 2
        self.image_rect.centery = self.height / 4 * 3
        if mx>self.image_rect.left and mx < self.image_rect.right and my > self.image_rect.top and my < self.image_rect.bottom or self.settings.pause_menu == True:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(180)
        self.screen.blit(self.image,self.image_rect)

        if x == False:
            return False
        if x == True:
            return True

    
    def mouseclick(self, x, y):
        if x > self.image_rect.left and x < self.image_rect.right and y > self.image_rect.top and y< self.image_rect.bottom and self.settings.movement_type_arrows == True:
            return True
        elif x > self.image_rect.left and x < self.image_rect.right and y > self.image_rect.top and y< self.image_rect.bottom and self.settings.movement_type_arrows == False:
            return True
        else:
            return False



class return_menu_button():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.settings = settings()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)


    def blitme(self,x,mx,my):
        if x == True:
            text_str = "Pause Menu"
        else:
            text_str = "Main Menu"
        self.image = self.font.render(text_str, True, self.text_color, None)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.width / 2
        self.image_rect.centery = self.height / 4 * 1
        if mx>self.image_rect.left and mx < self.image_rect.right and my > self.image_rect.top and my < self.image_rect.bottom or self.settings.pause_menu == True:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(180)
        self.screen.blit(self.image, self.image_rect)

    
    def mouseclick(self,x,y):
        if x > self.image_rect.left and x < self.image_rect.right and y > self.image_rect.top and y< self.image_rect.bottom:
            return True
        else:
            return False


class Hard_Mode_button():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.settings = settings()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)


    def blitme(self,x,mx,my):
        if x == True:
            self.text_color = (255, 255, 255)
            text_str = "Normal Mode"
            self.image = self.font.render(text_str, True, self.text_color, None)
        else:
            self.text_color = (255, 0, 0)
            text_str = "Hard Mode"
            self.image = self.font.render(text_str, True, self.text_color, None)
        
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.width / 2
        self.image_rect.centery = self.height / 2
        if mx>self.image_rect.left and mx < self.image_rect.right and my > self.image_rect.top and my < self.image_rect.bottom or self.settings.pause_menu == True:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(180)
        self.screen.blit(self.image,self.image_rect)

    
    def mouseclick(self,x,y):
        if x > self.image_rect.left and x < self.image_rect.right and y > self.image_rect.top and y< self.image_rect.bottom:
            return True
        else:
            return False