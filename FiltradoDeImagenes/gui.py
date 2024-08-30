import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import filters

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter Application")
        self.image = None
        self.create_widgets()

    def create_widgets(self):
        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.filter_var = tk.StringVar(value="blur")
        self.filter_menu = tk.OptionMenu(self.root, self.filter_var, "blur", "motion_blur", "find_edges", "sharpen", "emboss", "average_blur")
        self.filter_menu.pack()

        self.apply_button = tk.Button(self.root, text="Apply Filter", command=self.apply_filter)
        self.apply_button.pack()

        self.save_button = tk.Button(self.root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def apply_filter(self):
        if self.image:
            filter_function = getattr(filters, f"{self.filter_var.get()}_image", None)
            if filter_function:
                filtered_image = filter_function(self.image)
                self.display_image(filtered_image)

    def save_image(self):
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                self.image.save(save_path)

    def display_image(self, img):
        self.image = img
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
