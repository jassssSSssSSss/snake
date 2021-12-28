from turtle import Turtle
import random
#why not js create a new object food that belongs to Turtle class?
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randrange(-280, 280, 20)
        rand_y = random.randrange(-280, 280, 20)
        self.goto(x = rand_x, y = rand_y)



