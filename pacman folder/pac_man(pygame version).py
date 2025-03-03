# Example file showing a basic pygame "game loop"
import pygame
import matplotlib.image as mpimg
import PIL.Image
# pygame setup
pygame.init()
def pacman_game():
    # create a window
    screen = pygame.display.set_mode((747,790))
    clock = pygame.time.Clock()
    running = True
    ghost_direction = 1
    score = 0
    x_index = 1
    y_index = -1
    coll_y = False
    coll_x = False
    game_active = False
    starting = True
    start_screen = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\pacman_end_screen.gif")
    play_button = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\play_game.gif")
    game_background = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\pac_man_background.gif")
    # Load start screen
    if not game_active and starting:
        print("start screen")
        screen.blit(start_screen, (0, 0))
        screen.blit(play_button, (300, 450))
    pygame.display.flip()

    while running:
        # game events go here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #star game buttton it also sets the game to active
                if x > 300 and x < 480 and y > 450 and y < 500 and starting == True:
                    print("here")
                    game_active = True
                    starting = False
                    print("game frame")
                    screen = pygame.display.set_mode((1000,1000))
                    screen.blit(game_background, (0, 0))
                    pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()   # always quit pygame when done!
pacman_game()