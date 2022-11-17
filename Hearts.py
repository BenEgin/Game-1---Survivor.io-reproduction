import pygame
from settings import settings


class Heart(pygame.sprite.Sprite):

    def __init__(self, ai_game):
        
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = settings()
        self.hearts = pygame.sprite.Group()
        self.xpos1 = self.screen_rect.width /5 * 3
        self.xpos2 = self.xpos1 + 100
        self.xpos3 = self.xpos2 + 100

        image1 = pygame.image.load('Sprites/Heart.png')
        
        self.image = pygame.transform.scale(image1, (70,70))
        self.rect = self.image.get_rect()

    
    def blitme_hearts(self,lives):
        i = 1
        while i < (lives +1 ):
            new_heart = Heart(self)
            if i == 1:
                new_heart.x = self.xpos1
            elif i == 2:
                new_heart.x = self.xpos2
            elif i == 3:
                new_heart.x =self.xpos3

            new_heart.y = 20 
            new_heart.rect = new_heart.x, new_heart.y
            self.hearts.add(new_heart)
            self.screen.blit(self.image, new_heart.rect)
            i += 1