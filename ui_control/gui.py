import os
from tkinter import Tk, Canvas, PhotoImage, mainloop, NW, Label, Frame, Button, LEFT
from PIL import ImageTk, Image

IMG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'img'))


def fixWindowSize(tk):
    tk.geometry('{}x{}'.format(1000, 800))
    tk.resizable(False, False)
    return tk


def getBackgroundImg(tk):
    img = Image.open(os.path.join(IMG_PATH, "pepper.jpg"))
    backgroundImage = ImageTk.PhotoImage(img)
    return backgroundImage


tk = Tk()
tk = fixWindowSize(tk)
img = Image.open(os.path.join(IMG_PATH, "pepper.jpg"))
backgroundImage = getBackgroundImg(tk)
backgroundLabel = Label(tk, image=backgroundImage)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
tk.mainloop()
