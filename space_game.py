import turtle
import random
import time
import os

# Game settings
WIDTH = 800
HEIGHT = 600
SHIP_SPEED = 5
ASTEROID_SPEED = 3
FUEL_SPEED = 2
LIVES = 3

# High score file
HIGH_SCORE_FILE = "high_score.txt"

# Load high score
def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read())
    return 0

# Save high score
def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

# Setup screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Asteroid Dodger - NASA Space Mission")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)  # Fast updates

# Score and lives
score = 0
high_score = load_high_score()
lives = LIVES

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.write("Score: 0  High: {}  Lives: {}".format(high_score, lives), align="center", font=("Arial", 24, "normal"))

# Spaceship
ship = turtle.Turtle()
ship.shape("triangle")
ship.color("cyan")
ship.penup()
ship.speed(0)
ship.goto(0, -250)
ship.dy = 0
ship.dx = 0

# Lists
asteroids = []
fuels = []

# Create asteroid
def create_asteroid():
    a = turtle.Turtle()
    size = random.randint(20, 40)
    a.shapesize(size/20)
    a.shape("circle")
    a.color("gray")
    a.penup()
    a.goto(random.randint(-WIDTH//2 + 50, WIDTH//2 - 50), HEIGHT//2)
    a.dy = -ASTEROID_SPEED - random.randint(1, 3)
    asteroids.append(a)

# Create fuel orb
def create_fuel():
    f = turtle.Turtle()
    f.shape("circle")
    f.color("yellow")
    f.penup()
    f.shapesize(0.5)
    f.goto(random.randint(-WIDTH//2 + 50, WIDTH//2 - 50), HEIGHT//2)
    f.dy = -FUEL_SPEED
    fuels.append(f)

# Collision detection
def is_collided(t1, t2):
    return abs(t1.xcor() - t2.xcor()) < 30 and abs(t1.ycor() - t2.ycor()) < 30

# Keyboard controls
def go_up():
    ship.dy = SHIP_SPEED

def go_down():
    ship.dy = -SHIP_SPEED

def go_left():
    ship.dx = -SHIP_SPEED

def go_right():
    ship.dx = SHIP_SPEED

def no_movement():  # Inertia decay
    if ship.dx > 0:
        ship.dx -= 0.5
    elif ship.dx < 0:
        ship.dx += 0.5
    if ship.dy > 0:
        ship.dy -= 0.5
    elif ship.dy < 0:
        ship.dy += 0.5

wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Main game loop
game_running = True
spawn_timer = 0
fuel_timer = 0

while game_running:
    wn.update()

    # Spawn asteroids/fuel
    spawn_timer += 1
    if spawn_timer > 30:  # Every ~0.5 sec
        create_asteroid()
        spawn_timer = 0
    fuel_timer += 1
    if fuel_timer > 120:  # Rarer fuel
        create_fuel()
        fuel_timer = 0

    # Move ship (with inertia)
    no_movement()
    ship.setx(ship.xcor() + ship.dx)
    ship.sety(ship.ycor() + ship.dy)

    # Boundaries
    if ship.xcor() > WIDTH//2 - 20:
        ship.setx(WIDTH//2 - 20)
    if ship.xcor() < -WIDTH//2 + 20:
        ship.setx(-WIDTH//2 + 20)
    if ship.ycor() > HEIGHT//2 - 20:
        ship.sety(HEIGHT//2 - 20)
    if ship.ycor() < -HEIGHT//2 + 20:
        ship.sety(-HEIGHT//2 + 20)

    # Move & remove asteroids
    for a in asteroids[:]:
        a.sety(a.ycor() + a.dy)
        if a.ycor() < -HEIGHT//2:
            a.goto(1500, 1500)  # Offscreen
            asteroids.remove(a)
        if is_collided(ship, a):
            lives -= 1
            a.goto(1500, 1500)
            asteroids.remove(a)
            pen.clear()
            pen.goto(0, 250)
            pen.write("Score: {}  High: {}  Lives: {}".format(score, high_score, lives), align="center", font=("Arial", 24, "normal"))
            if lives == 0:
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)
                pen.goto(0, 0)
                pen.write("GAME OVER! Final Score: {}".format(score), align="center", font=("Arial", 36, "normal"))
                time.sleep(2)
                game_running = False

    # Move & collect fuels
    for f in fuels[:]:
        f.sety(f.ycor() + f.dy)
        if f.ycor() < -HEIGHT//2:
            f.goto(1500, 1500)
            fuels.remove(f)
        if is_collided(ship, f):
            score += 10
            f.goto(1500, 1500)
            fuels.remove(f)
            pen.clear()
            pen.goto(0, 250)
            pen.write("Score: {}  High: {}  Lives: {}".format(score, high_score, lives), align="center", font=("Arial", 24, "normal"))

    time.sleep(1/120)  # 60 FPS

wn.bye()