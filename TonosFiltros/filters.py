import random
from PIL import Image, ImageDraw

# PRIMER FILTRO - Dithering al azar
def random_dithering(imagen):
    """
    Aplica el filtro de dithering aleatorio a una imagen.
    :param imagen: La imagen a la que se le aplicará el dithering.
    :return: La imagen con el dithering aleatorio aplicado.
    """
    pixeles = imagen.load()
    ancho, alto = imagen.size

    for i in range(ancho):
        for j in range(alto):
            valor_pixel = pixeles[i, j]
            if isinstance(valor_pixel, tuple):
                valor_pixel = valor_pixel[0]  

            valor_random = random.randint(0, 255)
            if valor_random > valor_pixel:
                pixeles[i, j] = (0, 0, 0)
            else:
                pixeles[i, j] = (255, 255, 255)

    return imagen

# SEGUNDO FILTRO - Dithering ordenado
def ordered_dithering(imagen):
    """
    Aplica el filtro de dithering ordenado a una imagen usando una matriz de umbrales predefinidos.
    :param imagen: La imagen a la que se le aplicará el dithering ordenado.
    :return: La imagen con el dithering ordenado aplicado.
    """
    pixeles = imagen.load()
    ancho, alto = imagen.size

    matriz_ordenada = [
        [8, 3, 4],
        [6, 1, 2],
        [7, 5, 9]
    ]

    for i in range(ancho):
        for j in range(alto):
            valor_pixel = pixeles[i, j]
            if isinstance(valor_pixel, tuple):
                valor_pixel = valor_pixel[0]  

            umbral = matriz_ordenada[j % 3][i % 3]
            valor_normalizado = valor_pixel // 28

            if valor_normalizado < umbral:
                pixeles[i, j] = (0, 0, 0)
            else:
                pixeles[i, j] = (255, 255, 255)

    return imagen

# TERCER FILTRO - Dithering disperso
def dispersed_dithering(imagen):
    """
    Aplica el filtro de dithering disperso a una imagen usando una matriz dispersa.
    :param imagen: La imagen a la que se le aplicará el dithering disperso.
    :return: La imagen con el dithering disperso aplicado.
    """
    pixeles = imagen.load()
    ancho, alto = imagen.size

    matriz_disperso = [
        [1, 7, 4],
        [5, 8, 3],
        [6, 2, 9]
    ]

    for i in range(ancho):
        for j in range(alto):
            valor_pixel = pixeles[i, j]
            if isinstance(valor_pixel, tuple):
                valor_pixel = valor_pixel[0]  
            umbral = matriz_disperso[j % 3][i % 3]
            valor_normalizado = valor_pixel // 28

            if valor_normalizado < umbral:
                pixeles[i, j] = (0, 0, 0)
            else:
                pixeles[i, j] = (255, 255, 255)

    return imagen

# CUARTO FILTRO - Floyd-Steinberg Dithering
def floyd_steinberg_dithering(imagen):
    """
    Aplica el filtro de Floyd-Steinberg Dithering a una imagen.
    :param imagen: La imagen a la que se le aplicará el dithering.
    :return: La imagen con el dithering de Floyd-Steinberg aplicado.
    """
    pixeles = imagen.load()
    ancho, alto = imagen.size

    for y in range(alto):
        for x in range(ancho):
            valor_actual = pixeles[x, y]
            if isinstance(valor_actual, tuple):
                valor_actual = valor_actual[0]  

            nuevo_valor = 255 if valor_actual > 127 else 0
            error = valor_actual - nuevo_valor
            pixeles[x, y] = (nuevo_valor, nuevo_valor, nuevo_valor)

            if x < ancho - 1:
                pixeles[x + 1, y] = corregir_pixel(pixeles[x + 1, y], error * 7 / 16)
            if x > 0 and y < alto - 1:
                pixeles[x - 1, y + 1] = corregir_pixel(pixeles[x - 1, y + 1], error * 3 / 16)
            if y < alto - 1:
                pixeles[x, y + 1] = corregir_pixel(pixeles[x, y + 1], error * 5 / 16)
            if x < ancho - 1 and y < alto - 1:
                pixeles[x + 1, y + 1] = corregir_pixel(pixeles[x + 1, y + 1], error * 1 / 16)

    return imagen

def corregir_pixel(pixel, error):
    """
    Corrige el valor de un píxel sumándole el error de cuantización.
    :param pixel: Valor original del píxel.
    :param error: Error de cuantización a aplicar.
    :return: El nuevo valor del píxel corregido.
    """
    if isinstance(pixel, tuple):
        pixel = pixel[0]  

    nuevo_pixel = min(max(int(pixel + error), 0), 255)
    return (nuevo_pixel, nuevo_pixel, nuevo_pixel)

# FILTRO DE SEMITONOS CON PUNTOS
def apply_halftone_filter(image, dot_size=10, overlap=0.2):
    """
    Aplica el filtro de semitonos con puntos a una imagen.
    :param image: La imagen a la que se le aplicará el filtro de semitonos.
    :param dot_size: Tamaño de los puntos en el semitono.
    :param overlap: Porcentaje de superposición entre los puntos.
    :return: La imagen con el filtro de semitonos aplicado.
    """
    print(f"Procesando imagen de tamaño: {image.size}")

    if image.mode != 'L':
        image = image.convert('L')

    width, height = image.size
    new_image = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(new_image)
    pixels = image.load()

    half_dot = dot_size / 2
    overlap_amount = dot_size * overlap

    for y in range(0, height, dot_size):
        for x in range(0, width, dot_size):
            brightness = pixels[x, y]  
            radius = int((1 - brightness / 255) * half_dot + overlap_amount)
            radius = max(1, radius)  

            if radius > 0:
                upper_left = (x - radius, y - radius)
                bottom_right = (x + radius, y + radius)
                draw.ellipse([upper_left, bottom_right], fill=0)
    return new_image
