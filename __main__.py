import os
import pygame

#def game_file(name):
#    return (
#        name.endswith('.py')
#        and not name.startswith('__')
#        and name != 'utils.py'
#    )

def main():

    #Title Screen
    pygame.init()

    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    backgroundColor = (72, 72, 72)
    textColor = (201, 201, 201)

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    titleFont = pygame.font.Font('freesansbold.ttf', 80)
    titleText = titleFont.render('Arcade Hub', True, textColor)
    titleTextRect = titleText.get_rect()
    titleTextRect.center = (width/2, height/5)

    buttonFont = pygame.font.Font('freesansbold.ttf', 50)
    buttonText = buttonFont.render('Play', True, textColor)
    buttonTextRect = buttonText.get_rect()
    buttonTextRect.center = (width/2, height/2)

    while True:

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if width/2-50 <= mouse[0] <= width/2+50 and height/2-25 <= mouse[1] <= height/2+20: 
                    #Make this go to game screen with a list of all games
                    pygame.quit() 
                  
            
        screen.fill(backgroundColor)
        screen.blit(titleText, titleTextRect)

        if width/2-50 <= mouse[0] <= width/2+50 and height/2-25 <= mouse[1] <= height/2+20: 
            buttonText = buttonFont.render('Play', True, 'black')
            
        else: 
            buttonText = buttonFont.render('Play', True, textColor)

        screen.blit(buttonText, buttonTextRect) 

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()