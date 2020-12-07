import tkinter as tk

from controller.controller import Controller
from view.assets import Assets
from view.top_bar import TopBar
from view.settings import Settings
from view.emotion_form import EmotionForm

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = Controller(self)

        self.settings = Settings()
        self.assets = Assets()

        self.canvas = tk.Canvas(self, 
            width=self.settings.width, 
            height=self.settings.height)

        self.top_bar = TopBar(self)
        self.emotion_form = EmotionForm(self)
        
        self.canvas.create_image(self.settings.backgrouind_y_offset, 
            self.settings.backgrouind_x_offset, 
            anchor="center",
            image=self.assets.background_image)
        self.canvas.pack()

        self.top_bar.place(x=0,y=30)

    def show_game_controls(self):
        self.emotion_form.place(x=10, y=300)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="bottom", fill="both", expand=True)
    root.mainloop()