from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = self.y_move * -1

    def bouncex(self):
        self.x_move = self.x_move * -1
        self.move_speed = self.move_speed * 0.9

    def restart_game(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bouncex()

