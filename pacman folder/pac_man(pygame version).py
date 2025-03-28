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
        t.sleep(5)  # Adjust the sleep time as needed
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
    
choice_num = 0
threading.Thread(target=monitor, daemon=True).start()
outer_left_wall_y = -430
outer_right_wall_y = 470
outer_top_wall_x = -430
outer_bottom_wall_x = 300
def pacman_game():
    # create a window
    screen = pygame.display.set_mode((747,790))
    clock = pygame.time.Clock()
    running = True
    ghost_direction = 1
    score = 0
    x_index = 1
    y_index = -1
    global game_active
    global starting
    game_active = False
    starting = True
    start_screen = pygame.image.load(r"pacman folder\pacman_end_screen.gif")
    play_button = pygame.image.load(r"pacman folder\play_game.gif")
    game_background = pygame.image.load(r"pacman folder\pac_man_background.gif")
    pacman = pygame.image.load(r"pacman folder\pac_man.gif")
    ghost = pygame.image.load(r"pacman folder\pacman ghost.gif")
    death_screen = pygame.image.load(r"pacman folder\pacman_start_screen.gif")
    horizontal_wall= pygame.image.load(r"pacman folder\horizontal_wall.gif")
    vertical_wall = pygame.image.load(r"pacman folder\pac_man_vertical_wall.gif")
    class pellet:
        def __init__(self,image, x , y, eaten= False):
            normal_x = x+300 
            normal_y = y+250
            self.x = normal_x
            self.y =normal_y
            self.eaten = eaten
            self.image = image
            self.position = self.image.get_rect().move(normal_x , normal_y)
        def detect_collision(self):
            if self.position.colliderect(pac_man_rectangle):
                self.eaten = True
        def reset(self):
            self.eaten = False
        pass
    pellet_list = [0,1,2,3,4]
    for pellet_num in pellet_list:
        pellet_list[pellet_num] = pellet(pygame.image.load(r"pacman folder\Pellet.gif"), pellet_num*100, 300)
    x = 0
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
    wall_list = [0,1,2,3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]

    y = 0
    for wall_num in range(49):
        if y >= 2:
            y = 0
        if wall_num < 2:
            wall_list[wall_num] = wall(horizontal_wall, outer_left_wall_y ,y*40-50)
        if 2<= wall_num <4:
            wall_list[wall_num] = wall(horizontal_wall, outer_right_wall_y,y*40-50)
        if 4<= wall_num <6:
            wall_list[wall_num] = wall(vertical_wall, y*40-50, outer_top_wall_x)
        if 6<= wall_num <8:
            wall_list[wall_num] = wall(vertical_wall, y*40-50, outer_bottom_wall_x)
        if 8<= wall_num <10:
            wall_list[wall_num] = wall(horizontal_wall, y*40-50, outer_top_wall_x)
        y += 1


    pac_man_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    ghost_pos = pygame.Vector2(500, 500)

    dt = 0
    # Load start screen

   

    while running:
        if starting:
            score = 0
        if not game_active and starting:
            screen = pygame.display.set_mode((747,1000))
            screen.blit(start_screen, (0, 0))
            screen.blit(play_button, (300, 450))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > 300 and x < 480 and y > 450 and y < 500 and starting == True:
                        print("here")
                        game_active = True
                        starting = False
                        score = 0
                        print("game frame")
                        pac_man_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                        ghost_pos = pygame.Vector2(500, 500)
                        screen = pygame.display.set_mode((1000,1000))
                        screen.blit(game_background, (0, 0))
                        screen.blit(pacman,pac_man_pos)
                        pygame.display.flip()
        # game events go here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            keys = pygame.key.get_pressed()
        def ghost_teleport():
            ghost_t = r.randint(1, 4)
            if ghost_t == 1:
                ghost_pos.x = pac_man_pos.x + 100
                ghost_pos.y = pac_man_pos.y
            if ghost_t == 2:
                ghost_pos.x = pac_man_pos.x - 100
                ghost_pos.y = pac_man_pos.y
            if ghost_t == 3:
                ghost_pos.x = pac_man_pos.x
                ghost_pos.y = pac_man_pos.y + 100
            if ghost_t == 4:
                ghost_pos.x = pac_man_pos.x
                ghost_pos.y = pac_man_pos.y - 100

        def ghost_rand():
            g_up = False
            g_down = False
            g_left = False
            g_right = False
            ghost_speed = 300 
            ghost_direction = r.randint(1, 5)
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
            if ghost_direction == 5:
                ghost_teleport()              
            # Ghost_speed matches pacman's speed and is then multiplied by how many the modulus that can be found in the ghost_choice function
            # It's multipled by the modulus to make the ghost feel fast enough
            if g_down == True:
                ghost_pos.y += (ghost_speed * 3) * dt
                pygame.display.flip()
            if g_up == True:
                ghost_pos.y -= (ghost_speed * 3) * dt
                pygame.display.flip()
            if g_left == True:
                ghost_pos.x -= (ghost_speed * 3) * dt
                pygame.display.flip()
            if g_right == True:
                ghost_pos.x += (ghost_speed * 3) * dt

                pygame.display.flip()
        def ghost_choice(): 
            # To make the ghost less jittery it only executes it's movement after pacman has moved x amount of times.
            # Currently the choice_num % 3 == 0 makes it happen after pacman has moved three times. 
            global choice_num
            if choice_num % 3 == 0:
                ghost_rand()
            choice_num += 1
            # This if statement caps choice_num to be 300 so that it doesn't grow too big and become an issue later
            if choice_num == 300:
                choice_num = 0

        def ghost_movement():
            if ghost_pos.x >= 30 and ghost_pos.x <= 950 and ghost_pos.y >= 30 and ghost_pos.y <= 750:
                def monitor():
                    while True:
                        #print variables here to monitor them. hold the key for the input and then escape to see the results of inputs
                        t.sleep(5)  # Adjust the sleep time as needed
                threading.Thread(target=monitor, daemon=True).start()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    ghost_choice()
                if keys[pygame.K_s]:
                    ghost_choice()
                if keys[pygame.K_a]:
                    ghost_choice()
                if keys[pygame.K_d]:
                    ghost_choice()
            
            elif ghost_pos.x <= 30:
                ghost_pos.x = 941
                pygame.display.flip()
            elif ghost_pos.x >= 950:
                ghost_pos.x = 31
                pygame.display.flip()
            elif ghost_pos.y <= 30:
                ghost_pos.y = 740
                pygame.display.flip()
            elif ghost_pos.y >= 750:
                ghost_pos.y = 33
                pygame.display.flip()
            else:
                print("error, we should not be here")

        def pac_man_movement():
            global up 
            global down 
            global left 
            global right
            global score
            score = 0
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

            # speed_mod is just a variable that adjusts the speed of pacman. Should be kept between 0 and 1. 
            # pacman currently moves at 80% of the base speed of 300
            speed_mod = 0.80
            if down == True:
                pac_man_pos.y += (300*speed_mod) * dt
                pygame.display.flip()
            if up == True:
                pac_man_pos.y -= (300*speed_mod) * dt
                pygame.display.flip()
            if left == True:
                pac_man_pos.x -= (300*speed_mod) * dt
                pygame.display.flip()
            if right == True:
                pac_man_pos.x += (300*speed_mod) * dt
                pygame.display.flip()  
                
        if game_active:
            def monitor():
                while True:
                    #print variables here to monitor them. hold the key for the input and then escape to see the results of inputs
                    print(wall_list[2].x, wall_list[2].y)
                    t.sleep(5)  # Adjust the sleep time as needed
            threading.Thread(target=monitor, daemon=True).start()
            pac_man_movement()    
            ghost_movement()
            screen.blit(game_background, (0, 0))
            screen.blit(pacman,pac_man_pos)
            screen.blit(ghost, ghost_pos)

            pac_man_rectangle = pacman.get_rect(topleft = (pac_man_pos.x, pac_man_pos.y))
            for wall in wall_list:
                try:
                    screen.blit(wall.image, (wall.x, wall.y))
                except AttributeError:
                    continue
                wall.detect_collision()

            # Update the score based on the number of eaten pellets
            score = 0
            for pellet in pellet_list:
                pellet.detect_collision()
                if not pellet.eaten:
                    screen.blit(pellet.image, (pellet.x, pellet.y))
                if pellet.eaten:
                    score += 1

            pygame.display.flip()
            if score == 5:
                screen = pygame.display.set_mode((1000,624))
                screen.blit(death_screen, (0, 0))
                pygame.display.flip()
                for events in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        running = False
                    if keys[pygame.K_SPACE]:
                        for pellet in pellet_list:
                            pellet.reset()
                        starting = True
                        game_active = False 

            pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
        dt = clock.tick(60) / 1000  # delta time in seconds (no idea what this does)
    pygame.quit()   # always quit pygame when done!
pacman_game()