# 🧠 Quick Recap: Python Loops & Transition

Before we dive into the Martian world of Scratch, let's take a moment to "wind up" what we learned yesterday about **Loops** and see how they translate to our new visual environment.

## 🌀 Yesterday's Mastery: Loops
In Python, we used loops to repeat actions without writing the same code over and over.

### 1. The `for` Loop
Used when we know *exactly* how many times we want to repeat.
```python
# Repeat 5 times
for i in range(5):
    print("Driving the rover...")
```

### 2. The `while` Loop
Used when we want to repeat *as long as* a condition is true.
```python
battery = 100
while battery > 0:
    print("Rover is exploring!")
    battery = battery - 1
```

---

## 🚀 Transitioning to Scratch
Scratch uses the exact same logic, but instead of typing, you snap **Blocks** together!

| Python Concept | Scratch Block | Description |
| :--- | :--- | :--- |
| `for i in range(10):` | **Repeat (10)** | Repeats the code inside a specific number of times. |
| `while True:` | **Forever** | Keeps the code running as long as the game is active. |
| `if battery < 10:` | **If <...>** | Runs the code only if the "sensing" condition is met. |

---

### 🏁 Today's Bridge
In today's project, we will use these concepts to:
1.  **Repeat** the rover movement check forever.
2.  **If** the rover touches a hazard, then reduce the score (Logic!).
3.  **Wait** until a specific discovery is made.

> [!TIP]
> **From Code to Blocks**: The logic is the same, only the "language" has changed. Let's see how much faster we can build with visual blocks!
