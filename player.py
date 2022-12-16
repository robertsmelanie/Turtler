from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle): 
    # Inheritance allows us to define a class that inherits all the methods and properties (attributes) from another class referred to as inheritance or class inheritance (inheritance allows us to define a class and pass in inheritances of another class)
    # Passing in the Turtle class here lets our Player class have all the same attributes and methods as the Turtle Class
    def __init__(self):
        # The super function returns a temporary object of the superclass that allows access to all of its methods to its child class.
        # Need not remember or specify the parent class name to access its methods. This function can be used both in single and multiple inheritances
        #Passing in the Class sets it up, this super function allows it to work.
        super().__init__()
        self.penup()
        # Now we can access everything we need to from the turtle class
        self.shape("turtle")
        self.color("black")
        self.right(270)
        self.goto(STARTING_POSITION)
        

    # Allow for forward movement
    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    #Reset the turtle
    def reset_turtle(self):
        self.goto(STARTING_POSITION)
        

    # Marks the finish line and return a Boolean value
    def crossed_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
