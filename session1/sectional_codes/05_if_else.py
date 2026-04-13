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
