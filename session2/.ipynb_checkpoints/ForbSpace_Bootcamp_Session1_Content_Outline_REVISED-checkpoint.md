# FORBSPACE BOOTCAMP SESSION #1
## Programming for Teens: Space Adventure
### April 13-14, 2026 | ForbSpace Cafe, Kitale

---

## SESSION OVERVIEW

**Target Audience:** High School Students (Ages 13-17)  
**Duration:** 2 Days (10:00 AM - 3:00 PM each day)  
**Theme:** Programming for Teens: Space Adventure  
**Platform:** Online-Python (https://www.online-python.com/) + Scratch  
**Instructor-to-Student Ratio:** 1:10 (with assistant tutors)

---

## LEARNING OBJECTIVES

By the end of Session #1, students will be able to:

1. **Understand the Four Pillars of Coding** using simple everyday examples
2. **Write basic Python programs** including output, variables, and user input
3. **Perform mathematical operations** and create simple calculators
4. **Make decisions in code** using if/else conditional statements
5. **Create repeating actions** using for and while loops
6. **Build reusable code blocks** using functions
7. **Connect coding concepts to space exploration**
8. **Develop a space-themed game** using Scratch (NASA JPL Mars Rover project)

---

## DAY 1: FOUNDATIONS OF CODING (April 13, 2026)

### WELCOME & ICE BREAKERS

#### Opening Activities:
1. **"Registration Station"**
   - Students sign in and receive name tags
   - Quick introduction round: "Name + One thing you want to learn"

2. **"What is Coding?" Brainstorm**
   - Ask students what they think coding is
   - Show examples: Phone apps, games, websites, calculators
   - Explain: "Coding is giving instructions to a computer"

3. **"Code Your Name"**
   - Students write their name using print statements
   - Example: `print("Hello, I am Alex!")`

#### Materials Needed:
- Name tags and markers
- Whiteboard for brainstorming
- Example code printouts

---

### THE FOUR PILLARS OF CODING

#### Introduction
- Welcome to the ForbSpace Coding Bootcamp
- Overview of the 4-day bootcamp journey
- Introduction to Python: "A language that is easy to learn and very powerful"

---

## **PILLAR 1: VARIABLES - Storing Information**

### Simple Explanation First

**What are Variables?**
- Variables are like **labeled boxes** where you store information
- Think of it like writing your name on a box and putting something inside
- You can look inside the box anytime, or change what's inside

**Everyday Example:**
```
Imagine you have a box labeled "my_name"
You write "Alex" on a paper and put it in the box
Later, you can open the box and see "Alex"
```

**In Python:**
```python
my_name = "Alex"
my_age = 16
my_favorite_color = "blue"

print(my_name)           # Shows: Alex
print(my_age)            # Shows: 16
print(my_favorite_color) # Shows: blue
```

**Data Types (The kinds of information you can store):**
1. **Text (String)** - Words and sentences: "Hello", "Alex", "I love coding"
2. **Numbers (Integer)** - Whole numbers: 16, 100, 2026
3. **Decimal Numbers (Float)** - Numbers with dots: 1.65, 9.5, 3.14
4. **Yes/No (Boolean)** - True or False only

**Try It Yourself:**
```python
name = "Your Name"
age = 15
height = 1.70
likes_coding = True

print("My name is", name)
print("I am", age, "years old")
print("I am", height, "meters tall")
print("I like coding:", likes_coding)
```

### Now Connect to Space

**Space Example:**
```python
astronaut_name = "Alex"
oxygen_level = 100
distance_to_mars = 225000000
is_ready_for_launch = True

print("Astronaut:", astronaut_name)
print("Oxygen level:", oxygen_level, "%")
print("Distance to Mars:", distance_to_mars, "km")
print("Ready for launch:", is_ready_for_launch)
```

**Activity: Create Your Profile**
- Create variables for your name, age, favorite subject, and dream job
- Print a sentence using all your variables

---

## **PILLAR 2: CONDITIONALS - Making Decisions**

### Simple Explanation First

**What are Conditionals?**
- Conditionals help your program make decisions
- Like when you decide: "If it's raining, take an umbrella. Otherwise, wear sunglasses."

**Everyday Example:**
```
IF you are hungry:
    Eat some food
ELSE:
    Keep doing what you're doing
```

**In Python:**
```python
age = 16

if age >= 13:
    print("You are a teenager!")
else:
    print("You are not a teenager yet.")
```

**Comparison Operators (How we compare things):**
- `==` means "equal to" (age == 16)
- `!=` means "not equal to" (name != "John")
- `>` means "greater than" (score > 50)
- `<` means "less than" (temperature < 30)
- `>=` means "greater than or equal to" (age >= 18)
- `<=` means "less than or equal to" (score <= 100)

**Try It Yourself:**
```python
score = 75

if score >= 80:
    print("Excellent! You got an A!")
elif score >= 60:
    print("Good job! You passed!")
else:
    print("Keep practicing! You'll get it next time.")
```

### Now Connect to Space

**Space Example:**
```python
oxygen_level = 85

if oxygen_level >= 80:
    print("Oxygen level is GOOD")
elif oxygen_level >= 50:
    print("Oxygen level is OKAY")
else:
    print("WARNING! Low oxygen level!")
```

**Activity: Grade Calculator**
- Ask user for their test score (0-100)
- Print different messages based on their score
- A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: Below 60

---

## **PILLAR 3: LOOPS - Repeating Actions**

### Simple Explanation First

**What are Loops?**
- Loops let you repeat something many times without writing it over and over
- Like counting from 1 to 10 - you don't write ten different lines, you use a loop!

**Everyday Example:**
```
Count from 1 to 5:
1... 2... 3... 4... 5...

Instead of writing:
print(1)
print(2)
print(3)
print(4)
print(5)

We write:
for number in range(1, 6):
    print(number)
```

**Two Types of Loops:**

**1. For Loop** - Use when you know HOW MANY times to repeat:
```python
# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Print "Hello" 5 times
for i in range(5):
    print("Hello!")
```

**2. While Loop** - Use when you DON'T know how many times:
```python
# Keep asking until user says "yes"
answer = ""
while answer != "yes":
    answer = input("Do you want to continue? ")
print("Okay, continuing...")
```

**Try It Yourself:**
```python
# Multiplication table for number 5
print("5 times table:")
for i in range(1, 11):
    result = 5 * i
    print("5 x", i, "=", result)
```

### Now Connect to Space

**Space Example:**
```python
# Countdown to launch
print("Starting countdown...")
for i in range(10, 0, -1):
    print(i, "...")
print("BLAST OFF!")

# Monitor fuel level
fuel = 100
while fuel > 0:
    print("Fuel remaining:", fuel, "%")
    fuel = fuel - 10
print("Fuel empty!")
```

**Activity: Countdown Timer**
- Create a countdown from 10 to 1
- Then print "Liftoff!"
- Bonus: Add a message at each number

---

## **PILLAR 4: FUNCTIONS - Reusable Code**

### Simple Explanation First

**What are Functions?**
- Functions are blocks of code you can use again and again
- Like a recipe - you write it once, then use it whenever you need it

**Everyday Example:**
```
Recipe for making tea:
1. Boil water
2. Put tea bag in cup
3. Pour hot water
4. Wait 3 minutes
5. Remove tea bag

Every time you want tea, you follow this recipe (function).
You don't write new instructions each time!
```

**In Python:**
```python
# Define the function
def say_hello():
    print("Hello!")
    print("How are you today?")

# Use the function (call it)
say_hello()
say_hello()
say_hello()
```

**Functions with Input (Parameters):**
```python
def greet_person(name):
    print("Hello,", name + "!")
    print("Nice to meet you!")

greet_person("Alex")
greet_person("Sarah")
greet_person("John")
```

**Functions that Give Back (Return Values):**
```python
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(5, 3)
print("5 + 3 =", answer)
```

**Try It Yourself:**
```python
def print_separator():
    print("--------------------")

print_separator()
print("Welcome to my program!")
print_separator()
print("This is the main content.")
print_separator()
```

### Now Connect to Space

**Space Example:**
```python
def launch_countdown():
    print("Starting countdown...")
    for i in range(10, 0, -1):
        print(i, "...")
    print("BLAST OFF!")

def check_fuel_level(fuel):
    if fuel >= 80:
        return "Fuel level is GOOD"
    elif fuel >= 50:
        return "Fuel level is OKAY"
    else:
        return "WARNING! Low fuel!"

# Use the functions
launch_countdown()
status = check_fuel_level(75)
print(status)
```

**Activity: Create Your Own Functions**
- Create a function that prints your name 3 times
- Create a function that takes two numbers and adds them
- Create a function that prints a decorative border

---

## SUMMARY: THE FOUR PILLARS

| Pillar | Simple Explanation | Space Connection |
|--------|-------------------|------------------|
| **Variables** | Labeled boxes to store information | Storing astronaut name, oxygen level, fuel |
| **Conditionals** | Making decisions (if/else) | Checking if oxygen is low, if fuel is enough |
| **Loops** | Repeating actions | Countdown timer, monitoring systems |
| **Functions** | Reusable blocks of code | Launch sequence, status checks |

**Remember:** These four pillars are the foundation of ALL programming. Every program you write will use these concepts!

---

### YOUR FIRST PROGRAM - HELLO WORLD

**The print() Function:**
- `print()` tells the computer to show something on the screen
- Put your message inside quotes: `print("Hello!")`

**Live Demo:**
```python
print("Hello, World!")
print("Welcome to ForbSpace Bootcamp!")
print("I am learning to code!")
```

**Student Activities:**

**Activity 1: Personalize Your Message**
```python
# Change the message to your name
print("Hello, my name is [YOUR NAME]!")
print("I am excited to learn coding!")
```

**Activity 2: Multi-Line Messages**
```python
print("Hello, everyone!")
print("I am ready to code!")
print("Let's learn together!")
```

**Challenge Activity: Create a Simple Pattern**
```python
print("* * * * *")
print("*       *")
print("*       *")
print("* * * * *")
```

**Common Errors to Watch For:**
- Missing quotes: `print(Hello)` ❌ → `print("Hello")` ✓
- Mismatched quotes: `print('Hello")` ❌ → `print("Hello")` ✓
- Missing parentheses: `print "Hello"` ❌ → `print("Hello")` ✓

---

### GETTING USER INPUT

**The input() Function:**
- `input()` asks the user a question
- The program waits for the user to type and press Enter
- The answer is stored as text

**Live Demo:**
```python
# Basic input
name = input("What is your name? ")
print("Hello,", name, "!")

# Multiple inputs
favorite_color = input("What is your favorite color? ")
print("Your favorite color is", favorite_color)
```

**Important:** Converting input to numbers:
```python
# For whole numbers
age = int(input("How old are you? "))

# For decimal numbers
height = float(input("What is your height in meters? "))
```

**Student Activity: Create a Registration Form**
```python
print("=== REGISTRATION FORM ===")
print()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_subject = input("What is your favorite subject? ")

print()
print("=== YOUR INFORMATION ===")
print("Name:", name)
print("Age:", age)
print("Favorite Subject:", favorite_subject)
print("Welcome to the bootcamp!")
```

---

### MATH & OPERATIONS

**Basic Operators:**
| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | + | 10 + 5 | 15 |
| Subtraction | - | 10 - 5 | 5 |
| Multiplication | * | 10 * 5 | 50 |
| Division | / | 10 / 5 | 2.0 |
| Power | ** | 10 ** 2 | 100 |
| Remainder | % | 10 % 3 | 1 |

**Live Demo:**
```python
# Basic calculations
a = 10
b = 5

print(a + b)     # 15
print(a - b)     # 5
print(a * b)     # 50
print(a / b)     # 2.0
print(a ** 2)    # 100 (10 squared)
print(a % 3)     # 1 (remainder of 10 divided by 3)
```

**Student Activity: Simple Calculator**
```python
print("=== SIMPLE CALCULATOR ===")
print()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print()
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

## DAY 2: ADVANCED CONCEPTS & PROJECTS (April 14, 2026)

### DAY 2 WARM-UP

#### Review Activity: "Code Relay Race"
- Students form teams of 4
- Each team member writes one line of code
- Goal: Create a working program that greets a user and calculates their age next year
- First team to produce working code wins!

---

### REVIEW & PRACTICE: THE FOUR PILLARS

#### Variables Practice
```python
# Create a simple profile
name = "Alex"
age = 16
school = "Kitale High"
grade = 10

print("Name:", name)
print("Age:", age)
print("School:", school)
print("Grade:", grade)

# Calculate age next year
age_next_year = age + 1
print("Next year I will be:", age_next_year)
```

#### Conditionals Practice
```python
# Simple grade checker
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - Keep it up!")
elif score >= 60:
    print("Grade: D - Needs improvement")
else:
    print("Grade: F - Study harder next time")
```

#### Loops Practice
```python
# Print numbers 1 to 10
print("Counting from 1 to 10:")
for i in range(1, 11):
    print(i)

# Print multiplication table for 7
print("\n7 times table:")
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
```

#### Functions Practice
```python
def greet(name):
    print("Hello,", name + "!")
    print("Welcome to coding class!")

def add(a, b):
    return a + b

# Use the functions
greet("Alex")
greet("Sarah")

result = add(10, 5)
print("10 + 5 =", result)
```

---

### CONNECTING TO SPACE: SPACE CALCULATOR PROJECT

Now that we understand the basics, let's create a Space Calculator!

```python
print("=== SPACE CALCULATOR ===")
print()

# Get user's Earth information
name = input("What is your name? ")
earth_age = int(input("How old are you on Earth? "))
earth_weight = float(input("What is your weight on Earth (kg)? "))

print()
print("=== YOUR SPACE INFORMATION ===")
print()

# Calculate age on other planets
mars_age = earth_age / 1.88
jupiter_age = earth_age / 11.86

# Calculate weight on other planets
moon_weight = earth_weight * 0.165
mars_weight = earth_weight * 0.38

print("Hello,", name + "!")
print()
print("Your age on different planets:")
print("  On Earth:", earth_age, "years")
print("  On Mars:", round(mars_age, 1), "years")
print("  On Jupiter:", round(jupiter_age, 1), "years")
print()
print("Your weight on different places:")
print("  On Earth:", earth_weight, "kg")
print("  On the Moon:", round(moon_weight, 1), "kg")
print("  On Mars:", round(mars_weight, 1), "kg")
```

---

### NASA JPL MARS ROVER PROJECT

#### Project Introduction

**About the Project:**
- Students will create a Mars Rover game using Scratch
- Based on NASA JPL's "Explore Mars with Scratch" lesson
- Learn computational thinking and basic game design

**What You'll Create:**
1. A Mars Rover that moves around the screen
2. Science targets (rocks/samples) to collect
3. Hazards (craters) to avoid
4. A scoring system
5. A timer

**Step-by-Step Instructions:**

**Step 1: Set Up the Environment**
1. Go to scratch.mit.edu and create an account
2. Create a new project
3. Add Mars surface backdrop
4. Add Mars rover sprite

**Step 2: Program Rover Movement**
```scratch
When [up arrow] key pressed
  move [10] steps

When [left arrow] key pressed
  turn left [15] degrees

When [right arrow] key pressed
  turn right [15] degrees
```

**Step 3: Add Science Targets**
1. Add rock/sample sprites
2. Program collection:
```scratch
When green flag clicked
  go to x:[random] y:[random]

When touching [rover]
  hide
  change [score] by [10]
  go to x:[random] y:[random]
  show
```

**Step 4: Add Hazards**
1. Add crater/rock hazard sprites
2. Program hazard detection:
```scratch
When touching [hazard]
  say ["Ouch!"] for [2] seconds
  change [score] by [-5]
```

**Step 5: Add Timer and Scoring**
```scratch
When green flag clicked
  set [score] to [0]
  set [time] to [60]
  repeat until [time] = [0]
    wait [1] seconds
    change [time] by [-1]
  say ["Mission Complete!"] for [5] seconds
```

**Step 6: Customize Your Game**
- Add sounds
- Change backgrounds
- Add more sprites
- Make it your own!

---

### PROJECT SHOWCASE & WRAP-UP

#### Project Showcase
- Volunteers demonstrate their Mars Rover games
- Class provides positive feedback
- Discuss what was learned

#### Wrap-Up
- Review of Session #1 concepts
- Preview of Session #2 (Python Takeoff)
- Distribute certificates of completion
- Group photo

---

## TEACHING TIPS & BEST PRACTICES

### For Teaching Beginners:
1. **Start simple** - Use everyday examples before space examples
2. **Show, don't just tell** - Live code everything
3. **Encourage experimentation** - Let students try changing things
4. **Celebrate mistakes** - They're learning opportunities
5. **Use visual aids** - Draw on the whiteboard
6. **Check for understanding** - Ask "Does this make sense?"

### Common Student Challenges:
1. **Syntax errors** - Typos, missing quotes, missing colons
2. **Indentation errors** - Python cares about spaces!
3. **Variable name confusion** - Using different names than defined
4. **Forgetting to convert input** - input() always gives text

### How to Help:
- Read error messages together
- Check for typos first
- Use print() to debug
- Compare working code with their code

---

## MATERIALS CHECKLIST

### For Instructors:
- [ ] Projector and screen
- [ ] Whiteboard and markers
- [ ] Printed "Four Pillars" reference sheet
- [ ] Name tags and markers
- [ ] Solution code for all activities

### For Students:
- [ ] Computers with internet access
- [ ] Access to online-python.com
- [ ] Scratch accounts (created in advance)
- [ ] Printed "Four Pillars Reference Card"
- [ ] Notebook and pen

---

## ASSESSMENT RUBRIC

### Participation (40%):
- Attends all sessions
- Participates in activities
- Asks questions
- Helps peers

### Coding Skills (40%):
- Completes all coding exercises
- Code runs without errors
- Demonstrates understanding of concepts
- Completes challenge activities

### Project (20%):
- Mars Rover game is functional
- Includes required features
- Shows creativity and effort
- Can explain how code works

---

## ADDITIONAL RESOURCES

### For Students:
- Online Python: https://www.online-python.com/
- Scratch: https://scratch.mit.edu/
- NASA JPL Lessons: https://www.jpl.nasa.gov/edu/resources/lesson-plan/explore-mars-with-scratch/

### For Instructors:
- Python for Beginners: https://docs.python.org/3/tutorial/
- Teaching Strategies: https://cseducators.stackexchange.com/
- NASA Educational Resources: https://www.jpl.nasa.gov/edu/

---

## CONTACT INFORMATION

**ForbSpace Inc.**  
Kitale-Webuye Road  
PO BOX 3082-02000  
Kitale, Kenya  

Email: forbspace24@gmail.com  
Phone: 0742 119 695  
Website: https://app.forbspace.com/

---

*"We inspire generations and the people of Africa through Research and Innovation to solve social and economic challenges using aeronautics and space technology."*

**- ForbSpace Mission Statement**
