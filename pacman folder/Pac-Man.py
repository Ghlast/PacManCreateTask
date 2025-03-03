import turtle as pac_man #Pac Man turtle
import turtle as pellets #Pellets turtle
import turtle as wall #Walls turtle
import turtle as ghost #Ghost turtle
import turtle as button  #Buttons
import keyboard #used in the movement functions, WASD
import time #used to smooth out movement
import random #used for randomization in generation
import math #used for ghost movement 
import pygame
import matplotlib.image as mpimg
#Screen Setup

wn = pac_man.Screen()
pac_man = pac_man.Turtle()
ghost = ghost.Turtle()
button = button.Turtle()
ghost_direction = 1
score = 0
x_index = 1
y_index = -1
coll_y = False
coll_x = False
game_active = False
def start():
    start_screen= "pacman_end_screen.gif"
    wn.register_shape(start_screen)
    wn.bgpic(start_screen)
    wn.setup(747, 1000)
    play_game = "play_game.gif"
    wn.register_shape(play_game)
    button.shape(play_game)
    button.showturtle()  
    print(button.isvisible())  
start()
def button_action(x,y):
    if  button.xcor()-(177/2) <= x <= button.xcor()+(177/2) and button.ycor()-(49/2)<= y <= button.ycor()+(49/2):
        wn.tracer(False)
        button.goto(-1000, -1000)
        wn.update()
        wn.tracer(True)
        pacman_game()
