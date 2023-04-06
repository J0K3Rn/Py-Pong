from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def up(self):
        if self.ycor() < 240:
            self.setposition(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -240:
            self.setposition(self.xcor(), self.ycor() - MOVE_DISTANCE)
