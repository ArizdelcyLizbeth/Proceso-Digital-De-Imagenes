import numpy as np
import cv2

def resize_image(image, scale, interpolation=cv2.INTER_LANCZOS4):
    """
    Redimensiona una imagen.
    Parámetros:
    - image: La imagen que se quiere redimensionar.
    - scale: Factor de escala para el redimensionamiento.
    - interpolation: Método de interpolación (por defecto cv2.INTER_LANCZOS4).
    Retorna:
    - resized: La imagen redimensionada.
    """
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    resized = cv2.resize(image, (width, height), interpolation=interpolation)
    return resized

def compute_average_color(image):
    """
    Calcula el color promedio de la imagen.
    Parámetros:
    - image: La imagen de la cual se calculará el color promedio.
    Retorna:
    - El color promedio de la imagen en formato BGR.
    """
    return np.mean(image, axis=(0, 1))

def recursive_image(image, num_steps, grayscale=False):
    """
    Genera una imagen recursiva a partir de la imagen dada, aplicando un filtro en cada paso.
    Parámetros:
    - image: La imagen original de entrada.
    - num_steps: El número de pasos o iteraciones recursivas.
    - grayscale: Si es True, convierte las regiones a tonos de gris.
    Retorna:
    - recursive_img: La imagen recursiva generada.
    """
    height, width, _ = image.shape
    step_size = width // (2 ** num_steps)

    recursive_img = np.zeros_like(image)

    for y in range(0, height, step_size):
        for x in range(0, width, step_size):
            region = image[y:y+step_size, x:x+step_size]
            avg_color = compute_average_color(region)
            
            if grayscale:
                avg_gray = np.mean(avg_color)
                avg_color = np.array([avg_gray] * 3)

            scale = step_size / width
            resized_img = resize_image(image, scale)
            resized_img = resized_img.astype(np.float32)
            
            # Aplicamos el color promedio
            avg_color = np.array(avg_color)
            adjusted_img = resized_img * (avg_color / 255.0)
            
            # Ddimensiones sean correctas
            y_end = min(y + step_size, height)
            x_end = min(x + step_size, width)

            adjusted_img = cv2.resize(adjusted_img, (x_end-x, y_end-y), interpolation=cv2.INTER_LANCZOS4)

            recursive_img[y:y_end, x:x_end] = adjusted_img[:y_end-y, :x_end-x]

    recursive_img = cv2.GaussianBlur(recursive_img, (5, 5), 0)

    return recursive_img

def apply_grayscale_filter(image_path, num_steps=6):
    """
    Aplica un filtro recursivo en tonos de gris a la imagen.
    Parámetros:
    - image_path: La ruta de la imagen de entrada.
    - num_steps: El número de pasos o iteraciones recursivas.
    Retorna:
    - La ruta de la imagen generada en tonos de gris.
    """
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img_color = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)

    recursive_img = recursive_image(gray_img_color, num_steps, grayscale=True)
    
    cv2.imwrite('recursive_gray_image.jpg', recursive_img)
    return 'recursive_gray_image.jpg'

def apply_color_filter(image_path, num_steps=6):
    """
    Aplica un filtro recursivo a color a la imagen.
    Parámetros:
    - image_path: La ruta de la imagen de entrada.
    - num_steps: El número de pasos o iteraciones recursivas.
    Retorna:
    - La ruta de la imagen generada a color.
    """
    img = cv2.imread(image_path)

    recursive_img = recursive_image(img, num_steps)
    
    cv2.imwrite('recursive_color_image.jpg', recursive_img)
    return 'recursive_color_image.jpg'
