from turtle import Turtle
import random

# Set some global variables
# Our car color list
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    # Our starting attributes
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    # Creating our cars
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            # Set the shape and size of the crs
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # change the color of the car to a random choice from our COLORS list
            new_car.color(random.choice(COLORS))
            # generates a new car -index location
            random_y = random.randint(-240, 280)
            # Has the new car go to that location, note the x-index is he same always
            new_car.goto(300, random_y)
            # Add the new car to the all_cars list
            self.all_cars.append(new_car)

    # Set the car movement and speed
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    # Stops all the cars
    def stop_cars(self):
        for car in self.all_cars:
            car.backward(0)

    # Increasing the speed when we increase the level
    def increase_speed(self):
        self.speed += 1