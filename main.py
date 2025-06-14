# I have cloned this repository from github
# I have added this comment
# Now ill push these changes to git and check on Tuf to see whether the changes reflect there too.

import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER!", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)


screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock() # clock object to control the frame rate.

game = Game()

GAME_UPDATE = pygame.USEREVENT # used to generate custom events
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.reset()
                game.game_over = False
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()     
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()   
                game.update_score(0, 1)               
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
   
    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))       # display score in game loop
    screen.blit(next_surface, (375, 180, 50, 50))       # display next (upcoming block) in game loop
    
    if game.game_over == True: 
        screen.blit(game_over_surface, (320, 450, 50, 50))  # display gameover text 
    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 20)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery)) # score values are dynamic 
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 20)                                                          # and doesnt have fixed

    game.draw(screen)

    pygame.display.update()
    clock.tick(60) # while loop will run 60 times a second


  