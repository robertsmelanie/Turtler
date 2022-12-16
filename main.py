import time 
from turtle import Screen, Turtle 
# Add First created import statement
from player import Player
from car_manager import CarManager
#
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # has everything not start at 0, 0 and move to its starting position)

# Create our objects to manipulate
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# listen() listens for any inputs we give
screen.listen()
# Sets it so we run the move_method whenever the Up key is entered
screen.onkey(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    # Sleep keeps the program from running to fast
    time.sleep(0.1)
    # This keeps the screen updating 
    screen.update()

    #Create the cars
    car_manager.create_car()
    # Move the cars
    car_manager.move_cars()

    # Setup if player finishes the level
    if player.crossed_finish():
        # Remember this function is setup to return a boolean value of True or False
        player.reset_turtle()
        scoreboard.increase_level()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()