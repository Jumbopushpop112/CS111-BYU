# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byuimage import Image
def iron_puzzle(filename):
    image = Image(filename)
    for pixel in image:
        pixel.red = 0
        pixel.green = 0
        pixel.blue *= 10
    return image


def west_puzzle(filename):
    image = Image(filename)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x,y)
            pixel.green = 0
            pixel.red = 0
            if pixel.blue < 16:
                pixel.blue *= 16
            else:
                pixel.blue = 0
    return image


def darken(filename, percent):
    image = Image(filename)
    for pixel in image:
        pixel.red = pixel.red * (1-percent)
        pixel.blue = pixel.blue * (1-percent)
        pixel.green = pixel.green * (1-percent)
    return image

def grayscale(filename):
    image = Image(filename)
    for pixel in image:
        average = (pixel.green + pixel.red + pixel.blue)/3
        pixel.red = average
        pixel.blue = average
        pixel.green = average
    return image


def sepia(filename):
    image = Image(filename)
    for pixel in image:
        true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
        pixel.red = true_red
        pixel.blue = true_blue
        pixel.green = true_green
        if pixel.red > 255:
            pixel.red = 255
        if pixel.blue > 255:
            pixel.blue = 255
        if pixel.green > 255:
            pixel.green = 255
            solution = sepia("test_files/cougar.png")
    return image


def create_left_border(filename, weight):
    image = Image(filename)
    newImage = Image.blank(image.width + weight, image.height)
    for y in range(image.height):
        for x in range(newImage.width):
            pixel = newImage.get_pixel(x,y)
            pixel.blue = 255
            pixel.red = 0
            pixel.green = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x,y)
            new_pixel = newImage.get_pixel(x+weight,y)
            new_pixel.blue = pixel.blue
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
    return newImage



def copper_puzzle(filename):
    image = Image(filename)
    for pixel in image:
        pixel.blue *= 20
        pixel.green * 20
        pixel.red = 0
    return image

if __name__ == "__main__":
    copper_puzzle("test_files/copper.png").show()
