import pygame
from letter import letter
from monitor import monitor
from vent import vent
import window

class door(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("door.png")
        self.arrowImage = pygame.image.load('Arrow.png')
        self.paperSlipImage = pygame.image.load("paper_slip.png")  # Load the paper slip image
        self.paperSlipButton = None 

    def display(self, screen):
        screen.blit(self.backgroundImg, (0, 0))

        # Left Arrow Button
        self.leftArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 4, screen.get_height() *3/ 4))
        screen.blit(self.arrowImage, self.leftArrowButton.topleft)

        # Right Arrow Button (flipped)
        flipped_arrow_image = pygame.transform.flip(self.arrowImage, True, False)  # Flip the image
        self.rightArrowButton = flipped_arrow_image.get_rect(center=(screen.get_width() * 3 / 4, screen.get_height() *3/ 4))
        screen.blit(flipped_arrow_image, self.rightArrowButton.topleft)

        self.paperSlipButton = self.paperSlipImage.get_rect()
        self.paperSlipButton.midbottom = (screen.get_width() / 2, screen.get_height())
        screen.blit(self.paperSlipImage, self.paperSlipButton.topleft)


    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            
            if self.leftArrowButton.collidepoint(event.pos):
                return(False,vent())
            if self.rightArrowButton.collidepoint(event.pos):
                return(False,monitor())
            
           
            if self.paperSlipButton and self.paperSlipButton.collidepoint(event.pos):
                return(False,letter())
               
                    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return((False,letter()))
        
            
        
        
            
        
        
                