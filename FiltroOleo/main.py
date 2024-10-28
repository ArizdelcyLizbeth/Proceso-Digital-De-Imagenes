import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from filter import apply_oil_filter

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Filtro de Óleo")
        self.root.geometry("650x750")  
        self.root.configure(bg="#FFE4E1")  

        self.original_image = None
        self.filtered_image = None
        self.image_label = tk.Label(root, bg="#FFE4E1")  
        self.image_label.pack(pady=20)

        button_style = {
            "font": ("Comic Sans MS", 14, "bold"),  
            "bg": "#FFD1DC", 
            "fg": "#FF69B4",  
            "activebackground": "#FFB6C1",  
            "activeforeground": "#FFFFFF",  
            "width": 25,  
            "height": 3,  
            "relief": tk.RAISED,
            "bd": 4,
        }

        # Botones
        self.load_button = tk.Button(root, text="💖 Cargar Imagen 💖", command=self.load_image, **button_style)
        self.load_button.pack(pady=15)

        self.save_button = tk.Button(root, text="💾 Guardar Imagen 💾", command=self.save_image, **button_style)
        self.save_button.pack(pady=15)

        self.apply_button = tk.Button(root, text="🎨 Aplicar filtro de óleo 🎨", command=self.apply_filter, **button_style)
        self.apply_button.pack(pady=15)

        self.remove_button = tk.Button(root, text="❌ Quitar filtro ❌", command=self.remove_filter, **button_style)
        self.remove_button.pack(pady=15)

    def load_image(self):
        """Carga una imagen desde el sistema de archivos y la muestra en la interfaz."""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.bmp")])
        if file_path:
            self.original_image = Image.open(file_path).convert("L") 
            self.display_image(self.original_image)

    def save_image(self):
        """Guarda la imagen filtrada en el sistema de archivos."""
        if self.filtered_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("BMP files", "*.bmp")])
            if file_path:
                self.filtered_image.save(file_path)
                messagebox.showinfo("Guardar Imagen", "Imagen guardada correctamente. 😊")

    def apply_filter(self):
        """Aplica el filtro de óleo a la imagen original y la muestra en la interfaz."""
        if self.original_image:
            self.filtered_image = apply_oil_filter(self.original_image)
            self.display_image(self.filtered_image)

    def remove_filter(self):
        """Muestra la imagen original, eliminando el filtro aplicado."""
        if self.original_image:
            self.display_image(self.original_image)

    def display_image(self, image):
        """Ajusta el tamaño de la imagen y la muestra en el label de la interfaz."""
        resized_image = image.resize((500, 500), Image.LANCZOS)  
        self.image_label.image = ImageTk.PhotoImage(resized_image) 
        self.image_label.config(image=self.image_label.image)  

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()
