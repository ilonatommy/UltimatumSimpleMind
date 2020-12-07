import tkinter as tk
from tkinter import StringVar


class EmotionForm(tk.Widget):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # setup comboboxes
        self.voice_label = tk.Label(self, text="Choose emotion in voice:")
        self.voiceEmotions = ["calm", "angry", "fearful", "happy", "sad"]
        self.voice_options = StringVar(self)
        self.voice_options.set(self.voiceEmotions[0])
        self.voice_menu = tk.OptionMenu(self, self.voice_options, *self.voiceEmotions)

        self.face_label = tk.Label(self, text="Choose emotion in facial expression:")
        self.faceEmotions = ["calm", "angry", "fearful", "happy", "sad", "surprised",  "disgusted"]
        self.face_options = StringVar(self)
        self.face_options.set(self.faceEmotions[0])
        self.face_menu = tk.OptionMenu(self, self.face_options, *self.faceEmotions)

        self.offer_label = tk.Label(self, text="Choose amount of money you offer:")
        self.offers = list(range(1, 10))
        self.offer_options = StringVar(self)
        self.offer_options.set(self.offers[4])
        self.offer_menu = tk.OptionMenu(self, self.offer_options, *self.offers)

        self.confirmation_button = tk.Button(self, text="CONFIRM", 
            command=self.onConfirmClicked,
            width=self.parent.settings.button_width, 
            activebackground=self.parent.settings.button_active_bg,
            highlightbackground=self.parent.settings.button_hl_bg, 
            highlightthickness=self.parent.settings.button_hl_thic)

        self.voice_label.grid(row=0, column=0)
        self.voice_menu.grid(row=1, column=0)

        self.face_label.grid(row=2, column=0)
        self.face_menu.grid(row=3, column=0)

        self.offer_label.grid(row=4, column=0)
        self.offer_menu.grid(row=5, column=0)

        self.confirmation_button.grid(row=6, column=0)

    def onConfirmClicked(self):
        voice_emotion = self.voice_options.get()
        face_emotion = self.face_options.get()
        offer_value = self.offer_options.get()
        self.parent.controller.confirm_proposition(voice_emotion,
            face_emotion, offer_value)

        
