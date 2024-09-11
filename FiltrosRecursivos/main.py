import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import filtros

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Imágenes recursivas")
        self.load_button = tk.Button(root, text="Cargar la Imagen", command=self.load_image)
        self.load_button.pack()
        self.grayscale_button = tk.Button(root, text="Aplicamos filtro gris", command=self.apply_grayscale_filter)
        self.grayscale_button.pack()
        self.color_button = tk.Button(root, text="Aplicamos filtro con color", command=self.apply_color_filter)
        self.color_button.pack()
        self.image_label = tk.Label(root)
        self.image_label.pack()
        self.image_path = None

    def load_image(self):
      
        self.image_path = filedialog.askopenfilename(filetypes=[("Imagen", "*.jpg;*.png")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((1000, 1000))
            self.img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.img_tk)

    def apply_grayscale_filter(self):
        if not self.image_path:
            messagebox.showwarning("Error", "Cargue la imagen.")
            return

        recursive_img_path = filtros.apply_grayscale_filter(self.image_path)
        self.display_image(recursive_img_path)

    def apply_color_filter(self):
        if not self.image_path:
            messagebox.showwarning("Error", "Cargue la imagen.")
            return

        recursive_img_path = filtros.apply_color_filter(self.image_path)
        self.display_image(recursive_img_path)

    def display_image(self, image_path):
        recursive_image_pil = Image.open(image_path)
        recursive_image_pil.thumbnail((100000, 100000))
        self.img_tk = ImageTk.PhotoImage(recursive_image_pil)
        self.image_label.config(image=self.img_tk)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
