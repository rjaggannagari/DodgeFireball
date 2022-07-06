# imports 
import turtle
import random
import time

# creates the game window
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
space_ship.speed(10)

# the score starts at 0
score = 0
#scoreboard object
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0".format(score), align="center", font=("Courier", 24, "normal"))

meteors = []
# meteor objects
for _ in range (10):
    meteor = turtle.Turtle()
    meteor.shape("fire.gif")
    meteor.speed(10)
    meteor.penup()
    # random x coordinate to get spawned into
    random_x = random.randint(-400, 400)
    meteor.goto(random_x, 300)
    meteor.speed(random.uniform(0.4, 0.8))
    meteors.append(meteor)
    time.sleep(0.1)

below_meteors = []
# below meteor objects
for _ in range (10):
    below_meteor = turtle.Turtle()
    below_meteor.shape("fire.gif")
    below_meteor.speed(10)
    meteor.penup()
    # random x coordinate to get spawned into
    random_x = random.randint(-400, 400)
    below_meteor.goto(random_x, -300)
    below_meteor.speed(random.uniform(0.4, 0.8))
    below_meteors.append(below_meteor)
    time.sleep(0.1)

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

# only runs when it is true
game_running = True
while game_running:
    window.update()

    # the top meteors
    for meteor in meteors:
        new_y = meteor.ycor()
        new_y -= random.uniform(0.2, 0.8)
        meteor.sety(new_y)

        # this checks to see if there is a collision between the ship and the meteor
        if space_ship.distance(meteor) < 25:
            print("Game Over")
            time.sleep(2)
            game_running = False

        # this gives us a new random x value for the meteor
        new_random_x = random.randint(-390, 390)

        # respawns the fireball at a new location
        if meteor.ycor() < -300:
            meteor.goto(new_random_x, 300)
            score = score + 1
            pen.clear()
            pen.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal"))

    # the bottom meteors
    for below_meteor in below_meteors:
        new_below_y = below_meteor.ycor()
        new_below_y += random.uniform(0.2, 0.8)
        below_meteor.sety(new_below_y)

        # this checks to see if there is a collision between the ship and the meteor
        if space_ship.distance(below_meteor) < 25:
            print("Game Over")
            time.sleep(2)
            game_running = False

        # this gives us a new random x value for the meteor
        new_bottom_random_x = random.randint(-390, 390)

        # respawns the fireball at a new location
        if below_meteor.ycor() > 300:
            below_meteor.goto(new_bottom_random_x, -300)
            score = score + 1
            pen.clear()
            pen.write("Score: {} ".format(score), align="center", font=("Courier", 24, "normal"))