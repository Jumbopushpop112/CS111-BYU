from byuimage import Image
image = Image("pebbles.jpg")
image.show()

# for pixel in image:
#     pixel.green = 0
#     pixel.blue = 0
# image.show()



def darken(image):
    for pixel in image:
        pixel.red = pixel.red * 0.5
        pixel.green = pixel.green * 0.5
        pixel.blue = pixel.blue * 0.5
    return image

darken(image)
image.show()



def darken_half(image):
    """ Pass in an image, modify it """
    for y in range(image.height//2):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel.red = pixel.red * 0.5
            pixel.green = pixel.green * 0.5
            pixel.blue = pixel.blue * 0.5

image = Image("pebbles.jpg")
darken_half(image)
image.show()



def copy(image):
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_new = new_image.get_pixel(x, y)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    return new_image

copy(image).show()



def mute_top(image):
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_new = new_image.get_pixel(x, y)
            factor = 1.0
            if (pixel.red + pixel.blue + pixel.green)/3 > 120 and y < image.height//2:
                factor = 0.5
            pixel_new.red = pixel.red * factor
            pixel_new.green = pixel.green * factor
            pixel_new.blue = pixel.blue * factor
    return new_image

image = Image("pebbles.jpg")
mute_top(image).show()



def bottom_black_border(image):
    new_image = Image.blank(image.width,image.height+50)   # Create the larger image.
    for y in range(image.height):                          # Copy the original image
        for x in range(image.width):                       #  into the top of the new
            pixel = image.get_pixel(x, y)                  #  one.
            pixel_new = new_image.get_pixel(x, y)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    for y in range(image.height,image.height+50):          # Make the pixels in the
        for x in range(image.width):                       #  bottom black. RGB for
            pixel_new = new_image.get_pixel(x, y)          #  black is (0,0,0).
            pixel_new.red = 0
            pixel_new.green = 0
            pixel_new.blue = 0

    return new_image

bottom_black_border(image).show()