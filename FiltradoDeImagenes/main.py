import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import filters

class ImageFilterApp:
    """
    Aplicación de GUI para aplicar filtros a imágenes utilizando Tkinter.
    Permite subir una imagen, aplicar diferentes filtros, restaurar la imagen original y guardar la imagen filtrada.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Filtros de Imagen")
        self.root.configure(bg="#ffe6f2")  
        self.upload_button = tk.Button(root, text="Subir Imagen", command=self.upload_image,
                                       bg="#ff99cc", fg="white", font=("Helvetica", 12, "bold"),
                                       activebackground="#ff66b2", activeforeground="white")
        self.upload_button.pack(pady=10)
        self.filter_var = tk.StringVar(value="blur")
        self.filter_menu = tk.OptionMenu(root, self.filter_var, "blur", "motion_blur", "find_edges", "sharpen", "emboss", "promedio")
        self.filter_menu.config(bg="#ff66b2", fg="white", font=("Helvetica", 12),
                                activebackground="#ff99cc", activeforeground="white")
        self.filter_menu.pack(pady=10)
        self.apply_button = tk.Button(root, text="Aplicar Filtro", command=self.apply_filter,
                                      bg="#ff6699", fg="white", font=("Helvetica", 12, "bold"),
                                      activebackground="#ff3385", activeforeground="white")
        self.apply_button.pack(pady=10)
        self.restore_button = tk.Button(root, text="Restaurar Imagen", command=self.restore_image,
                                        bg="#ff99cc", fg="white", font=("Helvetica", 12, "bold"),
                                        activebackground="#ff66b2", activeforeground="white")
        self.restore_button.pack(pady=10)
        self.save_button = tk.Button(root, text="Guardar Imagen", command=self.save_image,
                                     bg="#ff66b2", fg="white", font=("Helvetica", 12, "bold"),
                                     activebackground="#ff3385", activeforeground="white")
        self.save_button.pack(pady=10)
        
        self.img = None
        self.img_array = None
        self.original_img = None
        self.img_label = tk.Label(self.root, bg="#ffe6f2", relief="sunken", bd=2)
        self.img_label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.img = Image.open(file_path)
            self.img_array = np.array(self.img)
            self.original_img = self.img.copy()
            self.display_image(self.img)
    
    def display_image(self, img):
        img_tk = ImageTk.PhotoImage(img)
        self.img_label.config(image=img_tk)
        self.img_label.image = img_tk

    def apply_filter(self):
        if self.img_array is None:
            messagebox.showerror("Error", "No hay imagen cargada")
            return
        
        filter_name = self.filter_var.get()
        filter_func = getattr(filters, filter_name, None)
        if filter_func:
            filtered_array = filter_func(self.img_array)
            self.img = Image.fromarray(filtered_array)
            self.display_image(self.img)
        else:
            messagebox.showerror("Error", "Filtro no encontrado")

    def restore_image(self):
        if self.original_img is None:
            messagebox.showerror("Error", "No hay imagen original para restaurar")
            return
        
        self.img = self.original_img.copy()
        self.img_array = np.array(self.img)
        self.display_image(self.img)

    def save_image(self):
        if self.img is None:
            messagebox.showerror("Error", "No hay imagen para guardar")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            self.img.save(file_path)

def main():
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()