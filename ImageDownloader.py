import tkinter as tk
from tkinter import Entry, Button, Label
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO
import threading

class NishantDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Nishant Image Dowloader")
        
        self.url_label = Label(root, text="Enter image url that you want to download")
        self.url_label.pack()    
        
        self.url_entry = Entry(root, width= 100)
        self.url_entry.pack()
        
        self.btn_download = Button(root, text="Save")
        self.btn_download.pack()
    
        self.image = Label(root, text="Saved Image:")
        self.image.pack()

        self.image_res = tk.Canvas(root, width=400, height=400)
        self.image_res.pack()
        
def main():
    root = tk.Tk()
    app = NishantDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()