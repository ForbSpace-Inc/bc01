import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Adventure")

# Draw a rocket
rocket = turtle.Turtle()
rocket.color("white")
rocket.penup()
rocket.goto(0, -100)
rocket.pendown()
rocket.begin_fill()
rocket.goto(-20, -150)
rocket.goto(20, -150)
rocket.goto(0, -100)
rocket.end_fill()

# Draw random stars
for _ in range(20):
    star = turtle.Turtle()
    star.color("yellow")
    star.penup()
    star.goto(random.randint(-300, 300), random.randint(-300, 300))
    star.dot(5)

# Draw a planet
def draw_planet(x, y, color):
    planet = turtle.Turtle()
    planet.color(color)
    planet.penup()
    planet.goto(x, y)
    planet.pendown()
    planet.circle(50)

draw_planet(200, 100, "blue")  # Earth-like planet

turtle.done()