import sys
from byuimage import Image

#validate commands function
def validate_commands(listArguments, numReqArguments):
    print(listArguments)
    if ("-" in listArguments[1]) and (len(listArguments) == numReqArguments):
        return True
    else:
        raise Exception("Command line arguments are not appropriate!")
#darken function
def darken(filename, outputFileName, percent):
    image = Image(filename)
    for pixel in image:
        pixel.red = pixel.red * (1-percent)
        pixel.blue = pixel.blue * (1-percent)
        pixel.green = pixel.green * (1-percent)
    image.save(outputFileName)
#display function
def display(filename):
    image = Image(filename)
    image.show()
#sepia function
def sepia(filename, outputfileName):
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
    image.save(outputfileName)
#grayscale function
def grayscale(filename, outputFileName):
    image = Image(filename)
    for pixel in image:
        average = (pixel.green + pixel.red + pixel.blue)/3
        pixel.red = average
        pixel.blue = average
        pixel.green = average
    image.save(outputFileName)
#function to make the borders
def make_borders(filename, outputFileName, thickness, red, green, blue):
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
    borderImage.save(outputFileName)
#function to flip an image
def flipped(filename, outputFileName):
    image = Image(filename)
    newImage = Image.blank(image.width,image.height)
    for y in range(0,newImage.height):
        for x in range(0,newImage.width):
            pixel = image.get_pixel(x,y)
            newPixel = newImage.get_pixel(x,image.height-y-1)
            newPixel.red = pixel.red
            newPixel.blue = pixel.blue
            newPixel.green = pixel.green
    newImage.save(outputFileName)
#mirror image function
def mirror(filename, outputFileName):
    image = Image(filename)
    newImage = Image.blank(image.width, image.height)
    for y in range(0, newImage.height):
        for x in range(0, newImage.width):
            pixel = image.get_pixel(x, y)
            newPixel = newImage.get_pixel(image.width-x-1,y)
            newPixel.red = pixel.red
            newPixel.blue = pixel.blue
            newPixel.green = pixel.green
    newImage.save(outputFileName)
def collage(image1, image2, image3, image4, outputFileName, thickness):
    #make the border image
    image1 = Image(image1)
    image2 = Image(image2)
    image3 = Image(image3)
    image4 = Image(image4)
    dimension1 = (image1.width + image1.width + (thickness * 3))
    dimension2 = (image1.height + image1.height + (thickness * 3))
    borderImage = Image.blank(dimension1, dimension2)
    for y in range(borderImage.height):
        for x in range(borderImage.width):
            pixel = borderImage.get_pixel(x,y)
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 0
    """
    For this part of my code, I noticed that I had different offsets that needed to be sent for each placing of an image,
    and I was not very certain on how to refactor my code. However, the code works, but a similar pattern is called each time.
    I figured that because I did not know how to refactor this code in the best way, that I would just leave it the way
    that it is. The code works as intended but might be able to be simplified
    """
    #copy image 1 over
    for y in range(image1.height):
        for x in range(image1.width):
            imagePixel = image1.get_pixel(x, y)
            borderPixel = borderImage.get_pixel(x + thickness, y + thickness)
            borderPixel.red = imagePixel.red
            borderPixel.blue = imagePixel.blue
            borderPixel.green = imagePixel.green
    #copy image 2 over
    for y in range(image1.height):
        for x in range(image1.width):
            imagePixel = image2.get_pixel(x, y)
            borderPixel = borderImage.get_pixel(x + image2.width + (thickness * 2), y + thickness )
            borderPixel.red = imagePixel.red
            borderPixel.blue = imagePixel.blue
            borderPixel.green = imagePixel.green
    #copy image 3 over
    for y in range(image1.height):
        for x in range(image1.width):
            imagePixel = image3.get_pixel(x, y)
            borderPixel = borderImage.get_pixel(x+thickness, y - image3.height - thickness)
            borderPixel.red = imagePixel.red
            borderPixel.blue = imagePixel.blue
            borderPixel.green = imagePixel.green
    #copy image 4 over
    for y in range(image1.height):
        for x in range(image1.width):
            imagePixel = image4.get_pixel(x, y)
            borderPixel = borderImage.get_pixel(x+ image4.width + (thickness * 2), y - image4.height - thickness)
            borderPixel.red = imagePixel.red
            borderPixel.blue = imagePixel.blue
            borderPixel.green = imagePixel.green
    #save image to file
    borderImage.save(outputFileName)
#detect green function
def detect_green(pixel, curFactor, curThreshold):
  average = (pixel.red + pixel.green + pixel.blue) / 3
  if pixel.green >= curFactor * average and pixel.green >  curThreshold:
    return True
  else:
    return False
#greenscreen function
def greenScreen(foreground, background, outputFileName, factor, threshold):
    final = Image.blank(background.width, background.height)
    for y in range(background.height):
        for x in range(background.width):
            fp = final.get_pixel(x, y)
            bp = background.get_pixel(x, y)
            fp.red = bp.red
            fp.green = bp.green
            fp.blue = bp.blue
    for y in range(foreground.height):
        for x in range(foreground.width):
            fp = foreground.get_pixel(x, y)
            if not detect_green(fp, factor,threshold):
                np = final.get_pixel(x, y)
                np.red = fp.red
                np.green = fp.green
                np.blue = fp.blue
    final.save(outputFileName)
def main():
    if sys.argv[1] == "-d" and validate_commands(sys.argv,3):
        display(sys.argv[2])
    elif sys.argv[1] == "-k" and validate_commands(sys.argv, 5):
        darken(sys.argv[2], sys.argv[3], float(sys.argv[4]))
    elif sys.argv[1] == "-s" and validate_commands(sys.argv, 4):
        sepia(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-g" and validate_commands(sys.argv,4):
        grayscale(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-b" and validate_commands(sys.argv, 8):
        make_borders(sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]))
    elif sys.argv[1] == "-f" and validate_commands(sys.argv, 4):
        flipped(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-m" and validate_commands(sys.argv, 4):
        mirror(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-c" and validate_commands(sys.argv, 8):
        collage(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], int(sys.argv[7]))
    elif sys.argv[1] == "-y" and validate_commands(sys.argv, 7):
        background = Image(sys.argv[3])
        foreground = Image(sys.argv[2])
        outputFile = sys.argv[4]
        factor = float(sys.argv[6])
        threshold = int(sys.argv[5])
        greenScreen(foreground, background, outputFile, factor, threshold)
if __name__ == "__main__":
    main()