import tkinter as tk
from tkinter import filedialog, Label
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import cv2
from filters import aplicar_filtro_maximo, aplicar_filtro_minimo

class TinderKatApp:
    """
    Permite cargar una imagen y aplicar filtros de máximo y mínimo.
    Métodos:
        __init__(root): Inicializa la interfaz.
        cargar_imagen(): Permite al usuario cargar una imagen.
        filtro_maximo(): Aplica un filtro máximo a la imagen cargada y la muestra.
        filtro_minimo(): Aplica un filtro mínimo a la imagen cargada y la muestra.
        quitar_filtro(): Restaura la imagen original sin filtros.
        guardar_imagen(): Guarda la imagen.
        mostrar_imagen(imagen): Muestra la imagen proporcionada en la etiqueta de la interfaz.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Filtros Máximos y Mínimos 🌸")
        self.root.geometry("600x700") 

        self.root.set_theme("breeze")  

        self.imagen_original = None
        self.imagen_actual = None

        marco_botones = ttk.Frame(root, padding=20)
        marco_botones.pack(pady=10)

        botones_info = [
            ("Cargar imagen 📷", self.cargar_imagen),
            ("Filtro de máximos 🌟", self.filtro_maximo),
            ("Filtro de mínimos 🌷", self.filtro_minimo),
            ("Quitar filtro ❌", self.quitar_filtro),
            ("Guardar imagen 💾", self.guardar_imagen),
        ]

        for texto, comando in botones_info:
            boton = ttk.Button(
                marco_botones,
                text=texto,
                command=comando,
                style="TButton"
            )
            boton.pack(pady=5, ipadx=5, ipady=5, fill='x')

        self.label_imagen = Label(root, bg="#fdf7f2")
        self.label_imagen.pack(pady=10)

    def cargar_imagen(self):
        ruta_imagen = filedialog.askopenfilename()
        if ruta_imagen:
            self.imagen_original = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
            self.imagen_actual = self.imagen_original.copy()
            self.mostrar_imagen(self.imagen_actual)

    def filtro_maximo(self):
        if self.imagen_actual is not None:
            self.imagen_actual = aplicar_filtro_maximo(self.imagen_actual)
            self.mostrar_imagen(self.imagen_actual)

    def filtro_minimo(self):
        if self.imagen_actual is not None:
            self.imagen_actual = aplicar_filtro_minimo(self.imagen_actual)
            self.mostrar_imagen(self.imagen_actual)

    def quitar_filtro(self):
        if self.imagen_original is not None:
            self.imagen_actual = self.imagen_original.copy()
            self.mostrar_imagen(self.imagen_actual)

    def guardar_imagen(self):
        if self.imagen_actual is not None:
            ruta_guardado = filedialog.asksaveasfilename(defaultextension=".png",
                                                         filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if ruta_guardado:
                cv2.imwrite(ruta_guardado, self.imagen_actual)

    def mostrar_imagen(self, imagen):
        imagen_pil = Image.fromarray(imagen)
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
        self.label_imagen.config(image=imagen_tk)
        self.label_imagen.image = imagen_tk

if __name__ == "__main__":
    root = ThemedTk(theme="breeze")
    app = TinderKatApp(root)
    root.mainloop()
