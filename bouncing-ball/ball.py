import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulation")


ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = 0

gravity = 0.1
while True:

    ball.dy -= gravity
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() < -300:
        ball.dy *= -1
