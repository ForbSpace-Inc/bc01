# =============================================
# LESSON 05: If / Else
# =============================================

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult and can join!")
    
    # NESTED IF: A decision inside a decision
    is_student = input("Are you a student? (yes/no): ")
    if is_student == "yes":
        print("You get a student discount!")
        
elif age >= 13:
    # ELIF: short for "else if" - for more than two choices
    print("You are a teenager and can join!")
else:
    print("Sorry, you need to be 13 or older.")



# Inequality Symbols:
# >   Greater than
# <   Less than
# >=  Greater or equal
# <=  Less or equal
# ==  Exactly equal
# !=  Not equal





