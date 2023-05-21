import tkinter as tk
import pygame
import random


class MothersDayGame:
    def __init__(self, master):
        self.master = master
        master.title("Mother's Day Game")
        self.score = 0
        pygame.mixer.init()
        pygame.mixer.music.load("blue_danube.mp3")
        pygame.mixer.music.play(-1)

        self.instruction_text = tk.Label(master, text="Click on the Heart!", font=("Arial", 25))
        self.instruction_text.pack(pady=10)

        self.button = tk.Button(master, text="❤", font=("Arial", 50), command=self.increment_score)
        self.button.pack(pady=10)

        self.score_label = tk.Label(master, text="Score: {}".format(self.score), font=("Arial", 15))
        self.score_label.pack(pady=10)

        self.time_left = 30
        self.timer_label = tk.Label(master, text="Timer: {}".format(self.time_left), font=("Arial", 15))
        self.timer_label.pack(pady=10)
        self.timer_function()

    def increment_score(self):
        self.score += 1
        self.score_label.configure(text="Score: {}".format(self.score))
        self.button.place(x=random.randint(0, 500), y=random.randint(0, 500))

    def timer_function(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text="Timer: {}".format(self.time_left))
            self.master.after(1000, self.timer_function)
        else:
            self.instruction_text.configure(text="Game Over!", font=("Arial", 25))
            self.score_label.configure(text="Final Score: {}".format(self.score), font=("Arial", 25))
            self.button.destroy()


master = tk.Tk()
game = MothersDayGame(master)
master.mainloop()
