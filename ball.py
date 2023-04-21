from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):                      # метод перемещает мяч в направлении его движения по осям x и y
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):             # изменяет направление движения мяча по оси y, умножая атрибут y_move на -1
        self.y_move *= -1

    def bounce_x(self):   #изменяет направление движения мяча по оси x, умножая атрибут x_move на -1 и уменьшая атрибут move_speed на 10%
        self.x_move *= -1
        # self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
