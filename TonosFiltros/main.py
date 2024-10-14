import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import filters  

class HalftoneApp:
    """
    Constructor de la clase HalftoneApp. Inicializa la ventana principal y los elementos de la GUI.
    :param root: Objeto principal de tkinter (ventana).
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Filtros de Dithering y Semitonos")
        self.root.geometry("800x600")

        self.label = tk.Label(root, text="Carga una imagen para aplicar el filtro", font=("Arial", 14))
        self.label.pack(pady=20)

        self.load_button = tk.Button(root, text="Cargar Imagen", command=self.load_image)
        self.load_button.pack(pady=10)

        self.filter_buttons = tk.Frame(root)
        self.filter_buttons.pack(pady=20)

        tk.Button(self.filter_buttons, text="Dithering Aleatorio", command=lambda: self.apply_custom_filter("random")).grid(row=0, column=0, padx=20)
        tk.Button(self.filter_buttons, text="Dithering Ordenado", command=lambda: self.apply_custom_filter("ordered")).grid(row=1, column=0, padx=20)
        tk.Button(self.filter_buttons, text="Dithering Disperso", command=lambda: self.apply_custom_filter("dispersed")).grid(row=2, column=0, padx=20)
        tk.Button(self.filter_buttons, text="Floyd-Steinberg", command=lambda: self.apply_custom_filter("floyd")).grid(row=3, column=0, padx=20)
        tk.Button(self.filter_buttons, text="Semitonos", command=lambda: self.apply_custom_filter("halftone")).grid(row=4, column=0, padx=20)

        self.remove_filter_button = tk.Button(root, text="Quitar Filtro", command=self.remove_filter, state=tk.DISABLED)
        self.remove_filter_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Guardar Imagen", command=self.save_image)
        self.save_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(pady=20)

        self.image = None
        self.filtered_image = None
        self.original_image = None  

    def load_image(self):
        """
        Abre un cuadro de diálogo para que el usuario cargue una imagen.
        La imagen cargada se muestra en el canvas.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            try:
                self.image = Image.open(file_path)
                self.original_image = self.image.copy()  
                print(f"Imagen cargada: {file_path}")
                self.display_image(self.image)
                self.remove_filter_button.config(state=tk.NORMAL)  
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    def display_image(self, img):
        """
        Muestra una imagen en el canvas ajustada a 600x400 píxeles.
        :param img: Imagen a mostrar.
        """
        self.image_tk = ImageTk.PhotoImage(img.resize((600, 400)))
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def apply_custom_filter(self, filter_type):
        """
        Aplica un filtro de dithering o semitonos a la imagen cargada.
        :param filter_type: Tipo de filtro que se quiere aplicar.
        """
        if filter_type == "random":
            self.filtered_image = filters.random_dithering(self.image.copy())
        elif filter_type == "ordered":
            self.filtered_image = filters.ordered_dithering(self.image.copy())
        elif filter_type == "dispersed":
            self.filtered_image = filters.dispersed_dithering(self.image.copy())
        elif filter_type == "floyd":
            self.filtered_image = filters.floyd_steinberg_dithering(self.image.copy())
        elif filter_type == "halftone":
            self.filtered_image = filters.apply_halftone_filter(self.image.copy())

        self.display_image(self.filtered_image)
        self.remove_filter_button.config(state=tk.NORMAL) 

    def remove_filter(self):
        """
        Revertir la imagen a su estado original.
        """
        if self.original_image:
            self.display_image(self.original_image) 
            self.remove_filter_button.config(state=tk.DISABLED)  

    def save_image(self):
        """
        Abre un cuadro de diálogo para guardar la imagen con el filtro aplicado.
        """
        if self.filtered_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("Image files", "*.bmp;*.png;*.jpg")])
            if file_path:
                try:
                    self.filtered_image.save(file_path)
                    messagebox.showinfo("Éxito", "Imagen guardada correctamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar la imagen: {e}")
        else:
            messagebox.showerror("Error", "No hay imagen filtrada para guardar.")

root = tk.Tk()
app = HalftoneApp(root)
root.mainloop()
