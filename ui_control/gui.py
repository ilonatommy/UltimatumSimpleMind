#!/usr/bin/env python

import os
from tkinter import Tk, Canvas, PhotoImage, mainloop, NW, Label, Frame, Button, LEFT
from PIL import ImageTk, Image

from decision_module import DecisionModule

IMG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'img'))
WIDTH = 1000
HEIGHT = 800
BUTTON_FRAME_THICKNESS = 2
BUTTON_WIDTH = 8
BACKGROUND_Y_OFFSET = 500
BACKGROUND_X_OFFSET = 400


def getBackgroundImg():
    img = Image.open(os.path.join(IMG_PATH, "pepper.jpg"))
    backgroundImage = ImageTk.PhotoImage(img)
    return backgroundImage


class Gui:
    def __init__(self, tk):
        tk.title("Pepper Ultimatum Game")
        self.tk = tk
        self.canvas = Canvas(self.tk, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.backgroundImg = getBackgroundImg()

        self.dm = DecisionModule()

        self.info = Label(self.tk, text="", background="#FFF")
        start_button_window = self.canvas.create_window(100, 100, anchor='nw',
                                                        window=self.info)

        self.infoHidden = True
        self.startHidden = True

    def fixWindowSize(self, ):
        self.tk.geometry('{}x{}'.format(WIDTH, HEIGHT))
        self.tk.resizable(False, False)

    def setBasicButtons(self):
        yOffset = 15
        xOffset = 10
        quit_button = Button(self.tk, text="QUIT", command=self.tk.quit, anchor='n',
                             width=BUTTON_WIDTH, activebackground="#b5f1f7",
                             highlightbackground="#b5f1f7", highlightthickness=BUTTON_FRAME_THICKNESS)
        quit_button_window = self.canvas.create_window(xOffset, yOffset, anchor='nw', window=quit_button)

        start_button = Button(self.tk, text="START", command=self.dm.start_game, anchor='n',
                              width=BUTTON_WIDTH, activebackground="#b5f1f7",
                              highlightbackground="#b5f1f7", highlightthickness=BUTTON_FRAME_THICKNESS)
        start_button_window = self.canvas.create_window(xOffset * 3 + BUTTON_WIDTH * 10, yOffset, anchor='nw',
                                                        window=start_button)

        start_button = Button(self.tk, text="INFO", command=self.onInfo, anchor='n',
                              width=BUTTON_WIDTH, activebackground="#b5f1f7",
                              highlightbackground="#b5f1f7", highlightthickness=BUTTON_FRAME_THICKNESS)
        start_button_window = self.canvas.create_window(xOffset * 5 + 2 * BUTTON_WIDTH * 10, yOffset, anchor='nw',
                                                        window=start_button)

    def onInfo(self):
        if self.infoHidden:
            self.info.config(text="Zasady gry:\nTutaj znajdą sie zasady gry")
        else:
            self.info.config(text="")
        self.infoHidden = not self.infoHidden

    def onStart(self):
        # TODO: stworzyć przyciski dla wejsciowych emocji + toggle dla przyciskania START
        quit_button = Button(tk, text="EMOTION", command=self.tk.quit, anchor='n',
                             width=BUTTON_WIDTH, activebackground="#b5f1f7",
                             highlightbackground="#b5f1f7", highlightthickness=BUTTON_FRAME_THICKNESS)
        quit_button_window = self.canvas.create_window(100, 10, anchor='nw', window=quit_button)


tk = Tk()
gui = Gui(tk)
gui.fixWindowSize()
gui.canvas.create_image(BACKGROUND_Y_OFFSET, BACKGROUND_X_OFFSET, image=gui.backgroundImg)
gui.setBasicButtons()
tk.mainloop()
