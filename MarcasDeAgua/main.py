import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Toplevel, Label
from PIL import Image, ImageTk
from watermark import add_watermark

class WatermarkApp:
    """
    Permite a los usuarios cargar una imagen,
    añadir una marca de agua de texto, y guardar la imagen resultante.
    """
    def __init__(self, root):
        """
        Inicializa la interfaz de usuario 
        Args:
            root (Tk): Ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Aplicación de marca de agua")

        self.label = tk.Label(root, text="Introduzca el texto de la marca de agua:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root)
        self.text_entry.pack(pady=5)

        self.upload_button = tk.Button(root, text="Subir imagen", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.add_watermark_button = tk.Button(root, text="Añadir marca de agua", command=self.add_watermark)
        self.add_watermark_button.pack(pady=10)

        self.image_path = None
        self.watermarked_image = None

    def upload_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            print("Imagen cargada:", self.image_path)

    def add_watermark(self):
        if not self.image_path:
            messagebox.showerror("Error", "Por favor, cargue una imagen primero.")
            return

        watermark_text = self.text_entry.get()
        if not watermark_text:
            messagebox.showerror("Error", "Introduzca el texto de la marca de agua.")
            return

        # Mostrar la imagen con la marca de agua en una ventana
        self.show_image_with_watermark(watermark_text)

    def show_image_with_watermark(self, watermark_text):
        # Agregar la marca de agua y obtener la imagen resultante
        watermarked_image = add_watermark(self.image_path, watermark_text)

        # Crear una ventana para mostrar la imagen
        top = Toplevel(self.root)
        top.title("Imagen con marca de agua")

        # Convertir la imagen de Pillow a formato que Tkinter puede mostrar
        photo = ImageTk.PhotoImage(watermarked_image)

        label = Label(top, image=photo)
        label.image = photo  # Mantener una referencia para evitar que la imagen sea recolectada por el GC
        label.pack()

        # Agregar botón para guardar la imagen
        save_button = tk.Button(top, text="Salvar Imagen", command=lambda: self.save_image(watermarked_image))
        save_button.pack(pady=10)

    def save_image(self, image):
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if output_path:
            image.save(output_path)
            messagebox.showinfo("Éxito", "Imagen guardada exitosamente.")

root = tk.Tk()
app = WatermarkApp(root)
root.mainloop()
