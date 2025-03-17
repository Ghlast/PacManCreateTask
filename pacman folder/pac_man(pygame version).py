# Example file showing a basic pygame "game loop"
import pygame
import random as r
import threading
import time as t
# pygame setup
pygame.init()

# Create a function to monitor variables
# Got this from AI, you can now see the status of the variables in the console as the code runs. sweet right?
def monitor():
    while True:
       #print variables here to monitor them. hold the key for the input and then escape to see the results of inputs
        time.sleep(5)  # Adjust the sleep time as needed
# Start the monitoring thread
def  get_direction_of_pac_man():
    if up == True:
        return "up"
    if down == True:
        return "down"
    if left == True:
        return "left"
    if right == True:
        return "right"
threading.Thread(target=monitor, daemon=True).start()
def pacman_game():
    # create a window
    screen = pygame.display.set_mode((747,790))
    clock = pygame.time.Clock()
    running = True
    ghost_direction = 1
    score = 0
    x_index = 1
    y_index = -1
    game_active = False
    starting = True
    try:
        start_screen = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\pacman_end_screen.gif")
    except:
        start_screen = pygame.image.load(r"C:\Users\toasa\OneDrive\Documents\GitHub\PacManCreateTask\pacman folder\pacman_end_screen.gif")
    try:
        play_button = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\play_game.gif")
    except FileNotFoundError:
        play_button = pygame.image.load(r"C:\Users\toasa\OneDrive\Documents\GitHub\PacManCreateTask\pacman folder\play_game.gif")
    try:
        game_background = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\pac_man_background.gif")
    except FileNotFoundError:
        game_background = pygame.image.load(r"C:\Users\toasa\OneDrive\Documents\GitHub\PacManCreateTask\pacman folder\pac_man_background.gif")
    try:
        pacman = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\pac_man.gif")
    except FileNotFoundError:
        pacman = pygame.image.load(r"C:\Users\toasa\OneDrive\Documents\GitHub\PacManCreateTask\pacman folder\pac_man.gif")
    try:
        ghost = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\pacman ghost.gif")
    except FileNotFoundError:
        ghost = pygame.image.load(r"C:\Users\toasa\OneDrive\Documents\GitHub\PacManCreateTask\pacman folder\pacman ghost.gif")
    try:
        death_screen = pygame.image.load(r"H:\My Drive\10 nth grade\Computer science\git hub folder\projects and packages!\Pacman Horror\Ryan-and-Toa-Create-Task-\PacManCreateTask\pacman folder\pacman_start_screen.gif")
    except FileNotFoundError:
        death_screen = pygame.image
    except FileNotFoundError:
        death_screen = pygame.image.load(r"C:\Users\toasa\OneDrive\Documents\GitHub\PacManCreateTask\pacman folder\pacman_start_screen.gif")

    horizontal_wall= pygame.image.load(r"pacman folder\horizontal_wall.gif")
    class pellet:
        def __init__(self,image, x , y, eaten= False):
            normal_x = x+300 
            normal_y = y+250
            self.x = normal_x
            self.y =normal_y
            self.eaten = eaten
            self.image = image
            self.position = self.image.get_rect().move(normal_x , normal_y)
        def eaten_state(self):
                self.eaten = True
        pass
    pellet_list = [0,1,2,3,4]
    for pellet_num in pellet_list:
        pellet_list[pellet_num] = pellet(pygame.image.load(r"pacman folder\Pellet.gif"), pellet_num*100, 300)
    pellet_rectangles = [0,1,2,3,4]
    x = 0
    for pellet in pellet_list:
        pellet_rectangles[x] = pellet.position
        x += 1

        
    class wall:
        def __init__(self, image, x, y):
            normal_x = x+450 
            normal_y = y+400
            self.x = normal_x
            self.y = normal_y
            self.image = image
            self.position = self.image.get_rect().move(self.x,self.y)
        def detect_collision(self):
                if self.position.colliderect(pac_man_rectangle):
                    if get_direction_of_pac_man() == "right":
                        pac_man_pos.x -= 10
                    if get_direction_of_pac_man() == "left":
                        pac_man_pos.x += 10
                    if get_direction_of_pac_man() == "up":
                        pac_man_pos.y += 10
                    if get_direction_of_pac_man() == "down":
                        pac_man_pos.y -= 10
    wall_list = [0, 1, 2, 3, 4]
    for wall_num in range(0, 5):
        wall_list[wall_num] = wall(pygame.image.load(r"pacman folder\horizontal_wall.gif"), 200, wall_num*100)
        


    pac_man_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    ghost_pos = pygame.Vector2(500, 500)

    dt = 0
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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            keys = pygame.key.get_pressed()
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
                    screen.blit(pacman,pac_man_pos)
                    pygame.display.flip()
        def ghost_rand():
            g_up = False
            g_down = False
            g_left = False
            g_right = False
            ghost_count = 0
            ghost_d = 1
            ghost_direction = r.randint(1, 4)
            if (ghost_count % 3 == 1):
                ghost_direction = ghost_d
            if ghost_direction == 1:
                g_up = True
                g_left = False
                g_right = False
            if ghost_direction == 2:
                g_down = True
                g_left = False
                g_right = False
            if ghost_direction == 3:
                g_left = True
                g_up = False
                g_down = False
            if ghost_direction == 4:
                g_right = True
                g_up = False
                g_down = False               
            if g_down == True:
                ghost_pos.y += 450 * dt
                pygame.display.flip()
            if g_up == True:
                ghost_pos.y -= 450 * dt
                pygame.display.flip()
            if g_left == True:
                ghost_pos.x -= 450 * dt
                pygame.display.flip()
            if g_right == True:
                ghost_pos.x += 450 * dt
                pygame.display.flip()               
            t.sleep(0.01)
            ghost_d = ghost_direction
            ghost_count += 1
            print(ghost_d, ghost_count)
            

        def ghost_movement():
           if ghost_pos.x >= 30 and ghost_pos.x <= 950 and ghost_pos.y >= 30 and ghost_pos.y <= 750:
                def monitor():
                    while True:
                        #print variables here to monitor them. hold the key for the input and then escape to see the results of inputs
                        t.sleep(5)  # Adjust the sleep time as needed
                threading.Thread(target=monitor, daemon=True).start()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    ghost_rand()
                if keys[pygame.K_s]:
                    ghost_rand()
                if keys[pygame.K_a]:
                    ghost_rand()
                if keys[pygame.K_d]:
                    ghost_rand()

        def pac_man_movement():
            global up 
            global down 
            global left 
            global right 
            up = False
            down = False
            left = False
            right = False
            if pac_man_pos.x >= 30 and pac_man_pos.x <= 950 and pac_man_pos.y >= 30 and pac_man_pos.y <= 750:
                def monitor():
                    while True:
                        #print variables here to monitor them. hold the key for the input and then escape to see the results of inputs
                        t.sleep(5)  # Adjust the sleep time as needed
                threading.Thread(target=monitor, daemon=True).start()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    up = True
                    left = False
                    right = False
                if keys[pygame.K_s]:
                    down = True
                    left = False
                    right = False
                if keys[pygame.K_a]:
                    left = True
                    up = False
                    down = False
                if keys[pygame.K_d]:
                    right = True
                    up = False
                    down = False
                
            elif pac_man_pos.x <= 30:
                pac_man_pos.x = 941
                pygame.display.flip()
            elif pac_man_pos.x >= 950:
                pac_man_pos.x = 31
                pygame.display.flip()
            elif pac_man_pos.y <= 30:
                pac_man_pos.y = 740
                pygame.display.flip()
            elif pac_man_pos.y >= 750:
                pac_man_pos.y = 33
                pygame.display.flip()
            else:
                print("error, we should not be here")


            if down == True:
                pac_man_pos.y += 300 * dt
                pygame.display.flip()
            if up == True:
                pac_man_pos.y -= 300 * dt
                pygame.display.flip()
            if left == True:
                pac_man_pos.x -= 300 * dt
                pygame.display.flip()
            if right == True:
                pac_man_pos.x += 300 * dt
                pygame.display.flip()  
                
        if game_active:
            def monitor():
                while True:
                    #print variables here to monitor them. hold the key for the input and then escape to see the results of inputs
                    t.sleep(5)  # Adjust the sleep time as needed
            threading.Thread(target=monitor, daemon=True).start()
            pac_man_movement()    
            ghost_movement()
            screen.blit(game_background, (0, 0))
            screen.blit(pacman,pac_man_pos)
            screen.blit(ghost, ghost_pos)

            pac_man_rectangle = pacman.get_rect(topleft = (pac_man_pos.x, pac_man_pos.y))
            for wall in wall_list:
                screen.blit(wall.image, (wall.x, wall.y))
                wall.detect_collision()

            for pellet in pellet_list:
                screen.blit(pellet.image, (pellet.x, pellet.y))


            pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
        dt = clock.tick(60) / 1000  # delta time in seconds (no idea what this does)
    pygame.quit()   # always quit pygame when done!
pacman_game()