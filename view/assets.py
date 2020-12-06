import os
from PIL import ImageTk, Image

class Assets:
    def __init__(self):
        self.assets_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                            '..', 'img'))
        self.background_image = self.get_image("pepper.jpg")

    def get_image(self, name):
        img_path = os.path.join(self.assets_path, name)
        img = Image.open(img_path)
        return ImageTk.PhotoImage(img)