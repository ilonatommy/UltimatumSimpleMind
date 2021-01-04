import tkinter as tk
from tkinter import messagebox

from controller.decision_module import DecisionModule


class Controller:
    def __init__(self, parent):
        self.dm = DecisionModule()
        self.infoHidden = False
        self.parent = parent

        self.user_score = 0
        self.robot_score = 0

    def onInfo(self):
        information = [
            "Ultimatum is turn-based game.",
            "As a player you will either propose a division of resources or evaluate the robot's offer.",
            "If accepted, parties get te agreed upon amount. In other cases, nobody receives anything.",
            "To aid our efforts, we also ask you to provide your emotions, which in the",
            "full version will be read via robot's camera and microphone"]
        messagebox.showinfo("Rules", " ".join(information))

    def onStart(self):
        self.dm.start_game()
        self.parent.show_game_controls()

    def onQuit(self):
        self.parent.parent.quit()

    def confirm_proposition(self, voice_emotion, face_emotion, offer_value):
        robot_answer = self.dm.humanOffer(offer_value, face_emotion, voice_emotion)

        if robot_answer["decision"] == "accepted":
            print("robot accepted!")
            self.robot_score += int(offer_value)
            self.user_score += 10 - int(offer_value)
            self.update_score()
        else:
            print("robot declined")

        user_answer = messagebox.askquestion("Robot has spoken!",
                                             "He {} your offer! He offers you {}. Do you accept?"
                                             .format(robot_answer["decision"], robot_answer["offer"]))
        if user_answer == "yes":
            print("user accepted!")
            self.user_score += robot_answer["offer"]
            self.robot_score += 10 - robot_answer["offer"]
            self.update_score()
        else:
            print("User declined")

    def update_score(self):
        self.parent.scoreboard.update(self.robot_score, self.user_score)


if __name__ == "__main__":
    c = Controller()
    print("Ok!")
