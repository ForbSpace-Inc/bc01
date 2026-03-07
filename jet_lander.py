import turtle
import random
import time
import os

# Game settings
WIDTH = 800
HEIGHT = 600
GRAVITY = 0.4  # Realistic pull down
THRUST = 2.0
LIFT_FACTOR = 0.1  # Speed creates lift
RUNWAY_START = -100
RUNWAY_END = 100
MAX_FUEL = 500
LAND_SPEED = 8  # Max safe landing speed

# High score (best landings)
HIGH_SCORE_FILE = "jet_high_score.txt"

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
wn.bgcolor("lightblue")
wn.title("Jet Lander - FAA Pilot Challenge")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)

# Score (landings)
score = 0
high_score = load_high_score()
fuel = MAX_FUEL
attempts = 5

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 250)
pen.write("Landings: 0  High: {}  Fuel: {}  Attempts: {}".format(high_score, fuel, attempts), align="center", font=("Arial", 24, "normal"))

# Jet
jet = turtle.Turtle()
jet.shape("square")
jet.color("red")
jet.penup()
jet.tilt(90)  # Point right
jet.speed(0)
jet.goto(-WIDTH//2 + 50, 0)
jet.altitude = 200  # Start altitude
jet.speed_x = 3  # Forward speed
jet.fuel = MAX_FUEL

# Runway
runway = turtle.Turtle()
runway.penup()
runway.pencolor("green")
runway.pensize(10)
runway.goto(RUNWAY_START, -HEIGHT//2 + 20)
runway.pendown()
runway.goto(RUNWAY_END, -HEIGHT//2 + 20)
runway.penup()

# Clouds (moving background)
clouds = []
for _ in range(5):
    c = turtle.Turtle()
    c.shape("circle")
    c.color("white")
    c.penup()
    c.shapesize(3, 5)
    c.goto(random.randint(-WIDTH//2, WIDTH//2), random.randint(100, HEIGHT//2 - 50))
    c.dx = random.uniform(0.5, 1.5)
    clouds.append(c)

# Keyboard
def thrust_up():
    global fuel
    if fuel > 0:
        jet.dy = THRUST  # Thrust up
        fuel -= 1

def pitch_down():
    jet.dy = -1  # Slight down

def speed_up():
    jet.speed_x += 0.2

def speed_down():
    if jet.speed_x > 1:
        jet.speed_x -= 0.2

wn.listen()
wn.onkey(thrust_up, "Up")
wn.onkey(pitch_down, "Down")
wn.onkey(speed_up, "Right")
wn.onkey(speed_down, "Left")

# Main loop
game_running = True
landed = False

while game_running:
    wn.update()

    # Physics: Gravity, lift, thrust
    lift = jet.speed_x * LIFT_FACTOR
    net_force = -GRAVITY + lift + getattr(jet, 'dy', 0)
    jet.altitude += net_force
    if hasattr(jet, 'dy'):
        del jet.dy  # Reset thrust

    # Move forward
    jet.setx(jet.xcor() + jet.speed_x)

    # Rotate for pitch (visual)
    if net_force > 0:
        jet.tiltangle(90 - net_force*5)
    else:
        jet.tiltangle(90 + abs(net_force)*5)

    # Update position
    jet.sety(-HEIGHT//2 + 30 + jet.altitude)

    # Move clouds
    for c in clouds:
        c.setx(c.xcor() + c.dx)
        if c.xcor() > WIDTH//2:
            c.setx(-WIDTH//2)

    # Landing check
    if jet.xcor() > RUNWAY_START and jet.xcor() < RUNWAY_END and jet.altitude < 10:
        if jet.speed_x < LAND_SPEED and jet.altitude > -5:
            score += 1
            if score > high_score:
                high_score = score
                save_high_score(high_score)
            pen.clear()
            pen.goto(0, 250)
            pen.write("SUCCESSFUL LANDING! Landings: {}  High: {}".format(score, high_score), align="center", font=("Arial", 36, "normal"))
            time.sleep(1)
            # Reset for next
            jet.goto(-WIDTH//2 + 50, 0)
            jet.altitude = 200
            jet.speed_x = 3
            fuel = MAX_FUEL
        else:
            pen.clear()
            pen.goto(0, 0)
            pen.write("CRASH! Too fast/high.", align="center", font=("Arial", 24, "normal"))
            time.sleep(1)
            attempts -= 1
            jet.goto(-WIDTH//2 + 50, 0)
            jet.altitude = 200
            jet.speed_x = 3
            fuel = MAX_FUEL
        pen.clear()
        pen.goto(0, 250)
        pen.write("Landings: {}  High: {}  Fuel: {}  Attempts: {}".format(score, high_score, fuel, attempts), align="center", font=("Arial", 24, "normal"))
        if attempts == 0:
            pen.goto(0, 0)
            pen.write("Mission Complete! Total Landings: {}".format(score), align="center", font=("Arial", 36, "normal"))
            time.sleep(3)
            game_running = False

    # Crash if too low off-runway
    if jet.altitude < 0 and not (RUNWAY_START < jet.xcor() < RUNWAY_END):
        attempts -= 1
        pen.clear()
        pen.goto(0, 0)
        pen.write("CRASH Off Runway!", align="center", font=("Arial", 24, "normal"))
        time.sleep(1)
        jet.goto(-WIDTH//2 + 50, 0)
        jet.altitude = 200
        jet.speed_x = 3
        fuel = MAX_FUEL
        pen.clear()
        pen.goto(0, 250)
        pen.write("Landings: {}  High: {}  Fuel: {}  Attempts: {}".format(score, high_score, fuel, attempts), align="center", font=("Arial", 24, "normal"))

    # Boundaries/fuel out
    if jet.altitude > HEIGHT//2 - 100:
        jet.altitude = HEIGHT//2 - 100
    if fuel < 0:
        fuel = 0

    time.sleep(1/60)  # 60 FPS

wn.bye()