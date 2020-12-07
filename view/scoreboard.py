
import tkinter as tk

class Scoreboard(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.robot_score_text = "Robot's score is: "
        self.user_score_text =  "User's score is:  "

        self.robot_score_label = tk.Label(self, text=self.robot_score_text + "0")
        self.user_score_label = tk.Label(self, text=self.user_score_text + "0")

        self.robot_score_label.grid(row=0, column=0)
        self.user_score_label.grid(row=1, column=0)
    
    def update(self, robot_score, user_score):
        self.robot_score_label["text"] = self.robot_score_text + str(robot_score)
        self.user_score_label["text"] = self.user_score_text + str(user_score)
