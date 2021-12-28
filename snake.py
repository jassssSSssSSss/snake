from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
X_COR = 20
#constant is capitalized and its here so that easy to change in the future
#for snakey we are using turtle in the class so its a has a r/s. snakey has turtles. for food its inheriting 
#the turtle class so its an is a r/s. food is a turtle. 


#SOOO IMPT!!! need to rmb the def all need self as parameter and every variable need a self. in front!!!
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snakey()
        self.head = self.segments[0]
        

    def create_snakey(self):
        for _ in range(3):
            self.add_segment()
            # TODO: figure out wtf happening w my snakey starting coord
            X_COR -= 20
            
    def add_segment(self, position):
        snakey = Turtle(shape = "square")
        snakey.color("white")
        snakey.penup()
        snakey.goto(x = X_COR,y = 0)
        self.segments.append(snakey)
    
    def extend(self):
        #TODO: understand whats gg on here 
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x = new_x, y = new_y)
            self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
        


