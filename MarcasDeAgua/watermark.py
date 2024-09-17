from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, output_path=None):
    with Image.open(image_path) as im:
        im = im.convert("RGBA")
        
        watermark = Image.new("RGBA", im.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)
        
        font_size = 50  
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size) if ImageFont.truetype else ImageFont.load_default()
        
        width, height = im.size
        
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        watermark_color = (255, 255, 255, 128)  
        
       
        spacing = 200  # Espacio entre marcas de agua 
        for x in range(-width, width + spacing, spacing):
            for y in range(-height, height + spacing, spacing):
                draw.text((x, y), watermark_text, font=font, fill=watermark_color)
        
        combined = Image.alpha_composite(im, watermark)
        combined = combined.convert("RGB")
        
        if output_path:
            combined.save(output_path)
        return combined
