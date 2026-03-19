from byuimage import Image
#flip an image vertically
def flipped(filename):
    image = Image(filename)
    newImage = Image.blank(image.width,image.height)
    for y in range(0,newImage.height):
        for x in range(0,newImage.width):
            pixel = image.get_pixel(x,y)
            newPixel = newImage.get_pixel(x,image.height-y-1)
            newPixel.red = pixel.red
            newPixel.blue = pixel.blue
            newPixel.green = pixel.green
    return newImage
#fill the borders around an image
def make_borders(filename, thickness, red, green, blue):
    #make the new image and fill the border with specified colors
    image = Image(filename)
    borderImage = Image.blank(image.width + (thickness * 2), image.height + (thickness*2))
    for y in range(borderImage.height):
        for x in range(borderImage.width):
            pixel = borderImage.get_pixel(x,y)
            pixel.red = red
            pixel.green = green
            pixel.blue = blue
    #now it's time to copy the original image!
    for y in range(image.height):
        for x in range(image.width):
            imagePixel = image.get_pixel(x,y)
            borderPixel = borderImage.get_pixel(x+thickness,y+thickness)
            borderPixel.red = imagePixel.red
            borderPixel.blue = imagePixel.blue
            borderPixel.green = imagePixel.green
    return borderImage
if __name__ == "__main__":
    flipped("test_files/landscape.png").show()
    make_borders("test_files/landscape.png", 30, 200, 0, 0).show()