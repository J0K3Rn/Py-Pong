from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.pensize(3)
        self.color("white")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.draw_line()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def draw_line(self):
        self.setpos(0, -405)
        self.setheading(90)
        for i in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
