import tkinter as tk
from PIL import Image, ImageTk
import os


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.img = Image.open(os.path.join('app','bola.webp'))
        self.imgtk = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(image=self.imgtk)
        self.label.pack()

        self.button = tk.Button(text="Filtro", command=self.update_img)
        self.button.pack()

    def update_img(self):
        img = Image.eval(self.img, lambda x: 255 - x)
        self.imgtk = ImageTk.PhotoImage(img)
        self.label.configure(image=self.imgtk)

if __name__ == '__main__':
    app = App()
    app.mainloop()