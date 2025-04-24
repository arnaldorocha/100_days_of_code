from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_speed = MOVE_DISTANCE
    def move(self):
        self.forward(self.move_speed)
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def increase_speed(self):
        self.move_speed += MOVE_DISTANCE
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def reset(self):
        self.goto(STARTING_POSITION)
        self.move_speed = MOVE_DISTANCE
    def set_speed(self, speed):
        self.move_speed = speed
    def get_speed(self):
        return self.move_speed
    def set_position(self, x, y):
        self.goto(x, y)
    def get_position(self):
        return self.xcor(), self.ycor()
    def set_heading(self, heading):
        self.setheading(heading)
    def get_heading(self):
        return self.heading()
    def set_shape(self, shape):
        self.shape(shape)
    def get_shape(self):
        return self.shape()
    def set_penup(self):
        self.penup()
    def set_pendown(self):
        self.pendown()
    def set_color(self, color):
        self.color(color)
    def get_color(self):
        return self.color()
    def set_speed(self, speed):
        self.speed(speed)
