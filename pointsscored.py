import pygame.font
from settings import settings

class pointsscored:
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.settings = settings()

        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
            
        # Font settings for scoring information.
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (255, 255, 255)
        
        # Prepare the initial score image.
        # Display the score at the top right of the screen.
        self.settings.score = 0
        
        self.prep_score(self.settings.hardcore_mode,self.settings.score)

    
    def prep_score(self,mode,score):
        score_str = str(score)
        text_str = ("Score: ")
        display_str = text_str + score_str
        if mode == False:
            self.text_color = (255,0,0)
        else:
            self.text_color = (255, 255, 255)
        self.score_image = self.font.render(display_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)


class Highscore:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.highscore = 0
            
        # Font settings for scoring information. 
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.initial_highscore()


    def new_highscore(self):
        myFile = open("highscore.txt", "w")
        myFile.write(str(self.settings.score))
        myFile.close()


    def initial_highscore(self):
        get_initial_score = False
        while get_initial_score == False:
            try:
                myFile = open("highscore.txt", "r")
                self.highscore = myFile.readline()
                myFile.close()
                get_initial_score = True
            except:
                myFile = open("highscore.txt", "w")
                myFile.write("0")
                myFile.close()


    def show_highscore(self,x):
        myFile = open("highscore.txt", "r")
        self.highscore = myFile.readline()
        myFile.close()
        highscore_str = str(self.highscore)
        text_str = ("Highscore: ")
        display_str = text_str + highscore_str
        if x == False:
            self.text_color = (255,0,0)
        else:
            self.text_color = (255, 255, 255)
        self.score_image = self.font.render(display_str, True,
        self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20
        self.screen.blit(self.score_image, self.score_rect)


    def check_highscore(self):
        myFile = open("highscore.txt", "r")
        self.highscore = myFile.readline()
        myFile.close()
        if self.settings.score > int(self.highscore):
            self.new_highscore()