import tkinter as tk
from tkinter import messagebox 

from controller.decision_module import DecisionModule

class Controller():
    def __init__(self, parent):
        self.dm = DecisionModule()
        self.infoHidden = False
        self.parent = parent

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
        self.parent.root.quit()

    def confirm_proposition(self, voice_emotion, face_emotion, offer_value):
        robot_answer = self.dm.humanOffer(offer_value, face_emotion, voice_emotion)
        user_answer = messagebox.askquestion("Robot has spoken!", 
            "He {} your offer! He offers you {} in return. Do you accept?"
                .format(robot_answer["decision"], robot_answer["offer"]))
        if user_answer == "yes":
            print("user accepted!")
        else:
            print("User denied")

if __name__ == "__main__":
    c = Controller()
    print("Ok!")