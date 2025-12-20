import turtle
import winsound

game_started = False


#  SCREEN 
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  
screen.bgpic("tabletennis.gif")
player1 = screen.textinput("Player 1", "Enter Left Player Name:")
player2 = screen.textinput("Player 2", "Enter Right Player Name:")
if not player1:
    player1 = "Player 1"
if not player2:
    player2 = "Player 2"

#  LEFT PADDLE 
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)  
left_paddle.penup()
left_paddle.goto(-350, 0)

#  RIGHT PADDLE
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# BALL 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

#  SCORE
WINNING_SCORE = 2

score_left = 0
score_right = 0

game_over = False

#SCORE POSITION
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("0    0", align="center", font=("Courier", 24, "normal"))

#  PLAYER NAMES 
player_names = turtle.Turtle()
player_names.speed(0)
player_names.color("white")
player_names.penup()
player_names.hideturtle()
player_names.goto(0, 230)
player_names.write(f"{player1}         {player2}",
                   align="center", font=("Courier", 20, "normal"))


start_text = turtle.Turtle()
start_text.speed(0)
start_text.color("white")
start_text.penup()
start_text.hideturtle()
start_text.goto(0, 0)
start_text.write("WELCOME TO PING PONG\nPress SPACE to Start",
                 align="center", font=("Courier", 28, "bold"))


#  FUNCTIONS 

def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:      
        y += 40
        left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -250:     
        y -= 40
        left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 40
        right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -250:
        y -= 40
        right_paddle.sety(y)

def start_game():
    global game_started
    game_started = True
    start_text.clear()

def play_win_sound():
    winsound.PlaySound("champion 1.wav", winsound.SND_ASYNC)

#keys
screen.listen()
screen.onkeypress(left_paddle_up, "w")
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")
screen.onkeypress(start_game, "space")

import random

def confetti():
    pieces = []

    
    for i in range(80):
        c = turtle.Turtle()
        c.speed(0)
        c.penup()
        c.shape("circle")
        c.shapesize(0.3, 0.3)  # tiny confetti size
        c.color(random.choice(["red", "yellow", "pink", "blue", "green", "purple", "orange"]))
        c.goto(random.randint(-380, 380), random.randint(150, 300))
        c.dy = random.uniform(-0.3, -1)   
        pieces.append(c)

    
    for _ in range(250):  
        for p in pieces:
            p.sety(p.ycor() + p.dy)

            
            if p.ycor() < -280:
                p.goto(random.randint(-380, 380), random.randint(200, 300))

        screen.update()


        screen.update()

#GAME LOOP
while True:
    screen.update()

    if not game_started or game_over:
        continue

    # Movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # bounce on top area
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bounce bottom area
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right wall = left player scores
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        score_display.clear()
        score_display.write(f"{score_left}    {score_right}",
                            align="center", font=("Courier", 24, "normal"))

        if score_left == WINNING_SCORE:
             ball.dx = 0
             ball.dy = 0
             game_over = True
             score_display.clear()
             score_display.write(f"{player1} Wins!", align="center", font=("Courier", 30, "bold"))
             play_win_sound()
             confetti()

    # Left wall = right player scores
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        score_display.clear()
        score_display.write(f"{score_left}    {score_right}",
                            align="center", font=("Courier", 24, "normal"))

        if score_right == WINNING_SCORE:
         ball.dx = 0
         ball.dy = 0
         game_over = True
         score_display.clear()
         score_display.write(f"{player2} Wins!", align="center", font=("Courier", 30, "bold"))
         play_win_sound()
         confetti()

 # Ball collision with right paddle
    if (340 < ball.xcor() < 350) and \
        (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1    

    # Ball collision with left paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
       (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1 
