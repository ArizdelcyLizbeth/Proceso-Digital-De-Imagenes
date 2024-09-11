import numpy as np
import cv2
from PIL import Image

def resize_image(image, scale):
    """Redimensiona la imagen al tamaño especificado por la escala."""
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    return resized

def recursive_image(image, num_steps):
    """Genera una imagen recursiva a partir de la imagen dada."""
    height, width, _ = image.shape
    step_size = width // (2 ** num_steps)
    
    # Crea una imagen en blanco para el resultado
    recursive_img = np.zeros((height, width, 3), dtype=np.uint8)
    
    for y in range(0, height, step_size):
        for x in range(0, width, step_size):
            scale = step_size / width
            resized_img = resize_image(image, scale)
            img_height, img_width, _ = resized_img.shape
            y_end = min(y + img_height, height)
            x_end = min(x + img_width, width)
            recursive_img[y:y_end, x:x_end] = resized_img[:y_end-y, :x_end-x]

    return recursive_img

def apply_grayscale_filter(image_path, num_steps=5):
    """Aplica un filtro recursivo en tonos de gris a la imagen."""
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img_color = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)

    # Generar imagen recursiva en tonos de gris
    recursive_img = recursive_image(gray_img_color, num_steps)
    
    # Guardar la imagen recursiva
    imagen_recursiva = 'recursive_gray_image.jpg'
    cv2.imwrite(imagen_recursiva, recursive_img)

    return imagen_recursiva

def apply_color_filter(image_path, num_steps=5):
    """Aplica un filtro recursivo a color a la imagen."""
    img = cv2.imread(image_path)

    # Generar imagen recursiva a color
    recursive_img = recursive_image(img, num_steps)
    
    # Guardar la imagen recursiva
    imagen_recursiva = 'recursive_color_image.jpg'
    cv2.imwrite(imagen_recursiva, recursive_img)

    return imagen_recursiva