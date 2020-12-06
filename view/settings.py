class Settings():
    """ Contains application settings"""
    def __init__(self):
        """ Initialize application settings"""

        # Application window
        self.width = 1000
        self.height = 800 

        self.backgrouind_y_offset = 500
        self.backgrouind_x_offset = 400

        # Buttons
        self.button_width = 8
        self.button_hl_thic = 2
        self.button_active_bg = "#b5f1f7"
        self.button_hl_bg = "#b5f1f7"

if __name__ == "__main__":
    s = Settings()
    print("Ok!")