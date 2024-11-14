import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import filters  

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escalar Imágenes")
        self.root.config(bg="#F7D1D1")  

        # Imagen original y modificada
        self.original_image = None
        self.modified_image = None
        self.filter_applied = False  
        self.last_filter = None  # Rastreo del último filtro aplicado

        self.create_widgets()

    def create_widgets(self):
        button_style = {
            "font": ("Arial", 12, "bold"),
            "bg": "#F8A9C9",  
            "fg": "#ffffff",  
            "activebackground": "#F5B4D4", 
            "relief": "flat",
            "width": 20,
            "height": 2,
            "bd": 0,
            "highlightthickness": 0
        }

        self.load_button = tk.Button(self.root, text="Cargar Imagen", command=self.load_image, **button_style)
        self.load_button.pack(pady=15)

        self.scale_up_button = tk.Button(self.root, text="Escalar Hacia Arriba", command=self.scale_up, **button_style)
        self.scale_up_button.pack(pady=5)

        self.scale_down_button = tk.Button(self.root, text="Escalar Hacia Abajo", command=self.scale_down, **button_style)
        self.scale_down_button.pack(pady=5)

        self.reset_button = tk.Button(self.root, text="Borrar Filtro", command=self.reset_filter, **button_style)
        self.reset_button.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Guardar Imagen", command=self.save_image, **button_style)
        self.save_button.pack(pady=5)

        self.image_label = tk.Label(self.root, bg="#F7D1D1")
        self.image_label.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.modified_image = self.original_image.copy()
            self.filter_applied = False  # Reiniciar estado de filtro
            self.last_filter = None  # Reiniciar filtro aplicado
            self.display_image(self.modified_image)

    def scale_up(self):
        if self.can_apply_filter("scale_up"):
            if self.modified_image:
                numpy_image = filters.pil_to_numpy(self.modified_image)
                self.modified_image = filters.escala_hacia_arriba(numpy_image, 1.5)
                self.modified_image = filters.numpy_to_pil(self.modified_image)
                self.filter_applied = True
                self.last_filter = "scale_up"  # Marcar el último filtro aplicado
                self.display_image(self.modified_image)
            else:
                messagebox.showerror("Error", "Primero carga una imagen.")

    def scale_down(self):
        if self.can_apply_filter("scale_down"):
            if self.modified_image:
                numpy_image = filters.pil_to_numpy(self.modified_image)
                self.modified_image = filters.escala_hacia_abajo(numpy_image, 2)
                self.modified_image = filters.numpy_to_pil(self.modified_image)
                self.filter_applied = True
                self.last_filter = "scale_down"  # Marcar el último filtro aplicado
                self.display_image(self.modified_image)
            else:
                messagebox.showerror("Error", "Primero carga una imagen.")

    def can_apply_filter(self, current_filter):
        """ Verifica si se puede aplicar el filtro actual """
        if not self.filter_applied or self.last_filter == current_filter:
            return True
        else:
            messagebox.showwarning("Advertencia", "Primero borra el filtro anterior antes de aplicar uno diferente.")
            return False

    def reset_filter(self):
        if self.original_image:
            self.modified_image = self.original_image.copy()
            self.filter_applied = False  # Reiniciar estado de filtro
            self.last_filter = None  # Reiniciar filtro aplicado
            self.display_image(self.modified_image)
        else:
            messagebox.showerror("Error", "Primero carga una imagen.")

    def save_image(self):
        if self.modified_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if save_path:
                self.modified_image.save(save_path)
        else:
            messagebox.showerror("Error", "No hay imagen para guardar.")

    def display_image(self, image):
        image_tk = ImageTk.PhotoImage(image)
        self.image_label.config(image=image_tk)
        self.image_label.image = image_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
