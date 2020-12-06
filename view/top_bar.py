import tkinter as tk


class TopBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # Create
        self.start_button = self.__createTopBarButton("START", self.parent.controller.onStart)
        self.info_button = self.__createTopBarButton("INFO", self.parent.controller.onInfo)
        self.quit_button = self.__createTopBarButton("QUIT", self.parent.controller.onQuit)

        # Position
        self.start_button.grid(row=1, column=0)
        self.info_button.grid(row=1, column=1)
        self.quit_button.grid(row=1, column=2)

    def __createTopBarButton(self, label, command):
        button = tk.Button(self, text=label, command=command,
            width=self.parent.settings.button_width, 
            activebackground=self.parent.settings.button_active_bg,
            highlightbackground=self.parent.settings.button_hl_bg, 
            highlightthickness=self.parent.settings.button_hl_thic)

        return button


