import numpy as np

def aplicar_filtro_maximo(imagen):
    """
    Aplica el filtro utilizando una vecindad de 3x3 píxeles.

    Este filtro toma el valor máximo de la vecindad de cada píxel en la imagen y lo asigna al píxel central.
    El filtro se realiza sobre cada píxel de la imagen, excluyendo los bordes para evitar errores
    por falta de vecindad.

    Parámetros:
    imagen (numpy.ndarray): Imagen de entrada en formato de matriz de píxeles.

    Retorna:
    numpy.ndarray: Imagen resultante con el filtro máximo aplicado.
    """

    imagen_maxima = np.copy(imagen)
    
    kernel = np.ones((3, 3), np.uint8)
    
    for i in range(1, imagen.shape[0] - 1): 
        for j in range(1, imagen.shape[1] - 1):

            vecindad = imagen[i - 1:i + 2, j - 1:j + 2]
            imagen_maxima[i, j] = np.max(vecindad * kernel)
    
    return imagen_maxima


def aplicar_filtro_minimo(imagen):
    """
    Aplica el filtro utilizando una vecindad de 3x3 píxeles.

    Este filtro toma el valor mínimo de la vecindad de cada píxel en la imagen y lo asigna al píxel central.
    El filtro se realiza sobre cada píxel de la imagen, excluyendo los bordes para evitar errores
    por falta de vecindad.

    Parámetros:
    imagen (numpy.ndarray): Imagen de entrada en formato de matriz de píxeles.

    Retorna:
    numpy.ndarray: Imagen resultante con el filtro mínimo aplicado.
    """
    imagen_minima = np.copy(imagen)
    
    kernel = np.ones((3, 3), np.uint8)
    
    for i in range(1, imagen.shape[0] - 1):  
        for j in range(1, imagen.shape[1] - 1):
            vecindad = imagen[i - 1:i + 2, j - 1:j + 2]
            imagen_minima[i, j] = np.min(vecindad * kernel)
    
    return imagen_minima
