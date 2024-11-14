import numpy as np
from PIL import Image

def interpolacion_bilinear(imagen, nueva_altura, nueva_anchura):
    """
    Realiza interpolación bilineal para redimensionar la imagen.
    :param imagen: La imagen como una matriz de píxeles.
    :param nueva_altura: La nueva altura.
    :param nueva_anchura: La nueva anchura.
    :return: Imagen redimensionada.
    """
    altura, anchura = imagen.shape[:2]
    nueva_imagen = np.zeros((nueva_altura, nueva_anchura, imagen.shape[2]), dtype=imagen.dtype)

    escala_x = anchura / nueva_anchura
    escala_y = altura / nueva_altura

    for i in range(nueva_altura):
        for j in range(nueva_anchura):
            x = j * escala_x
            y = i * escala_y
            x1, y1 = int(x), int(y)
            x2, y2 = min(x1 + 1, anchura - 1), min(y1 + 1, altura - 1)
            dx, dy = x - x1, y - y1

            A = imagen[y1, x1]
            B = imagen[y1, x2]
            C = imagen[y2, x1]
            D = imagen[y2, x2]

            pixel_val = (A * (1 - dx) * (1 - dy) +
                         B * dx * (1 - dy) +
                         C * (1 - dx) * dy +
                         D * dx * dy)

            nueva_imagen[i, j] = np.clip(pixel_val, 0, 255)

    return nueva_imagen

def escala_hacia_arriba(imagen, factor):
    """
    Aumenta el tamaño de la imagen utilizando interpolación bilineal.
    :param imagen: La imagen como una matriz de píxeles.
    :param factor: Factor de escala hacia arriba.
    :return: Nueva imagen escalada.
    """
    nueva_altura = int(imagen.shape[0] * factor)
    nueva_anchura = int(imagen.shape[1] * factor)
    return interpolacion_bilinear(imagen, nueva_altura, nueva_anchura)

def escala_hacia_abajo(imagen, factor):
    """
    Reduce el tamaño de la imagen utilizando interpolación bilineal.
    :param imagen: La imagen como una matriz de píxeles.
    :param factor: Factor de escala hacia abajo.
    :return: Nueva imagen reducida.
    """
    nueva_altura = max(1, int(imagen.shape[0] / factor))
    nueva_anchura = max(1, int(imagen.shape[1] / factor))
    return interpolacion_bilinear(imagen, nueva_altura, nueva_anchura)

def pil_to_numpy(imagen_pil):
    return np.array(imagen_pil)

def numpy_to_pil(imagen_numpy):
    return Image.fromarray(imagen_numpy.astype(np.uint8))
