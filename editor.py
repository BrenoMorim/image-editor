from PIL import ImageFilter, Image, ImageOps
from validator import Validator


def blur_image(image: Image) -> Image:
    return image.filter(ImageFilter.BLUR)

def contour_image(image: Image) -> Image:
    return image.filter(ImageFilter.CONTOUR)

def detail_image(image: Image) -> Image:
    return image.filter(ImageFilter.DETAIL)

def sharpen_image(image: Image) -> Image:
    return image.filter(ImageFilter.SHARPEN)

def smooth_image(image: Image) -> Image:
    return image.filter(ImageFilter.SMOOTH)

def edge_image(image: Image) -> Image:
    return image.filter(ImageFilter.EDGE_ENHANCE)

def grayscale_image(image: Image) -> Image:
    return ImageOps.grayscale(image)

def flip_image(image: Image) -> Image:
    return ImageOps.flip(image)

def invert_image(image: Image) -> Image:
    image = image.convert("RGB")
    return ImageOps.invert(image)

def mirror_image(image: Image) -> Image:
    return image.transpose(method=Image.FLIP_LEFT_RIGHT)

function_mapping = {
    "blur": blur_image,
    "smooth": smooth_image,
    "sharpen": sharpen_image,
    "edge": edge_image,
    "detail": detail_image,
    "contour": contour_image,
    "grayscale": grayscale_image,
    "flip": flip_image,
    "invert": invert_image,
    "mirror": mirror_image
}

def execute(args: Validator):
    with Image.open(args.input) as image:
        result_image = function_mapping[args.action](image)
        result_image.save(args.output)
