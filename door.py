import pygame
from letter import letter
from monitor import monitor
from Padlock import Padlock
from vent import vent
import window

class door(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("./assets/images/door.png")
        self.arrowImage = pygame.image.load('./assets/images/Arrow.png')
        self.paperSlipImage = pygame.image.load("./assets/images/paper_slip.png")  # Load the paper slip image
        self.paperSlipButton = None 
        self.padlockImg = pygame.image.load("./assets/images/keypad.jpg")
        self.padlockImg = pygame.transform.scale(self.padlockImg, (80, 100))

    def display(self, screen):
        screen.blit(self.backgroundImg, (0, 0))
        

        self.padlockButton = self.padlockImg.get_rect(center=(950, 430))
        screen.blit(self.padlockImg, self.padlockButton.topleft)

        # Left Arrow Button
        self.leftArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 8, screen.get_height() *2 / 4 +10))
        screen.blit(self.arrowImage, self.leftArrowButton.topleft)

        # Right Arrow Button (flipped)
        flipped_arrow_image = pygame.transform.flip(self.arrowImage, True, False)  # Flip the image
        self.rightArrowButton = flipped_arrow_image.get_rect(center=(screen.get_width() * 7 / 8, screen.get_height() *2 / 4 +10))
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
            if self.padlockButton.collidepoint(event.pos):
                return(False, Padlock())


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return((False,letter()))

