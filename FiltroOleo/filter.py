import numpy as np
from PIL import Image

def apply_sobel_filter(image_array):
    """
    Aplica el filtro de Sobel a una imagen en escala de grises para detectar bordes.
    Args:
        image_array (np.ndarray): Matriz 2D que representa la imagen en escala de grises.
    Returns:
        np.ndarray: Matriz 2D en escala de grises que resalta los bordes detectados.
    """

    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])
    
    height, width = image_array.shape
    edges = np.zeros_like(image_array)

    # Recorre cada píxel en la imagen (excepto los bordes)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            gx = np.sum(sobel_x * image_array[i - 1:i + 2, j - 1:j + 2])
            gy = np.sum(sobel_y * image_array[i - 1:i + 2, j - 1:j + 2])
            edges[i, j] = np.sqrt(gx**2 + gy**2)

    return edges.astype(np.uint8)

def apply_oil_filter(image):
    """
    Aplica un efecto de oleo a la imagen en escala de grises, combinando el efecto
    con los bordes detectados mediante el filtro de Sobel.
    Args:
        image (PIL.Image): Imagen en escala de grises.
    Returns:
        PIL.Image: Imagen filtrada en escala de grises con el efecto de óleo y los bordes resaltados.
    """

    img_array = np.array(image)
    height, width = img_array.shape

    filtered_array = np.zeros_like(img_array)

    kernel_size = 21  
    half_kernel = kernel_size // 2

    edges = apply_sobel_filter(img_array)

    # Recorre cada píxel, ignorando los bordes, y aplica el filtro de oleo
    for i in range(half_kernel, height - half_kernel):
        for j in range(half_kernel, width - half_kernel):

            region = img_array[i - half_kernel:i + half_kernel + 1, j - half_kernel:j + half_kernel + 1]

            hist, _ = np.histogram(region.flatten(), bins=256, range=(0, 256))

            most_frequent = np.argmax(hist)

            pixel_values = []
            for val in range(max(0, most_frequent - 30), min(255, most_frequent + 30 + 1)):
                pixel_values.extend([val] * hist[val])

            if pixel_values:
                filtered_array[i, j] = np.random.choice(pixel_values)
            else:
                filtered_array[i, j] = most_frequent  

    smoothed_image = apply_smoothing(filtered_array)

    final_image = np.clip(smoothed_image + edges * 0.3, 0, 255)
    return Image.fromarray(final_image.astype(np.uint8), mode="L")

def apply_smoothing(image_array):
    """
    Aplica un suavizado promedio a una imagen en escala de grises
    Args:
        image_array (np.ndarray): Matriz 2D que representa la imagen en escala de grises.
    Returns:
        np.ndarray: Matriz 2D en escala de grises con el suavizado aplicado.
    """
    kernel = np.ones((3, 3), np.float32) / 9
    smoothed_array = np.zeros_like(image_array)

    height, width = image_array.shape
    half_kernel = kernel.shape[0] // 2

    # Aplica el suavizado promedio sobre cada píxel
    for i in range(half_kernel, height - half_kernel):
        for j in range(half_kernel, width - half_kernel):
            region = image_array[i - half_kernel:i + half_kernel + 1, j - half_kernel:j + half_kernel + 1]
            smoothed_array[i, j] = np.sum(region * kernel)

    return smoothed_array.astype(np.uint8)
