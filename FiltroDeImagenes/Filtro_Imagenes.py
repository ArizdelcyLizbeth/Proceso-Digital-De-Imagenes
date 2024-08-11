from PIL import Image, ImageOps, ImageEnhance
import os

class Filtros:
    def __init__(self, image_path):
        try:
            self.image = Image.open(image_path)
            print(f"Imagen {image_path} cargada exitosamente.")
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    def save_image(self, image, name):
       
        if not os.path.exists('ImagenesGeneradas'):
            os.makedirs('ImagenesGeneradas')

        image.save(os.path.join('ImagenesGeneradas', f"{name}.jpg"))

    def alto_contraste(self):
        def contrast(p):
            return 0 if p < 128 else 255

        gray_image = self.image.convert("L")
        contrast_image = gray_image.point(contrast).convert("RGB")
        self.save_image(contrast_image, "alto_contraste")

    def filtro_rojo(self):
        red_image = self.image.convert("RGB")
        pixels = red_image.load()
        for y in range(red_image.height):
            for x in range(red_image.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r, 0, 0)
        self.save_image(red_image, "filtro_rojo")

    def filtro_verde(self):
        green_image = self.image.convert("RGB")
        pixels = green_image.load()
        for y in range(green_image.height):
            for x in range(green_image.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (0, g, 0)
        self.save_image(green_image, "filtro_verde")

    def filtro_azul(self):
        blue_image = self.image.convert("RGB")
        pixels = blue_image.load()
        for y in range(blue_image.height):
            for x in range(blue_image.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (0, 0, b)
        self.save_image(blue_image, "filtro_azul")

    def filtro_morado(self):
        purple_image = self.image.convert("RGB")
        pixels = purple_image.load()
        for y in range(purple_image.height):
            for x in range(purple_image.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r, 0, b)
        self.save_image(purple_image, "filtro_morado")

    def inverso(self):
        inverted_image = ImageOps.invert(self.image.convert("RGB"))
        self.save_image(inverted_image, "inverso")

    def filtro_color_a_gris(self, metodo='a'):
        gray_image = self.image.copy()
        pixels = gray_image.load()
        
        for y in range(gray_image.height):
            for x in range(gray_image.width):
                r, g, b = pixels[x, y]
                
                if metodo == 'a':
                    # Método a: A+G+B div 3
                    gray_value = (r + g + b) // 3
                elif metodo == 'b':
                    # Método b: .28*R + .56*G + 0.11*B
                    gray_value = int(0.28 * r + 0.56 * g + 0.11 * b)
                elif metodo == 'c':
                    # Método c: (R,R,R),(G,G,G),(B,B,B)
                    # Ejemplo con R: (r, r, r)
                    gray_value = r  # Esto elige el canal rojo; puede cambiar a g o b según el caso
                
                pixels[x, y] = (gray_value, gray_value, gray_value)

        self.save_image(gray_image, f"filtro_color_a_gris_{metodo}")

    def filtro_mosaico(self, size=10):
        mosaic_image = self.image.copy()
        small_image = mosaic_image.resize(
            (mosaic_image.width // size, mosaic_image.height // size),
            resample=Image.NEAREST
        )
        mosaic_image = small_image.resize(
            (mosaic_image.width, mosaic_image.height),
            resample=Image.NEAREST
        )
        self.save_image(mosaic_image, "filtro_mosaico")

  