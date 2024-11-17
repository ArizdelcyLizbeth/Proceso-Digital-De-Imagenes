import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk
import letters

class App:
    """
    Clase principal para la interfaz grafica.
    Attributes:
        master (tk.Tk): Ventana principal.
        boton_cargar (tk.Button): Boton para cargar una imagen.
        boton_aplicar_filtro (tk.Button): Boton para aplicar el filtro a la imagen.
        boton_borrar_filtro (tk.Button): Boton para borrar el filtro aplicado.
        boton_guardar (tk.Button): Boton para guardar la imagen procesada.
        label_imagen (tk.Label): Label para mostrar la imagen cargada o procesada.
        imagen_original (PIL.Image): Imagen original cargada por el usuario.
        imagen_procesada (PIL.Image): Imagen despues de aplicar el filtro.
    """
    def __init__(self, master):
        """
        Inicializa la ventana principal y sus componentes.

        Args:
        master (tk.Tk): Ventana principal.
        """
        self.master = master
        master.title("Filtro de Letras")

        self.boton_cargar = tk.Button(master, text="Cargar Imagen", command=self.cargar_imagen)
        self.boton_cargar.pack()

        self.boton_aplicar_filtro = tk.Button(master, text="Aplicar Filtro", command=self.aplicar_filtro)
        self.boton_aplicar_filtro.pack()

        self.boton_borrar_filtro = tk.Button(master, text="Borrar Filtro", command=self.borrar_filtro)
        self.boton_borrar_filtro.pack()

        self.boton_guardar = tk.Button(master, text="Guardar Imagen", command=self.guardar_imagen)
        self.boton_guardar.pack()

        self.label_imagen = tk.Label(master)
        self.label_imagen.pack()

        self.imagen_original = None
        self.imagen_procesada = None

    def cargar_imagen(self):
        """
        Permite al usuario seleccionar una imagen.
        La imagen seleccionada se carga y se muestra en la interfaz.

        Llama a la función `mostrar_imagen` para mostrar la imagen cargada.
        """
        ruta = filedialog.askopenfilename()
        if ruta:
            self.imagen_original = Image.open(ruta)
            self.mostrar_imagen(self.imagen_original)

    def mostrar_imagen(self, imagen):
        """
        Muestra la imagen en la interfaz

        Args:
        imagen (PIL.Image): Imagen que se desea mostrar en la interfaz.
        """
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label_imagen.config(image=imagen_tk)
        self.label_imagen.image = imagen_tk

    def aplicar_filtro(self):
        """
        Aplica un filtro de letras a la imagen cargada.

        Solicita al usuario una letra para usar en el filtro mediante un cuadro de entrada.
        Si no se ha cargado una imagen, muestra un mensaje de error.
        """
        if self.imagen_original:
            letra = simpledialog.askstring("Entrada", "Coloca la letra con la que debe hacerse el filtro:")
            if letra:
                self.imagen_procesada = letters.aplicar_filtro(self.imagen_original, letra)
                self.mostrar_imagen(self.imagen_procesada)
        else:
            messagebox.showerror("Error", "No se ha cargado ninguna imagen.")

    def borrar_filtro(self):
        """
        Elimina el filtro aplicado y muestra la imagen original.

        Si no se ha cargado ninguna imagen, muestra un mensaje de error.
        """
        if self.imagen_original:
            self.mostrar_imagen(self.imagen_original)
            self.imagen_procesada = None
        else:
            messagebox.showerror("Error", "No se ha cargado ninguna imagen.")

    def guardar_imagen(self):
        """
        Guarda la imagen procesada en el sistema de archivos.

        Permite al usuario elegir la ubicación y el nombre del archivo para guardar la imagen procesada.
        Si no se ha procesado ninguna imagen, muestra un mensaje de error.
        """
        if self.imagen_procesada:
            ruta_guardado = filedialog.asksaveasfilename(defaultextension=".png",
                                                         filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if ruta_guardado:
                self.imagen_procesada.save(ruta_guardado)
                messagebox.showinfo("Éxito", "Imagen guardada correctamente.")
        else:
            messagebox.showerror("Error", "No hay una imagen procesada para guardar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
