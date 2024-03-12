import pygame
import pygame.gfxdraw


def main():
    pygame.init()
    size = (1280, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Spec")
    width = screen.get_width()
    height = screen.get_height()
    smallFont = pygame.font.Font(None, 35)
    twoP = smallFont.render('2 Players', True, (0,0,0))
    threep = smallFont.render('3 Players', True, (0,0,0))
    fourP = smallFont.render('4 Players', True, (0,0,0))
    done = False

    #0 = Player Number Selection
    #1 = Player Name Menu
    #2 = Game Board
    GAME_STATE = 0
    noOfPlayers = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if noOfPlayers == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 511.6 <= mouse[0] <= 792.3 and 248.8 <= mouse[1] <= 311.2:
                        print("2 Players")
                        noOfPlayers = 2
                        GAME_STATE = 1
                    if 511.6 <= mouse[0] <= 792.3 and 368.8 <= mouse[1] <= 431.2:
                        print("3 Players")
                        noOfPlayers = 3
                        GAME_STATE = 1
                    if 511.6 <= mouse[0] <= 792.3 and 489.2 <= mouse[1] <= 551.6:
                        print("4 Players")
                        noOfPlayers = 4
                        GAME_STATE = 1
            

        if noOfPlayers == 0:
            screen.fill((192,192,192))
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (0,128,255), ((511.6,248.8),(280.7,62.4)))
            screen.blit(twoP, (599.4,268.9))
            pygame.draw.rect(screen, (0,128,255), ((511.6,368.8),(280.7,62.4)))
            screen.blit(threep, (599.4,388.9))
            pygame.draw.rect(screen, (0,128,255), ((511.6,489.2),(280.7,62.4)))
            screen.blit(fourP, (599.4,509.3))
            pygame.display.flip()

        if GAME_STATE == 1:
            screen.fill((192,192,192))
            pygame.display.flip()
        

    pygame.quit()

if __name__ == "__main__":
    main()
    