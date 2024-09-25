from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, output_path=None, margin=50):
    """
    Agrega una marca de agua de texto repetida en toda la imagen 

    Args:
        image_path (str): Ruta de la imagen de entrada.
        watermark_text (str): Texto que se utilizará como marca de agua.
        output_path (str, optional): Ruta de salida donde se guardará la imagen con la marca de agua.
        margin (int, optional): Margen entre las repeticiones del texto de la marca de agua. 
                                El valor por defecto es 50 píxeles.

    Returns:
        PIL.Image.Image: Imagen resultante con la marca de agua aplicada.
    """
    with Image.open(image_path) as im:
        im = im.convert("RGBA")
        
        width, height = im.size
        
        watermark = Image.new("RGBA", im.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)
        
        font_size = 50  
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        watermark_color = (255, 255, 255, 128)  
        
        # Calcular el espaciado de imagen
        spacing_x = text_width + margin
        spacing_y = text_height + margin
        
        # Generar las marcas de agua en la imagen
        for x in range(0, width + spacing_x, spacing_x):
            for y in range(0, height + spacing_y, spacing_y):
                draw.text((x, y), watermark_text, font=font, fill=watermark_color)
        
        # Combinar la imagen original con la marca de agua
        combined = Image.alpha_composite(im, watermark)
        combined = combined.convert("RGB")
        
        if output_path:
            combined.save(output_path)
        return combined
        