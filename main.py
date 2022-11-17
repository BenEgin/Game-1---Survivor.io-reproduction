from random import randint
from math import sqrt
import pygame
import sys
from settings import settings
from character import character
from challenger import Challenger
from forcefield import forcefield
from Hearts import Heart
from pointsscored import pointsscored
from pointsscored import Highscore
from buttons import Start_Game
from buttons import options
from buttons import quit
from buttons import steering
from buttons import return_menu_button
from buttons import Hard_Mode_button
from buttons import main_menu_tips
from powerups import forcefield_size_powerup
from powerups import speed_character_powerup
from background import game_background
from background import menu_background
from background import options_background


class main:
    def __init__(self):
        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("SURVIVOR")
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        self.character = character(self)
        self.challenger = Challenger(self)
        self.challengers_red = pygame.sprite.Group()
        self.challengers_blue = pygame.sprite.Group()
        self.challengers_pink = pygame.sprite.Group()
        self.challengers_orange = pygame.sprite.Group()
        self.forcefield = forcefield(self)
        self.ps = pointsscored(self)
        self.hs = Highscore(self)
        self.heart = Heart(self)   
        self.hearts = pygame.sprite.Group()
        self.start_game = Start_Game(self)
        self.options = options(self)
        self.quit = quit(self)
        self.steering = steering(self)
        self.return_menu = return_menu_button(self)
        self.forcefield_powerup = forcefield_size_powerup(self)
        self.forcefield_powerups = pygame.sprite.Group()
        self.speed_powerup = speed_character_powerup(self)
        self.speed_powerups = pygame.sprite.Group()
        self.bg = game_background(self)
        self.mbg = menu_background(self)
        self.obg = options_background(self)
        self.hard_mode = Hard_Mode_button(self)
        self.mm_tips = main_menu_tips(self)
        self.tick = 1
        self.game_over_tick = 1
        self.powerup_counter_forcefield = 1
        self.powerup_counter_speed = 1
        self.powerup_counter_limit = 1000
        self.clock = pygame.time.Clock()
        self.settings.background_move_x = self.screen.get_width() / 2
        self.settings.background_move_y = self.screen.get_height() / 2
        self.image_game_over = pygame.image.load('Sprites/game_over.png')
        self.image_game_over_rect = self.image_game_over.get_rect()
        self.image_game_over_rect.center = self.screen.get_rect().center
        self.character.main_menu_setup()
        self.challenger.main_menu_setup()
        self.back_change_rem_x = 0
        self.back_change_rem_y = 0


    def run_game(self):
        while True:
            print(self.settings.score)
            if self.settings.main_menu == True:
                self.clock.tick(90)
                self.running_loop_menu()
            elif self.settings.options_menu == True:
                self.clock.tick(90) 
                self.running_loop_options()
            elif self.settings.game_over == True:
                self.clock.tick(90)
                self.game_over()
                self.game_over_tick += 1
            else:
                self.clock.tick(60)
                self.running_loop_game()


    def running_loop_game(self):
        if self.settings.game_active:
            self.check_events()
            self.character.update_pos(self.settings.movement_type_arrows,self.settings.powerup_speed_character)
            self.forcefield.update()
            self.forcefield.forcefield_determine_charge(self.settings.hardcore_mode)
            if self.settings.powerup_forcefield_size == True:
                self.powerup_counter_forcefield +=2
                if self.powerup_counter_forcefield > self.powerup_counter_limit:
                    self.settings.powerup_forcefield_size = False
                    self.powerup_counter_forcefield = 1
            if self.settings.powerup_speed_character == True:
                self.powerup_counter_speed += 2
                if self.powerup_counter_speed > self.powerup_counter_limit:
                    self.settings.powerup_speed_character = False
                    self.powerup_counter_speed = 1
         
            self.challenger_hit()
            self.character_hit()
            self.powerup_hit()
            if self.settings.spawn_counter < self.tick:
                self.spawn_challengers()   
                self.tick = 1
            self.tick +=2
            self.update_screen()
            self.back_change_rem_x = self.settings.background_move_x
            self.back_change_rem_y = self.settings.background_move_y


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.bg.display_background(self.character.rect)
        if self.settings.display_forcefield:
            self.forcefield.blitme(self.settings.powerup_forcefield_size,self.character.rect.center)
        self.character.blitme()
        self.ps.prep_score(self.settings.hardcore_mode,self.settings.score)
        self.ps.show_score()
        self.hs.show_highscore(self.settings.hardcore_mode)
        self.forcefield.display_forcefield_charge(self.settings.hardcore_mode)
        self.challengers_movement(self.settings.background_move_x, self.settings.background_move_y)
        self.display_powerups(self.settings.background_move_x, self.settings.background_move_y)
        self.heart.blitme_hearts(self.settings.character_lives)
        self.forcefield_powerup.display_powerup_charge(self.settings.powerup_forcefield_size,self.powerup_counter_forcefield,self.powerup_counter_limit)
        self.speed_powerup.display_powerup_charge(self.settings.powerup_speed_character  ,self.powerup_counter_speed,self.powerup_counter_limit, self.settings.powerup_forcefield_size)
        pygame.display.flip()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)  
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)
            

    def keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right_arrow = True
        elif event.key == pygame.K_LEFT:
            self.character.moving_left_arrow = True
        elif event.key == pygame.K_UP:
            self.character.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.character.moving_down = True  
        elif event.key == pygame.K_SPACE:
            self.settings.forcefield_active = True
            self.settings.display_forcefield = True
            self.settings.forcefield_bigger = True 
            self.settings.forcefield_smaller = False
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self.settings.game_active = False
            self.settings.main_menu = True
            self.settings.pause_menu = True       


    def keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right_arrow = False
        elif event.key == pygame.K_LEFT:
            self.character.moving_left_arrow = False
        elif event.key == pygame.K_UP:
            self.character.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.character.moving_down = False 
        elif event.key == pygame.K_SPACE:
            self.settings.forcefield_smaller = True
            self.settings.forcefield_normal = False
            self.settings.forcefield_active = False


    def update_spawnrate(self):
        self.settings.spawn_counter =  50 * (1 -self.settings.score/20000)
        if self.settings.spawn_counter < 5:
            self.settings.spawn_counter = 5


    def spawn_challengers(self):
        new_challenger = Challenger(self)
        new_challenger.x = randint(-200, self.settings.screen_width + 200)
        if new_challenger.x < 0 or new_challenger.x > self.settings.screen_width:
            new_challenger.y = randint(-200, self.settings.screen_height + 200)
        else:
            up_or_down = randint(1,2)
            if up_or_down == 1:
                new_challenger.y = randint(-200, -100)
            else:
                new_challenger.y = randint(self.settings.screen_height + 100, self.settings.screen_height + 200)
        sprite_color = randint(1,4)
        if sprite_color == 1:
            self.challengers_red.add(new_challenger)
        elif sprite_color == 2:
            self.challengers_blue.add(new_challenger)
        elif sprite_color == 3:
            self.challengers_orange.add(new_challenger)
        elif sprite_color == 4:
            self.challengers_pink.add(new_challenger)

    
    def challengers_movement(self,bx,by):
        for i in range(1,5):
            if i == 1:
                i = self.challengers_blue
            elif i == 2:
                i = self.challengers_red
            elif i == 3:
                i = self.challengers_orange
            elif i == 4:
                i = self.challengers_pink
            for enemy in i:
                enemy.x -= self.back_change_rem_x - bx
                enemy.y -= self.back_change_rem_y - by
                distance_x = self.character.x - enemy.rect.x
                distance_y = self.character.y - enemy.rect.y
                vector = int(sqrt(distance_x * distance_x + distance_y * distance_y))
                enemy.x += distance_x * self.settings.challenger_speed / vector 
                enemy.y += distance_y * self.settings.challenger_speed / vector
                enemy.rect.x = enemy.x
                enemy.rect.y = enemy.y
                if abs(distance_x) > abs(distance_y):
                    enemy.axis_assignment = True
                else:
                    enemy.axis_assignment = False
                if enemy.axis_assignment == True:
                    if i == self.challengers_blue:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_blue_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_blue_looking_right, enemy.rect)
                    elif i == self.challengers_red:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_red_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_red_looking_right, enemy.rect)
                    elif i == self.challengers_orange:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_orange_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_orange_looking_right, enemy.rect)
                    elif i == self.challengers_pink:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_pink_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_pink_looking_right, enemy.rect)
                else:
                    if i == self.challengers_blue:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_blue_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_blue_looking_down, enemy.rect)
                    elif i == self.challengers_red:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_red_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_red_looking_down, enemy.rect)
                    elif i == self.challengers_orange:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_orange_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_orange_looking_down, enemy.rect)
                    elif i == self.challengers_pink:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_pink_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_pink_looking_down, enemy.rect)        
              


    def character_hit(self):
        if self.settings.display_forcefield == False:
            collide_char_chal_red = pygame.sprite.spritecollideany(self.character, self.challengers_red)
            collide_char_chal_blue = pygame.sprite.spritecollideany(self.character, self.challengers_blue)
            collide_char_chal_orange = pygame.sprite.spritecollideany(self.character, self.challengers_orange)
            collide_char_chal_pink = pygame.sprite.spritecollideany(self.character, self.challengers_pink)
            if collide_char_chal_red or collide_char_chal_blue or collide_char_chal_orange or collide_char_chal_pink:
                self.settings.character_lives -= 1
                self.challengers_red.empty()
                self.challengers_blue.empty()
                self.challengers_orange.empty()
                self.challengers_pink.empty()
                self.speed_powerups.empty()
                self.forcefield_powerups.empty()
                self.character.rect.centerx = self.settings.screen_width / 2
                self.character.rect.centery = self.settings.screen_height/2
                self.hearts.clear
                self.settings.forcefield_charge = self.settings.forcefield_charge_limit
                if self.settings.character_lives < 1:
                    self.hs.check_highscore()
                    self.settings.game_over = True
                    self.settings.game_active = False

    
    def challenger_hit(self):
        for i in range(1,5):
            if i == 1:
                y = self.challengers_red
            elif i == 2:
                y = self.challengers_blue
            elif i == 3:
                y = self.challengers_orange
            else:
                y = self.challengers_pink
            collide_force_chall = pygame.sprite.spritecollideany(self.forcefield, y, pygame.sprite.collide_circle)
            if self.settings.display_forcefield and collide_force_chall:
                if randint(1,100) < self.settings.percentage_powerup:
                    x = randint(1,2)
                    if x == 1 and self.settings.powerup_forcefield_size == False:
                        self.create_powerup_forcefield_size(collide_force_chall.x,collide_force_chall.y)
                    elif x == 2 and self.settings.powerup_speed_character == False:
                        self.create_powerup_character_speed(collide_force_chall.x,collide_force_chall.y)            
                y.remove(collide_force_chall)
                self.settings.score += 50
         

    def create_powerup_forcefield_size(self,x,y):
        if self.settings.powerup_forcefield_size == False:
            new_powerup = forcefield_size_powerup(self)     
            new_powerup.rect.x = x 
            new_powerup.rect.y = y      
            new_powerup.x = new_powerup.rect.x
            new_powerup.y = new_powerup.rect.y         
            self.forcefield_powerups.add(new_powerup)


    def create_powerup_character_speed(self,x,y):
        if self.settings.powerup_speed_character == False:
            new_powerup = speed_character_powerup(self)     
            new_powerup.rect.x = x 
            new_powerup.rect.y = y         
            new_powerup.x = new_powerup.rect.x
            new_powerup.y = new_powerup.rect.y
            self.speed_powerups.add(new_powerup)
 

    def display_powerups(self,bx,by):
        for powerup_displayer in self.forcefield_powerups:  
            powerup_displayer.x -= self.back_change_rem_x - bx
            powerup_displayer.y -= self.back_change_rem_y - by
            powerup_displayer.rect.x = powerup_displayer.x
            powerup_displayer.rect.y = powerup_displayer.y
            self.screen.blit(self.forcefield_powerup.forcefield_powerup_image, powerup_displayer.rect)
        for powerup_displayer in self.speed_powerups: 
            powerup_displayer.x -= self.back_change_rem_x - bx
            powerup_displayer.y -= self.back_change_rem_y - by
            powerup_displayer.rect.x = powerup_displayer.x
            powerup_displayer.rect.y = powerup_displayer.y
            self.screen.blit(self.speed_powerup.speed_character_powerup_image, powerup_displayer.rect)   


    def powerup_hit(self):
        collided_powerup_forcefield_size = pygame.sprite.spritecollideany(self.character,self.forcefield_powerups)
        if collided_powerup_forcefield_size:
            self.settings.powerup_forcefield_size = True
            self.forcefield_powerups.empty()      
        collided_powerup_character_speed = pygame.sprite.spritecollideany(self.character,self.speed_powerups)      
        if collided_powerup_character_speed:
            self.settings.powerup_speed_character = True
            self.speed_powerups.empty()      




