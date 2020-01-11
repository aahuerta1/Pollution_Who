import pygame

#Initialize the pygame
pygame.init()

#Create the screen
scree = pygame.display.set_mode((1500, 800))

#Tittle and Icon
pygame.display.set_caption("Pollution Who")
icon = pygame.image.load('biohazard.png')
pygame.display.set_icon(icon)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB - Red, Green, Blue


