def load_bmp(filename):
    """Cargar los datos de un archivo BMP.
    Args:
        filename (str): Ruta del archivo BMP a cargar.
    Returns:
        bytes: Datos binarios del archivo BMP.
    """
    with open(filename, 'rb') as f:
        bmp_data = f.read()
    return bmp_data

def save_bmp(filename, bmp_data):
     """Guardar los datos en un archivo BMP.
    Args:
        filename (str): Ruta donde se guardará el archivo BMP.
        bmp_data (bytes): Datos binarios a guardar en el archivo BMP.
    """
    with open(filename, 'wb') as f:
        f.write(bmp_data)

def get_surrounding_neighbors(pixels, x, y, width, height):
    """Obtener los vecinos del píxel actual en un área de 3x3 alrededor (incluyendo diagonales).
    Args:
        pixels (bytearray): Datos de píxeles de la imagen.
        x (int): Coordenada X del píxel actual.
        y (int): Coordenada Y del píxel actual.
        width (int): Ancho de la imagen.
        height (int): Alto de la imagen. 
    Returns:
        list: Lista de colores de píxeles vecinos.
    """
    neighbors = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue  # Ignorar el píxel actual
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                index = (ny * width + nx) * 3
                neighbors.append(pixels[index:index + 3])
    return neighbors

def is_similar_to_color(r, g, b, target_color, tolerance=50):
    """Verifica si el píxel es similar al color objetivo dentro de una tolerancia.
    Args:
        r (int): Componente rojo del píxel.
        g (int): Componente verde del píxel.
        b (int): Componente azul del píxel.
        target_color (tuple): Color objetivo (R, G, B).
        tolerance (int): Tolerancia para la comparación. 
    Returns:
        bool: Verdadero si el color es similar al color objetivo, falso de lo contrario.
    """
    return abs(r - target_color[0]) <= tolerance and \
           abs(g - target_color[1]) <= tolerance and \
           abs(b - target_color[2]) <= tolerance

def replace_with_neighbor_color(pixels, x, y, width, height, target_color):
    """Reemplaza el píxel si es similar al color objetivo con un color de los vecinos.
    Args:
        pixels (bytearray): Datos de píxeles de la imagen.
        x (int): Coordenada X del píxel actual.
        y (int): Coordenada Y del píxel actual.
        width (int): Ancho de la imagen.
        height (int): Alto de la imagen.
        target_color (tuple): Color objetivo (R, G, B) que representa la marca de agua.
    """
    index = (y * width + x) * 3
    b, g, r = pixels[index:index + 3]

    if is_similar_to_color(r, g, b, target_color):
        neighbors = get_surrounding_neighbors(pixels, x, y, width, height)
        
        valid_neighbors = [color for color in neighbors if not is_similar_to_color(color[2], color[1], color[0], target_color)]
        
        if valid_neighbors:
            chosen_color = valid_neighbors[0] 
            pixels[index:index + 3] = chosen_color  

def remove_watermark(pixels, width, height, target_color):
    """Recorre todos los píxeles y suaviza aquellos que son similares al color objetivo.
    Args:
        pixels (bytearray): Datos de píxeles de la imagen.
        width (int): Ancho de la imagen.
        height (int): Alto de la imagen.
        target_color (tuple): Color objetivo (R, G, B) que representa la marca de agua.
    Returns:
        bytearray: Datos de píxeles modificados sin la marca de agua.
    """
    for y in range(height):
        for x in range(width):
            replace_with_neighbor_color(pixels, x, y, width, height, target_color)
    return pixels

def process_image(bmp_data, target_color=(255, 0, 0)):
    """Procesa la imagen BMP para eliminar la marca de agua usando vecinos.
    Args:
        bmp_data (bytes): Datos binarios de la imagen BMP.
        target_color (tuple): Color objetivo (R, G, B) que representa la marca de agua (por defecto rojo). 
    Returns:
        bytes: Datos binarios de la imagen BMP procesada sin la marca de agua.
    """
    header_size = 54
    pixels = bytearray(bmp_data[header_size:])
    width = int.from_bytes(bmp_data[18:22], 'little')
    height = int.from_bytes(bmp_data[22:26], 'little')

    pixels = remove_watermark(pixels, width, height, target_color)

    return bmp_data[:header_size] + pixels
