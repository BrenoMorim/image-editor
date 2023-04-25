from PIL import ImageFilter, Image, ImageOps
from validator import Validator


def blur_image(image: Image) -> Image:
    """
    Reduces the quality of the image
    """
    return image.filter(ImageFilter.BLUR)

def contour_image(image: Image) -> Image:
    """
    Turns all the image black, making only the contour white
    """
    return image.filter(ImageFilter.CONTOUR)

def detail_image(image: Image) -> Image:
    """
    Tries to make the image more detailed
    """
    return image.filter(ImageFilter.DETAIL)

def sharpen_image(image: Image) -> Image:
    """
    Increases the sharpness of the image
    """
    return image.filter(ImageFilter.SHARPEN)

def smooth_image(image: Image) -> Image:
    """
    Smoothes the image
    """
    return image.filter(ImageFilter.SMOOTH)

def edge_image(image: Image) -> Image:
    """
    Emphasizes the edges of the image
    """
    return image.filter(ImageFilter.EDGE_ENHANCE)

def grayscale_image(image: Image) -> Image:
    """
    Applies the grayscale filter on the image
    """
    return ImageOps.grayscale(image)

def flip_image(image: Image) -> Image:
    """
    Flips the image from top to bottom
    """
    return ImageOps.flip(image)

def invert_image(image: Image) -> Image:
    """
    Invert the colors of the image, black turns white, white turns black and so on.
    """
    image = image.convert("RGB")
    return ImageOps.invert(image)

def mirror_image(image: Image) -> Image:
    """
    Mirrors the image from left to right
    """
    return image.transpose(method=Image.FLIP_LEFT_RIGHT)

# Dictionary to map each action to a function, in order to avoid unnecessary if-elses
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

def execute(args: Validator) -> None:
    """
    Executes the specified action in the input file, saving the result in the output file

    :param args: Validator object, containing the CLI arguments
    :type args: Validator
    """
    with Image.open(args.input) as image:
        if args.action == "resize":
            result_image = image.resize(args.size)
        else:
            result_image = function_mapping[args.action](image)
        result_image.save(args.output)
