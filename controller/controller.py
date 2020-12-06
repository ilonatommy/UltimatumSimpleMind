import tkinter as tk

from controller.decision_module import DecisionModule

class Controller():
    def __init__(self, root):
        self.dm = DecisionModule()
        self.infoHidden = False
        self.root = root

    def onInfo(self):
        if self.infoHidden:
            self.info.config(text="Zasady gry:\nTutaj znajdą sie zasady gry")
        else:
            self.info.config(text="")
        self.infoHidden = not self.infoHidden

    def onStart(self):
        self.dm.start_game()

    def onQuit(self):
        self.root.quit()


if __name__ == "__main__":
    c = Controller()
    print("Ok!")