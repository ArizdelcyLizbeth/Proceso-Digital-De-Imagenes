import numpy as np

def blur(img_array):
    """
    Aplica un filtro de blur a la imagen dada.
    
    :param img_array: Array de la imagen a procesar.
    :return: Imagen filtrada con el filtro de blur.
    """
    filter = np.array([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ], dtype=np.float64)
    factor = 1.0 / np.sum(filter)
    return apply_filter(img_array, filter, factor)

def motion_blur(img_array):
    """
    Aplica un filtro motion_blur a la imagen dada.
    
    :param img_array: Array de la imagen a procesar.
    :return: Imagen filtrada con el filtro de motion_blur.
    """
    filter_size = 21 
    filter = np.zeros((filter_size, filter_size))
    for i in range(filter_size):
        filter[i, (i + filter_size // 2) % filter_size] = 1.0
    factor = 1.0 / np.sum(filter) 
    return apply_filter(img_array, filter, factor)

def find_edges(img_array):
    """
    Aplica un filtro para detectar bordes en la imagen dada.
    
    :param img_array: Array de la imagen a procesar.
    :return: Imagen filtrada con el filtro de find_edges.
    """
    filter = np.array([
        [0, 0, -1, 0, 0],
        [0, 0, -1, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    factor = 1.0
    return apply_filter(img_array, filter, factor)

def sharpen(img_array):
    """
    Aplica un filtro de sharpen a la imagen dada.
    
    :param img_array: Array de la imagen a procesar.
    :return: Imagen filtrada con el filtro de sharpen.
    """
    filter = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])
    factor = 1.0
    return apply_filter(img_array, filter, factor)

def emboss(img_array):
    """
    Aplica un filtro de emboss a la imagen dada.
    
    :param img_array: Array de la imagen a procesar.
    :return: Imagen filtrada con el filtro de emboss.
    """
    filter = np.array([
        [-1, -1, 0],
        [-1, 0, 1],
        [0, 1, 1]
    ])
    factor = 1.0
    bias = 128.0
    return apply_filter(img_array, filter, factor, bias)

def promedio(img_array):
    """
    Aplica un filtro de promedio a la imagen dada.
    Puede parecerse al filtro blur pero en realidad no es el mismo,
    blur es mas natural.

    :param img_array: Array de la imagen a procesar.
    :return: Imagen filtrada con el filtro de promedio.
    """
    filter = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]) / 25.0
    factor = 1.0
    return apply_filter(img_array, filter, factor)

def apply_filter(img_array, filter, factor, bias=0.0):
    """
    Aplica un filtro a la imagen dada.
    
    :param img_array: Array de la imagen a procesar.
    :param filter: Filtro a aplicar a la imagen.
    :param factor: Factor de ajuste para el filtro.
    :param bias: Valor opcional de sesgo a añadir a la imagen filtrada.
    :return: Imagen filtrada.
    """
    from scipy.signal import convolve2d
    filtered_img_array = np.zeros_like(img_array)
    for i in range(img_array.shape[2]):  
        filtered_img_array[:, :, i] = convolve2d(img_array[:, :, i], filter, mode='same', boundary='wrap') * factor + bias
    return filtered_img_array