from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Linebot(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(3)
        self.color("white")
        self.speed("fastest")
        self.setpos(0, -405)
        self.setheading(90)
        for i in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
