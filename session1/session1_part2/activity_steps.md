# 🕹️ Activity: Build Your Mars Rover Game

Follow these steps to create your Exploration Game. Each section adds a new feature to your mission!

## 🏁 Step 1: Setup
1.  **Open Scratch**: Go to the [Scratch Editor](https://scratch.mit.edu/projects/1296183150/editor).
2.  **Upload Backdrop**: Hover over "Choose a Backdrop" (Stage window) and select **Upload Backdrop**. Choose a Mars surface image.
3.  **Upload Sprite**: Hover over "Choose a Sprite" (Sprite window) and select **Upload Sprite**. Upload the Rover image.
4.  **Cleanup**: Delete the default Scratch Cat sprite.

## 🏎️ Step 2: Rover Controls
We want the Rover to move when we press the arrow keys. 
1.  Use the `When [key] pressed` block (under **Events**).
2.  Snap a `Point in direction` and `Move 10 steps` block (under **Motion**) to it.
3.  Repeat for Up, Down, Left, and Right!

## 🌟 Step 3: Science Targets
NASA rovers search for "Science Targets".
1.  Add a new sprite (like a **Star**).
2.  Create a script: `When Green Flag Clicked`, `Forever` check `If touching [Rover]` then `Hide`.
3.  **Don't forget**: Add a `Show` block at the very start so the Star returns when you restart the game!

## ⏲️ Step 4: Mission Timer
Missions have limited energy!
1.  Under **Variables**, click **Make a Variable** and name it `Timer`.
2.  Create a script to `Set Timer to 30`.
3.  Use a Loop to `Wait 1 seconds` and `Change Timer by -1`.
4.  If `Timer = 0`, then `Stop All`.

---

> [!CHECKLIST]
> ### 👩‍🚀 Mission Debrief
> - Does your rover move in all four directions?
> - Does the score increase or the target hide when you reach it?
> - Does the timer count down correctly?
> - **Bonus**: Can you add a second "Science Target"?
