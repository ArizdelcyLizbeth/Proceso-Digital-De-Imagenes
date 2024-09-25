import tkinter as tk
from tkinter import filedialog
from PIL import Image

def load_bmp(filename):
    """Cargar los datos de un archivo BMP."""
    with open(filename, 'rb') as f:
        return f.read()

def save_bmp(filename, bmp_data):
    """Guardar los datos en un archivo BMP."""
    with open(filename, 'wb') as f:
        f.write(bmp_data)

def remove_watermark(bmp_data):
    """Eliminar la marca de agua de los datos BMP."""
    header_size = 54
    pixels = bytearray(bmp_data[header_size:])

    width = int.from_bytes(bmp_data[18:22], 'little')
    height = int.from_bytes(bmp_data[22:26], 'little')

    red_threshold = 100
    transparency_factor = 0.7

    for i in range(0, len(pixels), 3):
        b, g, r = pixels[i:i + 3]

        if r > red_threshold and r > g + 50 and r > b + 50:
            gray_value = (b + g + r) // 3
            new_value = int((1 - transparency_factor) * gray_value + transparency_factor * 255)
            pixels[i:i + 3] = new_value, new_value, new_value  # Asignar nuevo valor a R, G y B

    return bmp_data[:header_size] + pixels

def select_image():
    """Seleccionar una imagen y procesarla para eliminar la marca de agua."""
    file_path = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp")]
    )

    if file_path:
        image = Image.open(file_path).convert("RGB")
        bmp_path = 'temp_image.bmp'
        image.save(bmp_path, format='BMP')

        # Leer los datos BMP
        bmp_data = load_bmp(bmp_path)

        # Procesar la imagen para eliminar la marca de agua
        processed_data = remove_watermark(bmp_data)

        # Guardar la imagen procesada como JPG
        output_path = 'imagen_procesada.jpg'
        
        width = int.from_bytes(processed_data[18:22], 'little')
        height = int.from_bytes(processed_data[22:26], 'little')
        pixels = processed_data[54:]  # Los datos de píxeles
        
        pixel_data = bytearray()
        for y in range(height):
            row_start = (height - 1 - y) * width * 3
            pixel_data.extend(pixels[row_start:row_start + width * 3])
        
        processed_image = Image.frombytes('RGB', (width, height), bytes(pixel_data))

        processed_image.save(output_path, format='JPEG')
        print(f'Imagen procesada guardada en {output_path}')
    else:
        print("No se seleccionó ninguna imagen.")

if __name__ == '__main__':
    # Crear la ventana para la interfaz gráfica
    root = tk.Tk()
    root.title("Quitar Marca de Agua")
    root.geometry("300x150")

    # Botón para seleccionar la imagen
    btn_select_image = tk.Button(root, text="Seleccionar Imagen", command=select_image)
    btn_select_image.pack(pady=50)

    # Iniciar el loop de la interfaz gráfica
    root.mainloop()
