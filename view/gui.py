#!/usr/bin/env python

import os
from tkinter import Tk, Canvas, PhotoImage, mainloop, NW, Label, Frame, Button, LEFT, Text, OptionMenu, StringVar
from PIL import ImageTk, Image

from controller.decision_module import DecisionModule

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
        self.voiceEmotions = ["calm", "angry", "fearful", "happy", "sad"]
        self.voice_options = StringVar(self.tk)
        self.voice_options.set(self.voiceEmotions[0])

        self.faceEmotions = ["calm", "angry", "fearful", "happy", "sad", "surprised",  "disgusted"]
        self.face_options = StringVar(self.tk)
        self.face_options.set(self.faceEmotions[0])

        self.offers = list(range(1, 10))
        self.offer_options = StringVar(self.tk)
        self.offer_options.set(self.offers[4])

        self.decisions = ["yes", "no"]
        self.decision_options = StringVar(self.tk)
        self.decision_options.set(self.decisions[0])

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

        start_button = Button(self.tk, text="START", command=self.onStart, anchor='n',
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
        self.dm.start_game()
        self.onNextRound()

    def onConfirmOffer(self):
        emotion_face = self.face_options.get()
        emotion_voice = self.voice_options.get()
        offer = self.offer_options.get()
        robot_offer, robot_decision = self.dm.humanOffer(offer, emotion_face, emotion_voice)
        if robot_decision == "yes":
            decision_text = "I accept your offer!"
        else:
            decision_text = "I decline your offer! We both get nothing."
        label_robot_decision = Label(self.tk, text=decision_text)
        label_decision_window = self.canvas.create_window(700, 80, anchor='nw', window=label_robot_decision)

        label_robot_offer = Label(self.tk, text="I offer you " + str(robot_offer) + ".\nAre you accepting?")
        label_offer_window = self.canvas.create_window(700, 180, anchor='nw', window=label_robot_offer)

        decision = OptionMenu(self.tk, self.decision_options, *self.decisions)
        decision_window = self.canvas.create_window(700, 220, anchor='nw', window=decision)

        confirm_decision_button = Button(self.tk, text="CONFIRM", command=self.onConfirmDecision, anchor='n',
                              width=BUTTON_WIDTH, activebackground="#b5f1f7",
                              highlightbackground="#b5f1f7", highlightthickness=BUTTON_FRAME_THICKNESS)
        confirm_decision_button_window = self.canvas.create_window(700, 280, anchor='nw', window=confirm_decision_button)

    def onConfirmDecision(self):
        human_decision = self.decision_options.get()
        if human_decision == "yes":
            after_round_text = "Perfect! You get offered money!"
        else:
            after_round_text = "You both get nothing!"
        label_after_round = Label(self.tk, text=after_round_text)
        label_after_round_window = self.canvas.create_window(700, 300, anchor='nw', window=label_after_round)

        next_round_button = Button(self.tk, text="NEXT ROUND", command=self.onNextRound, anchor='n',
                                         width=BUTTON_WIDTH, activebackground="#b5f1f7",
                                         highlightbackground="#b5f1f7", highlightthickness=BUTTON_FRAME_THICKNESS)
        next_round_button_window = self.canvas.create_window(700, 400, anchor='nw',
                                                                   window=next_round_button)

    def onNextRound(self):
        label_voice = Label(self.tk, text="Choose emotion in voice:")
        label_voice_window = self.canvas.create_window(50, 80, anchor='nw', window=label_voice)
        choice_voice = OptionMenu(self.tk, self.voice_options, *self.voiceEmotions)
        voice_window = self.canvas.create_window(50, 100, anchor='nw', window=choice_voice)

        label_face = Label(self.tk, text="Choose emotion in facial expression:")
        label_face_window = self.canvas.create_window(50, 180, anchor='nw', window=label_face)
        choice_face = OptionMenu(self.tk, self.face_options, *self.faceEmotions)
        face_window = self.canvas.create_window(50, 200, anchor='nw', window=choice_face)

        label_offer = Label(self.tk, text="Choose amount of money you offer:")
        label_offer_window = self.canvas.create_window(50, 280, anchor='nw', window=label_offer)
        choice_offer = OptionMenu(self.tk, self.offer_options, *self.offers)
        face_window = self.canvas.create_window(50, 300, anchor='nw', window=choice_offer)

        confirm_offer_button = Button(self.tk, text="CONFIRM", command=self.onConfirmOffer, anchor='n',
                                      width=BUTTON_WIDTH, activebackground="#b5f1f7",
                                      highlightbackground="#b5f1f7", highlightthickness=BUTTON_FRAME_THICKNESS)
        confirm_offer_button_window = self.canvas.create_window(50, 400, anchor='nw', window=confirm_offer_button)


tk = Tk()
gui = Gui(tk)
gui.fixWindowSize()
gui.canvas.create_image(BACKGROUND_Y_OFFSET, BACKGROUND_X_OFFSET, image=gui.backgroundImg)
gui.setBasicButtons()
tk.mainloop()
