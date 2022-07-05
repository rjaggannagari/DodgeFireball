# imports 
import turtle
import random

# creates the window
window = turtle.Screen()
window.title('Dodge the Object')
window.bgcolor(0, 0, 0)
window.setup(width = 800, height = 600)
window.tracer(0)
window.register_shape("alien_ship.gif")

# space ship object
space_ship = turtle.Turtle()
space_ship.shape("alien_ship.gif")
space_ship.color("white")
space_ship.penup()
space_ship.goto(0,-250)

# adds movement to the right
def move_right():
    old_x_cord = space_ship.xcor()
    new_x_cord = old_x_cord + 10
    space_ship.setx(new_x_cord)

# adds movement to the left
def move_left():
    old_x_cord = space_ship.xcor()
    new_x_cord = old_x_cord - 10
    space_ship.setx(new_x_cord)

# adds movement up
def move_up():
    old_y_cord = space_ship.ycor()
    new_y_cord = old_y_cord + 10
    space_ship.sety(new_y_cord)

# adds movement down
def move_down():
    old_y_cord = space_ship.ycor()
    new_y_cord = old_y_cord - 10
    space_ship.sety(new_y_cord)

# checks to see the movement
window.listen()
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

while True:
    window.update()