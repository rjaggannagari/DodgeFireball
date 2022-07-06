# imports 
import turtle
import random

# creates the window
window = turtle.Screen()
window.title('Dodge the Object')
window.bgpic('space_bg.gif')
window.setup(width = 800, height = 600)
window.tracer(0)
window.register_shape("alien.gif")
window.register_shape("fire.gif")

# space ship object
space_ship = turtle.Turtle()
space_ship.shape("alien.gif")
space_ship.color("white")
space_ship.penup()
space_ship.goto(0, 0)
space_ship.speed(5)

# meteor object
meteor = turtle.Turtle()
meteor.shape("fire.gif")
meteor.penup()
# random x coordinate to get spawned into
random_x = random.randint(-400, 400)
meteor.goto(random_x, 300)

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

    # sets a speed up for the meteor to fly down
    old_meteor_y = meteor.ycor()
    new_meteor_y = old_meteor_y - 0.1
    meteor.sety(new_meteor_y)

    # this gives us a new random x value for the meteor
    new_random_x = random.randint(-400, 400)
    # respawns the fireball at a new location
    if meteor.ycor() < -300:
        meteor.goto(new_random_x, 300)

    if space_ship.distance(meteor) < 25:
        print("You Lost")
        window.resetscreen()