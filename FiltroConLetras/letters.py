from PIL import Image, ImageDraw, ImageFont

def aplicar_filtro(imagen, letra):
    """
    Aplica un filtro a la imagen, convirtiendola en una imagen de texto.

    Args:
    imagen (PIL.Image): La imagen original a la que se le aplicara el filtro.
    letra (str): La letra que se usara.

    Returns:
    PIL.Image: Una nueva imagen.
    """
    # Convierte la imagen a escala de grises
    imagen = imagen.convert("L")
    ancho, alto = imagen.size
    nueva_imagen = Image.new("L", (ancho, alto), color=255)
    draw = ImageDraw.Draw(nueva_imagen)
    
    try:
        font_size = 8 
        font = ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()  

    # Dibuja la imagen con la letra seleccionada
    pixeles = imagen.load()
    step = font_size  

    for y in range(0, alto, step):
        for x in range(0, ancho, step):
            intensidad = pixeles[x, y]
            color = 255 - intensidad  
            draw.text((x, y), letra, font=font, fill=color)

    return nueva_imagen
