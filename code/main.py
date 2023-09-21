import pygame
#https://www.pygame.org/docs/


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
#Code taken from PyGame documentations


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) #FPS-limit 60


pygame.quit()