from PIL import Image, ImageFilter

def blur_image(image):
    return image.filter(ImageFilter.BLUR)

def motion_blur_image(image):
    size = (9, 9)
    motion_blur_filter = ImageFilter.Kernel(size, [
        1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 1
    ], scale=9)
    return image.filter(motion_blur_filter)

def find_edges_image(image):
    return image.filter(ImageFilter.FIND_EDGES)

def sharpen_image(image):
    return image.filter(ImageFilter.SHARPEN)

def emboss_image(image):
    return image.filter(ImageFilter.EMBOSS)

def average_blur_image(image):
    size = (3, 3)
    average_blur_filter = ImageFilter.Kernel(size, [
        0.0, 0.2, 0.0,
        0.2, 0.2, 0.2,
        0.0, 0.2, 0.0
    ], scale=1.0)
    return image.filter(average_blur_filter)