###############
###############
###############
# Menu control and detections


    def running_loop_menu(self):
        self.check_menu_events()
        self.movement_distributor()
        self.update_screen_menu()


    def check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events_menu(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events_menu(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.start_game.mouseclick(x,y) == True:
                    self.character.rect.center = self.screen.get_rect().center
                    self.settings.main_menu = False
                    self.settings.game_active = True
                    self.settings.pause_menu == False
                if self.options.mouseclick(x,y) == True:
                    self.settings.main_menu = False
                    self.settings.options_menu = True
                if self.quit.mouseclick(x,y) == True:
                    if self.settings.pause_menu == True:
                        self.character.main_menu_setup()
                        self.challenger.main_menu_setup()
                        self.settings.pause_menu = False
                        self.settings.main_menu = True
                    else:
                        sys.exit()


    def keydown_events_menu(self,event):
        if event.key == pygame.K_SPACE:
            self.settings.menu_attack = True
            self.settings.forcefield_active = True
            self.settings.display_forcefield = True
            self.settings.forcefield_bigger = True 
            self.settings.forcefield_smaller = False
        elif event.key == pygame.K_q:
            sys.exit()


    def keyup_events_menu(self,event):
        if event.key == pygame.K_SPACE:
            self.settings.menu_attack = False
            self.settings.forcefield_smaller = True
            self.settings.forcefield_active = False
            self.settings.forcefield_normal = False


    def movement_distributor(self):
        if self.settings.pause_menu == False:
            if self.settings.menu_attack == True:
                self.character.menu_movement_left()
                self.challenger.menu_movement_left()
            else:
                self.character.menu_movement_right()
                self.challenger.menu_movement_right()


    def update_screen_menu(self):
        x, y = pygame.mouse.get_pos()
        if self.settings.pause_menu == False:
            self.mbg.display_background()
            self.forcefield.update()
            self.forcefield.blitme(self.settings.powerup_forcefield_size,self.character.rect.center)
            if self.settings.menu_attack == True:
                self.challenger.main_menu_blitme_left()
                self.character.menu_blitme_left()
            else:
                self.challenger.draw_challenger()
                self.character.menu_blitme_right()
            self.mbg.display_background_lower()
            self.mm_tips.display_hint_text(self.mm_tips.hint)
        else:
            self.bg.display_background(self.character.rect)
            self.ps.prep_score(self.settings.hardcore_mode)
            self.ps.show_score()
            self.character.blitme()
            self.hs.show_highscore(self.settings.hardcore_mode)
            self.forcefield.display_forcefield_charge(self.settings.hardcore_mode)
            self.display_powerups(self.settings.background_move_x, self.settings.background_move_y)
            self.heart.blitme_hearts(self.settings.character_lives)
            self.forcefield_powerup.display_powerup_charge(self.settings.powerup_forcefield_size,self.powerup_counter_forcefield,self.powerup_counter_limit)
            self.speed_powerup.display_powerup_charge(self.settings.powerup_speed_character  ,self.powerup_counter_speed,self.powerup_counter_limit, self.settings.powerup_forcefield_size)
            self.blit_challengers_pause_menu()
        self.start_game.display_start_game(self.settings.pause_menu,self.settings.hardcore_mode,x,y)
        self.options.display_options(self.settings.hardcore_mode,x,y)
        self.quit.display_quit(self.settings.pause_menu,self.settings.hardcore_mode,x,y)
        pygame.display.flip()


    def blit_challengers_pause_menu(self):
        for i in range(1,5):
            if i == 1:
                i = self.challengers_blue
            elif i == 2:
                i = self.challengers_red
            elif i == 3:
                i = self.challengers_orange
            elif i == 4:
                i = self.challengers_pink
            for enemy in i:
                distance_x = self.character.x - enemy.rect.x
                distance_y = self.character.y - enemy.rect.y
                if sqrt(distance_x*distance_x) > sqrt(distance_y*distance_y):
                    enemy.axis_assignment = True
                else:
                    enemy.axis_assignment = False
                if enemy.axis_assignment == True:
                    if i == self.challengers_blue:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_blue_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_blue_looking_right, enemy.rect)
                    elif i == self.challengers_red:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_red_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_red_looking_right, enemy.rect)
                    elif i == self.challengers_orange:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_orange_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_orange_looking_right, enemy.rect)
                    elif i == self.challengers_pink:
                        if distance_x < 0:
                            self.screen.blit(self.challenger.image_pink_looking_left, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_pink_looking_right, enemy.rect)
                else:
                    if i == self.challengers_blue:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_blue_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_blue_looking_down, enemy.rect)
                    elif i == self.challengers_red:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_red_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_red_looking_down, enemy.rect)
                    elif i == self.challengers_orange:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_orange_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_orange_looking_down, enemy.rect)
                    elif i == self.challengers_pink:
                        if distance_y < 0:
                            self.screen.blit(self.challenger.image_pink_looking_up, enemy.rect)
                        else:
                            self.screen.blit(self.challenger.image_pink_looking_down, enemy.rect)


    ###############
    ###############
    ###############    
    # options menu



    def running_loop_options(self):
        self.check_options_events()
        self.update_screen_options()


    def check_options_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events_options(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events_options(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if self.steering.mouseclick(x,y) == True:
                    if self.settings.movement_type_arrows == True:
                        self.settings.movement_type_arrows = False
                    elif self.settings.movement_type_arrows == False:
                        self.settings.movement_type_arrows = True
                elif self.return_menu.mouseclick(x,y) == True:
                    self.settings.options_menu = False
                    self.settings.main_menu = True
                elif self.hard_mode.mouseclick(x,y) == True:
                    if self.settings.hardcore_mode == False:
                        self.settings.hardcore_mode = True
                        self.settings.forcefield_charge_limit = 500
                        self.settings.forcefield_charge = self.settings.forcefield_charge_limit
    
                    else:
                        self.settings.hardcore_mode = False
                        self.settings.forcefield_charge_limit = 250
                        self.settings.forcefield_charge = self.settings.forcefield_charge_limit

    
    def keydown_events_options(self,event):
        if event.key == pygame.K_SPACE:
            self.settings.menu_attack = True
        elif event.key == pygame.K_q:
            sys.exit()


    def keyup_events_options(self,event):
        if event.key == pygame.K_SPACE:
            self.settings.menu_attack = False
    

    def update_screen_options(self):
        x,y = pygame.mouse.get_pos()
        self.obg.display_background()
        if self.steering.update_steering_options(self.settings.movement_type_arrows,x,y) == True:
            self.settings.movement_type_arrows = True
        elif self.steering.update_steering_options(self.settings.movement_type_arrows,x,y) == False:
            self.settings.movement_type_arrows = False
        self.return_menu.blitme(self.settings.pause_menu,x,y)
        self.hard_mode.blitme(self.settings.hardcore_mode,x,y)
        pygame.display.flip()



###########
###########
###########
# game over



    def game_over(self):
        i = 1
        self.game_over_display()
        while i < 1000:
            self.game_over_screen()
            i += 1
        self.settings.game_over = False
        self.settings.main_menu = True
        self.character.main_menu_setup()
        self.challenger.main_menu_setup()
        self.settings.character_lives = 3
        self.settings.score = 0


    def game_over_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.image_game_over,self.image_game_over_rect)
        self.game_over_message_blit()
        self.show_score_game_over()
        pygame.display.flip()


    def game_over_message_blit(self):
        text_str = "GAME OVER"
        self.text_color_game_over = (255, 255, 255)
        self.font_game_over = pygame.font.SysFont(None, 100)
        self.game_over_message = self.font_game_over.render(text_str, True, self.text_color_game_over, self.settings.bg_color)
        self.game_over_message_rect = self.game_over_message.get_rect()
        self.game_over_message_rect.centerx = self.screen.get_rect().centerx
        self.game_over_message_rect.centery = self.screen.get_rect().bottom / 4 * 1
        self.screen.blit(self.game_over_message, self.game_over_message_rect)


    def game_over_display(self):
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None,100)
        score_str = str(self.settings.score)
        text_str = ("Score: ")
        display_str = text_str + score_str
        self.score_image_game_over = self.font.render(display_str, True, self.text_color, self.settings.bg_color)
        self.score_rect_game_over = self.score_image_game_over.get_rect()
        self.score_rect_game_over.centery = self.screen.get_rect().height * 0.8
        self.score_rect_game_over.centerx = self.screen.get_rect().width / 2


    def show_score_game_over(self):
        self.screen.blit(self.score_image_game_over,self.score_rect_game_over)


if __name__ == '__main__':
    ai = main()
    ai.run_game()