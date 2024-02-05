import tkinter as tk
from tkinter import Entry, Button, Label
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO
import threading
import os


class NishantDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Nishant Image Dowloader")
        
        self.url = Label(root, text="Enter image url that you want to download")
        self.url.pack()    
        
        self.url_bar = Entry(root, width= 100)
        self.url_bar.pack()
        
        self.btn_download = Button(root, text="Save", command = self.download_image)
        self.btn_download.pack()
    
        self.image = Label(root, text="Saved Image:")
        self.image.pack()

        self.image_res = tk.Canvas(root, width=400, height=400)
        self.image_res.pack()
        
    def download_image(self):
        url = self.url_bar.get()
        if url:
            #thread for saving image
            save_thread = threading.Thread(target=self.save_image, args=(url, ))
            save_thread.start()
            
    def save_image(self, url):
        try:
            response = urlopen(url)
            image_data = BytesIO(response.read())
            image = Image.open(image_data)
            image.thumbnail((400,400))
            
            save_path = os.path.join(os.getcwd(),"untitled_image.jpg")
            image.save(save_path)
            
            self.root.after(0, self.update_image, image)
            
        except Exception as ex:
            print("Unable to download image: {ex}")
        
    def update_image(self, image):
        tk_img = ImageTk.PhotoImage(image)
        
        self.image_res.config(width=tk_img.width(), height= tk_img.height())
        self.image_res.create_image(0,0, anchor = tk.NW, image = tk_img)
        self.image_res = tk_img    
    
    
def main():
    root = tk.Tk()
    app = NishantDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()