wn.onscreenclick(button_action)
def pacman_game():
    global pac_man
    global ghost
    global game_active
    #Game Parameters
    step_size = 10
    time_delay = 0.1
    game_active = True
    pellet_x_cor= random.randint(-10, 10)
    pellet_y_cor = random.randint(-10, 10)
    pellet_size = 0.5
    pelletNum = 10


    #Setup Variables
    pellets_list = []
    pellet_x_cor_list= []
    pellet_y_cor_list = []
    wall_xcor_list = []
    wall_ycor_list = []
    pellet_color = "White"
    pellet_shape = "circle"

    #Pac Man variables
    pac_man.penup()
    pac_man_image = "pac_man.gif"
    wn.register_shape(pac_man_image)
    pac_man.shape(pac_man_image)
    wn.bgpic("pac_man_background.gif")
    wn.setup(1000,1000)

    #Ghost Variables
    ghost.penup()
    ghost_image = "pacman ghost.gif"
    wn.register_shape(ghost_image)
    ghost.shape(ghost_image)
    ghost_speed = step_size*1
    ghost_int_x = random.randint(-10, 10)
    ghost_int_y = random.randint(-10, 10)
    wn.tracer(False)
    ghost.goto(ghost_int_x*step_size, ghost_int_y*step_size)
    wn.update()
    wn.tracer(True)
    global diff
    diff = 10

    #Ghost Movement
    def ghost_rand_movement():
        global ghost_direction
        ghost_direction = random.randint(1, 8)
        if ghost_direction == 1:
            ghost.setheading(0)
            ghost.forward(ghost_speed)
        if ghost_direction == 2:
            ghost.setheading(45)
            ghost.forward(ghost_speed*math.sqrt(2))
            ghost_round_move()
        if ghost_direction == 3:
            ghost.setheading(90)
            ghost.forward(ghost_speed)
        if ghost_direction == 4:
            ghost.setheading(135)
            ghost.forward(ghost_speed*math.sqrt(2))
        if ghost_direction == 5:
            ghost.setheading(180)
            ghost.forward(ghost_speed)
        if ghost_direction == 6:
            ghost.setheading(225)
            ghost.forward(ghost_speed*math.sqrt(2))
        if ghost_direction == 7:
            ghost.setheading(270)
            ghost.forward(ghost_speed)
        if ghost_direction == 8:
            ghost.setheading(315)
            ghost.forward(ghost_speed*math.sqrt(2))

    def ghost_round_move():
        ghost.goto(round(ghost.xcor()), round(ghost.ycor()))
        #print(ghost.xcor(), ghost.ycor())

    def ghost_teleport():
        ghost_direction = random.randint(1, 8)
        print(ghost_direction)
        if ghost_direction == 1 or 2:
            ghost.goto(pac_man.xcor(), pac_man.ycor()-step_size*2)
        if ghost_direction == 3 or 4:
            ghost.goto(pac_man.xcor(), pac_man.ycor()+step_size*2)
        if ghost_direction == 5 or 6:
            ghost.goto(pac_man.xcor()+step_size*2, pac_man.ycor())
        if ghost_direction == 7 or 8:
            ghost.goto(pac_man.xcor()-step_size*2, pac_man.ycor())

    def ghost_decision():
        tele_or_move = random.randint(0, diff)
        if tele_or_move == diff:
            wn.tracer(False)
            ghost_teleport()
            ghost_round_move()
            wn.update()
            wn.tracer(True)
        else:
            ghost_rand_movement()
            ghost_round_move()

    # Game Ovet State
    def dead():
        global game_active
        #print(pac_man.xcor()-ghost.xcor(), pac_man.ycor()-ghost.ycor())
        if abs(pac_man.xcor() - ghost.xcor()) <= step_size and abs(pac_man.ycor() - ghost.ycor()) <= step_size:
            for pellet in pellets_list:
                pellet_hide = 0
                pellet.hideturtle()
                pellet_hide += 1
            pac_man.hideturtle()
            ghost.hideturtle()
            wall.resetscreen()
            button.speed(0)
            wn.tracer(False)
            button.goto(-1000, -1000)
            wn.update()
            wn.tracer(True)
            pacman_end_screen = "pacman_start_screen.gif"
            wn.register_shape(pacman_end_screen)
            wn.bgpic(pacman_end_screen)
            wn.setup(1000,624)


    #Y collision check for pellets
    def y_coll():
        global coll_x
        if pac_man.ycor() in pellet_y_cor_list:
            #print("y detected")
            coll_x = True
        else: 
            coll_x = False

    #X collision check for pellets
    def x_coll():
        global coll_y
        if pac_man.xcor() in pellet_x_cor_list:
            #print("x detected")
            coll_y = True
        else: 
            coll_y = False

    #Ensures that Pac_Man has integer coordinates
    def move_round():
        pac_man.goto(round(pac_man.xcor()), round(pac_man.ycor()))

    # Movement Functions
    def up():
        pac_man.setheading(90)
        pac_man.forward(step_size)
        move_round()
        #print("up")
        x_coll()
        y_coll()
        collision()
        wall_detection()
        time.sleep(time_delay)
        ghost_decision()
        dead()


    def down():
        pac_man.setheading(270)
        pac_man.forward(step_size)
        move_round()
        #print("down")
        x_coll()
        y_coll()
        collision()
        wall_detection()
        time.sleep(time_delay)
        ghost_decision()
        dead()

    def left():
        pac_man.setheading(180)
        pac_man.forward(step_size)
        move_round()
        #print("left")
        x_coll()
        y_coll()
        collision()
        wall_detection()
        time.sleep(time_delay)
        ghost_decision()
        dead()

    def right():
        pac_man.setheading(0)
        pac_man.forward(step_size)
        move_round()
        #print("right")
        x_coll()
        y_coll()
        collision()
        wall_detection()
        time.sleep(time_delay)
        ghost_decision()
        dead()

    # Pellet and Wall generation
    wn.tracer(False)

    #Pellet generation
    for _ in range(pelletNum):
        pellet = pellets.Turtle()
        pellet.shape(pellet_shape)
        pellet.shapesize(pellet_size)
        pellet.color(pellet_color)
        pellets_list.append(pellet)
        pellet.penup()
        #Pellet coordinate determination
        pellet_x_cor += random.randint(-10, 10)
        pellet_y_cor += random.randint(-10, 10)

        #Pellet coordinate redundancy
        while pellet_x_cor*step_size in  pellet_x_cor_list:
         pellet_x_cor += random.randint(-10,10)
        
        pellet_x_cor_list.append(pellet_x_cor* step_size)

        while pellet_y_cor*step_size  in pellet_y_cor_list  :
         pellet_y_cor += random.randint(-10, 10)

        #Refining pellet generation. This portion does not work at the current moment. Idea was to ensure pellets are more spread out when generated so they're not as clustered. 
        '''
        for xCor in pellet_x_cor_list:
            while xCor + step_size > pellet_x_cor :
                pellet_x_cor += random.randint(-10,10)
            while xCor - step_size < pellet_x_cor:
                pellet_x_cor += random.randint(-10,10)

        for yCor in pellet_y_cor_list:
            while yCor + step_size > pellet_y_cor :
                pellet_y_cor += random.randint(-10,10)
            while yCor - step_size < pellet_y_cor:
                pellet_y_cor += random.randint(-10,10)'''


        
        pellet_y_cor_list.append(pellet_y_cor* step_size)
        pellet.speed(0)

        #Pellet placement 
        pellet.goto(pellet_x_cor*step_size,pellet_y_cor*step_size)

        #Wall Direction Randomization
        wall_up_or_down = random.randint(1, 2)
        if wall_up_or_down == 1:
            wall_direction = -1

        if wall_up_or_down == 2:
            wall_direction = 1

        #Wall coordinate determination
        wall_y = (pellet_y_cor*step_size) + (wall_direction*step_size)
        wall_x = (pellet_x_cor*step_size) - (step_size)

        #Wall creation
        walls = wall.Turtle()
        walls.hideturtle()
        walls.penup()
        walls.pencolor(pellet_color)
        walls.goto(wall_x, wall_y)
        walls.pendown()
        walls.speed(0)
        walls.forward(2*step_size)
        wn.update()
        wall_xcor_list.append(wall_x)
        wall_ycor_list.append(wall_y)

    wn.update()
    wn.tracer(True)

    #Wall Collision Detection
    def wall_detection ():
     for wallyCor , wallxCor in zip(wall_ycor_list, wall_xcor_list) :
        if pac_man.xcor() <= wallxCor+20 and pac_man.xcor() >= wallxCor and pac_man.ycor() == wallyCor:
            #print("there is a wall?")
            pac_man.backward(10)

            

    #Collision function for pellets that also increments score 
    def collision():
        global x_index
        global y_index
        global score
        #print(coll_x, coll_y)
        if coll_y == True and coll_x == True:
            y_index = pellet_y_cor_list.index(pac_man.ycor())
            x_index = pellet_x_cor_list.index(pac_man.xcor())
        else:
            y_index = -1
            x_index = 1

        if x_index == y_index:
            print(coll_x, coll_y)
            print("collision", x_index, y_index)
            pellet_x_cor_list.pop(x_index)
            pellet_y_cor_list.pop(y_index)
            pellets_list[x_index].hideturtle()
            pellets_list.pop(x_index)
            score += 1
            print("your score is ", score)

    #Actual Game loop
    while (game_active == True):

        if keyboard.is_pressed("w"):
            up()

        if keyboard.is_pressed("s"):
            down()
    
        if keyboard.is_pressed("a"):
            left()


        if keyboard.is_pressed("d"):
            right()

        #How to end game early
        if keyboard.is_pressed("escape"):
            game_active = False
            print("you exited the game.")
            exit()

        if keyboard.is_pressed("space"):
            for pellet in pellets_list:
                pellet_hide = 0
                pellet.hideturtle()
                pellet_hide += 1
            pac_man.hideturtle()
            ghost.hideturtle()
            wall.resetscreen()              
            start()
            button.goto(0 ,0)
            wn.onscreenclick(button_action)      

        #Win condition for game
        if score == pelletNum:
            game_active = False
            print("You Win!")
            exit()

        wn.update()
    

wn.mainloop()