import numpy as np

def blur(img_array):
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
    filter_size = 21  # Tamaño del filtro
    filter = np.zeros((filter_size, filter_size))
    
    # Crear un filtro diagonal para desenfoque
    for i in range(filter_size):
        filter[i, (i + filter_size // 2) % filter_size] = 1.0
    
    # Normalizar el filtro
    factor = 1.0 / np.sum(filter)  # Normalizar por la suma de todos los elementos
    
    return apply_filter(img_array, filter, factor)

def find_edges(img_array):
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
    filter = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])
    factor = 1.0
    return apply_filter(img_array, filter, factor)

def emboss(img_array):
    filter = np.array([
        [-1, -1, 0],
        [-1, 0, 1],
        [0, 1, 1]
    ])
    factor = 1.0
    bias = 128.0
    return apply_filter(img_array, filter, factor, bias)

def promedio(img_array):
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
    from scipy.signal import convolve2d
    filtered_img_array = np.zeros_like(img_array)
    for i in range(img_array.shape[2]):  
        filtered_img_array[:, :, i] = convolve2d(img_array[:, :, i], filter, mode='same', boundary='wrap') * factor + bias
    return filtered_img_array