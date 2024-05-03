import pygame

def mainScene():
    #Title Screen
    pygame.init()

    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    backgroundColor = (72, 72, 72)
    textColor = (201, 201, 201)

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    headerFont = pygame.font.Font('freesansbold.ttf', 80)
    headerText = headerFont.render('Games', True, textColor)
    headerTextRect = headerText.get_rect()
    headerTextRect.center = (width/2, height/5)

    while True:

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                  
            
        screen.fill(backgroundColor)
        screen.blit(headerText, headerTextRect)

        pygame.display.flip()
        clock.tick(60)