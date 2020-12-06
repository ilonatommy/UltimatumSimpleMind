import tkinter as tk

from controller.controller import Controller
from view.assets import Assets
from view.top_bar import TopBar
from view.settings import Settings

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = Controller(parent)

        self.settings = Settings()
        self.assets = Assets()

        self.canvas = tk.Canvas(self, width=self.settings.width, 
            height=self.settings.height)
        self.top_bar = TopBar(self)
        
        self.top_bar.pack(side="top", fill="x", expand=True)

        self.canvas.pack()
        self.canvas.create_image(self.settings.backgrouind_y_offset, 
            self.settings.backgrouind_x_offset, 
            image=self.assets.background_image)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="bottom", fill="both", expand=True)
    root.mainloop()