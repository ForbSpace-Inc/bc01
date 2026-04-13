# =============================================
# BONUS PROJECT: Smart Greeting Program
# =============================================

# 1. Ask name and age
name = input("What is your name? ")
age = int(input("How old are you? "))

# 2. Greet the user
print("Hello", name + "!")

# 3. Check if they are an adult
if age >= 18:
    print("You are an adult! Welcome to the advanced section.")
else:
    print("You are still young and full of potential!")

# 4. Print name 3 times
print("Let's repeat your name:")
for i in range(3):
    print(name)

# =====================
# CHALLENGE
# =====================
# Can you make the loop print your name 5 times instead?