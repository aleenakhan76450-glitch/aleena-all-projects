import turtle 
import os
def play_music():
    os.system("afplay bgmusic.mp3 &") 
def stop_music():
    os.system("killall afplay")
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)
play_music()

wn.bgpic("bg.gif")

#score
score_a = 0
score_b= 0 

#paddle a 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#ball
wn.register_shape("craig.gif")
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("craig.gif")
ball1.penup()
ball1.goto(0,0)
ball1.dx = 4
ball1.dy = -4

#ball2
wn.register_shape("tweek.gif")
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("tweek.gif")
ball2.penup()
ball2.goto(0,0)
ball2.dx = -4
ball2.dy = -4

#ball3
wn.register_shape("kenny.gif")
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("kenny.gif")
ball3.penup()
ball3.goto(0,0)
ball3.dx = 4
ball3.dy = 4


balls = [ball1, ball2, ball3] 

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal") )


#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#function
def paddle_a_up():
    y= paddle_a.ycor()
    y += 35
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y -= 35
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    for ball in balls:

       

        #move ball
        ball.setx(ball.xcor()+ ball.dx)
        ball.sety(ball.ycor()+ ball.dy)

        #music
        play_music
        os.system("afplay main sound.mp3&")



        #border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy*=-1
            os.system("afplay collide.mp3&")
        
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy*=-1
            os.system("afplay collide.mp3&")

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
            os.system("afplay score1.mp3&")
            if score_a == 10 or score_b == 10:
                 pen.goto(0,0)
                 pen.write("Game Over, You killed kenny!", align="center", font=("courier", 35, "bold"))
                 stop_music
                 break

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("courier", 24, "normal") )
            os.system("afplay score2.mp3&")
            if score_a == 10 or score_b == 10:
                 pen.goto(0,0)
                 pen.write("Game Over, You killed kenny!", align="center", font=("courier", 35, "bold"))
                 stop_music
                 break
            

        #paddle and ball collision
        if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50 ):
            ball.setx(340)
            ball.dx *= -1
            os.system("afplay 18789.mp3&")


        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50 ):
            ball.setx(-340)
            ball.dx *= -1
            os.system("afplay 18789.mp3&")

            
            

     
    
    
    #ai
    #closest_ball = balls[0] 
    #for ball in balls:
        #if ball.xcor() >  closest_ball.xcor:
            #closest_ball=ball 

        if ball.xcor() > ball2.xcor():
            if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 20:
             paddle_b_up()

        elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 20:
             paddle_b_down()
    else:
         if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 20:
             paddle_b_up()

         elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 20:
             paddle_b_down()
    if score_a == 10 or score_b == 10:
                pen.goto(0,0)
                pen.write("Game Over, You killed kenny!", align="center", font=("courier", 35, "bold"))
                break

   

   
    
        