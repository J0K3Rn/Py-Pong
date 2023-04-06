from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from linebot import Linebot
import time

# Declarations
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create game components
scoreboard = Scoreboard()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

# Draw dashed line
linebot = Linebot()

# Add controls
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


def main():
    game_alive = True
    while game_alive:
        time.sleep(ball.move_speed)
        screen.update()

        ball.move()

        # If ball hits top or bottom
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect when right paddle misses
        if ball.xcor() > 400:
            ball.reset_position()
            scoreboard.l_point()

        # Detect when left paddle misses
        if ball.xcor() < -400:
            ball.reset_position()
            scoreboard.r_point()

    screen.exitonclick()


if __name__ == "__main__":
    main()
