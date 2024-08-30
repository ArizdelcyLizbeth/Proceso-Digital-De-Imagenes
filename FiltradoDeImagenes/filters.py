import numpy as np

def blur(img_array):
    filter = np.array([
        [0.0, 0.2, 0.0],
        [0.2, 0.2, 0.2],
        [0.0, 0.2, 0.0]
    ])
    factor = 1.0
    return apply_filter(img_array, filter, factor)

def motion_blur(img_array):
    filter = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ])
    factor = 1.0 / 9.0
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
    filter = np.ones((3, 3)) / 9.0
    factor = 1.0
    return apply_filter(img_array, filter, factor)

def apply_filter(img_array, filter, factor, bias=0.0):
    from scipy.signal import convolve2d
    filtered_img_array = np.zeros_like(img_array)
    for i in range(img_array.shape[2]):  
        filtered_img_array[:, :, i] = convolve2d(img_array[:, :, i], filter, mode='same', boundary='wrap') * factor + bias
    return filtered_img_array
