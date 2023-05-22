import tkinter as tk
import pygame
import random


class MothersDayGame:
    def __init__(self, master):
        # Create and name the game window.
        self.master = master
        master.title("Mother's Day Game")
        self.score = 0
        # Load the background music.
        pygame.mixer.init()
        pygame.mixer.music.load("blue_danube.mp3")  # Replace with your music clip.
        pygame.mixer.music.play(-1)  # play the music in a loop.

        # Create a label for the game instructions.
        # the font parameter used when defining widgets is optional.
        # Visit https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
        # to see available fonts.
        self.instruction_text = tk.Label(master, text="Click on the Heart!", font=("Arial", 25))
        # Apply the widget onto the window.
        # The pady(y-axis) & padx(x-axis) parameters are optional. They show where to place the widget.
        self.instruction_text.pack(pady=10)

        # Create a button for the heart to be clicked.
        # the command parameter tells what the button does after being clicked.
        self.button = tk.Button(master, text="❤", font=("Arial", 50), command=self.increment_score)
        self.button.pack(pady=10)

        # Create a label for the score.
        # Use {} to represent a variable, at is stated in the format() and can be changed.
        self.score_label = tk.Label(master, text="Score: {}".format(self.score), font=("Arial", 15))
        self.score_label.pack(pady=10)

        # Create a timer.
        self.time_left = 30
        self.timer_label = tk.Label(master, text="Timer: {}".format(self.time_left), font=("Arial", 15))
        self.timer_label.pack(pady=10)
        # Call timer_function(). This decreases the time_left attribute each second.
        self.timer_function()

    def increment_score(self):    # This function increases score and randomizes heart position.
        self.score += 1      # Increase score.
        # Update the label text so the player can see the score increasing.
        self.score_label.configure(text="Score: {}".format(self.score))
        # Randomize heart position inside given range.
        self.button.place(x=random.randint(0, 500), y=random.randint(0, 500))

    def timer_function(self):   # This functions decreases the time and shows final message.
        if self.time_left > 0:    # If game is still running:
            self.time_left -= 1   # Decrease time.
            # Update label text so the player can see the time decreasing.
            self.timer_label.configure(text="Timer: {}".format(self.time_left))
            # Recursion (keep minimizing time_left) every second (1000 ms).
            self.master.after(1000, self.timer_function)
        else:     # If game ended:
            # Show some meaningful messages.
            self.instruction_text.configure(text="Game Over!", font=("Arial", 25))
            self.end = tk.Label(master, text="I love you, Mom!", font=("Arial", 15))
            self.end.pack(pady=10)
            # Show final score by changing text of score_label.
            self.score_label.configure(text="Final Score: {}".format(self.score), font=("Arial", 25))
            # Destroy (delete) heart button.
            self.button.destroy()


master = tk.Tk()    # similar to turtle.Turtle()
game = MothersDayGame(master)
master.mainloop()   # Prevents any code after this line from running until the player closes the window.
