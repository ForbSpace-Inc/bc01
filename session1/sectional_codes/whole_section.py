# =============================================
# SECTION 1.1: Your First Program – Hello World
# =============================================



# 01_hello_world.py
# Live Demo
print("Hello, World!")

# Explanation:
# print() = “show this on the screen”
# Everything inside the " " is text (called a string).
# The () tell the computer “do the print action now”.

# ------------------------------
# STUDENT ACTIVITY 1
# Change the message to “Hello, my name is_________!”
print("TODO: Change this line → Hello, my name is [YOUR NAME]!")

# ------------------------------
# STUDENT ACTIVITY 2
# Add a second line
print("TODO: Add another print statement below this line")
# Example (uncomment if you want):
# print("I am ready to code!")

# 02_variables.py
# =============================================
# SECTION 1.2: Variables – Memory Boxes
# =============================================

# Live Demo
name = "Alex"           # string (text)
age = 16                # integer (whole number)
height = 1.65           # float (number with decimal)
is_student = True       # boolean (True or False)

print(name)
print("My name is", name, "and I am", age, "years old.")

# Teacher tip: You can change a variable anytime
# age = age + 1
# print("Next year I will be", age)

# ------------------------------
# STUDENT ACTIVITY
# Create four variables about YOURSELF:
# name, age, favorite_subject, favorite_food
#
# Then print TWO different sentences using all four variables.

# TODO: Write your code here (replace the example)
my_name = "Your Name Here"
my_age = 15
my_favorite_subject = "Science"
my_favorite_food = "Pizza"

print("My name is", my_name, "and I am", my_age, "years old.")
print("I love", my_favorite_subject, "and my favorite food is", my_favorite_food, "!")


# 03_user_input.py
# =============================================
# SECTION 1.3: Getting Information from the User
# =============================================

# Live Demo
name = input("What is your name? ")
print("Hello", name, "! Nice to meet you.")

# ------------------------------
# STUDENT ACTIVITY (10 minutes)
# Make a short “greeting program” that asks for:
#   • name
#   • age
#   • favorite color
# Then prints ONE nice sentence using all three answers.

# TODO: Write your greeting program below
name = input("What is your name? ")
age = input("How old are you? ")
favorite_color = input("What is your favorite color? ")

print("Nice to meet you,", name, "! You are", age, "years old and your favorite color is", favorite_color, "!")


# 04_math_operations.py
# =============================================
# SECTION 1.4: Doing Math & Operations
# =============================================

# Live Demo
a = 10
b = 5
print(a + b)      # addition
print(a - b)      # subtraction
print(a * b)      # multiplication
print(a / b)      # division
print(a ** 2)     # power (10 to the power of 2)
print(a % 3)      # remainder

# ------------------------------
# STUDENT ACTIVITY (10 minutes)
# Build a tiny “age calculator”

# TODO: Write the age calculator here (uncomment and run)
# age = int(input("How old are you? "))
# print("You are", age * 12, "months old.")
# print("You are", age * 365, "days old.")

# 05_if_else.py
# =============================================
# SECTION 1.5: Making Decisions – if / else
# =============================================

# Live Demo
age = int(input("How old are you? "))
if age >= 13:
    print("You can join!")
else:
    print("Sorry, you need to be 13 or older.")

# Important: Lines under if and else must be indented (press Tab key)

# ------------------------------
# STUDENT ACTIVITY (15 minutes)
# Create a program that asks for a test score (0–100) and prints:
#   • “Excellent!” if score ≥ 80
#   • “Good job!” if score ≥ 60
#   • “Keep practicing!” otherwise

# TODO: Write your code here (starter already provided - just run and change if you want)
score = int(input("What is your test score (0-100)? "))

if score >= 80:
    print("Excellent!")
elif score >= 60:
    print("Good job!")
else:
    print("Keep practicing!")



# 06_loops.py
# =============================================
# SECTION 1.6: Repeating Things – Loops
# =============================================

# 1. For loop
print("--- For Loop Example ---")
for i in range(5):
    print("This line will repeat 5 times!")

# 2. While loop
print("\n--- While Loop Example ---")
count = 1
while count <= 5:
    print(count)
    count = count + 1

# Try changing the numbers and run again!
# Example ideas:
# Change range(5) → range(10)
# Change while count <= 5 → while count <= 10



