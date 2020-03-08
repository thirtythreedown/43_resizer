#! python3

##RESOURCES
##Automate the boring stuff p.403 - Adding a logo project
##PILLOW documentation - https://pillow.readthedocs.io/en/3.1.x/reference/Image.html (see Constructing Images)
##Python colors constants list - https://www.webucator.com/blog/2015/03/python-color-constants-module/
##https://github.com/python-pillow/Pillow/issues/2164
##Paste image into another with PILLOW - https://note.nkmk.me/en/python-pillow-paste/
##Looping over files in a folder - https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

import os
##Importing the os library
from PIL import Image
##Importing Image function from PIL library
os.makedirs('resized_pictures', exist_ok=True)
##Creating a folder to store resized pictures

def dimensions_getter(inputImage):
    """Collects the dimensions from an input image"""
    imWidth_local, imHeight_local = inputImage.size
    return imWidth_local, imHeight_local

def ratio_checker(imWidth, imHeight, targetRatio):
    """Compares the dimensions ratio of an input image against a 4:3 ratio"""
    imRatio = imWidth/imHeight
    if imRatio == targetRatio:
        return True
    else:
        return False

def widthPadding(inputIm, imWidth, imHeight, targetRatio):
    """Creates a background padding to extend the dimensions of a picture to a 4:3 ratio"""
    print("Padding for height!")
    newHeight = int(imWidth/targetRatio)
    ##Deriving correct height from the imWidth and targetRatio variables
    ##print("The padding height is " + str(newHeight))
    ##print("The padding width is " + str(imWidth))
    heightPadding = Image.new('RGB', (imWidth,newHeight), 'lightgrey')
    ##Defining characteristics for the padding and creating it
    outputIm_local = heightPadding.copy()
    ##Copying heightPadding image
    ##print("Copying the padding!")
    outputIm_local.paste(inputIm, (0,(int((newHeight-imHeight)/2))))
    ##print("Output picture assembled!")
    ##Pasting testIm in the center of the padding
    return outputIm_local

def heightPadding(inputIm, imWidth, imHeight, targetRatio):
    print("Padding for width!")
    newWidth = int(imHeight*targetRatio)
    ##print("The padding width is " + str(newWidth))
    ##print("The padding height is " + str(imHeight))
    widthPadding = Image.new('RGB', (newWidth, imHeight), 'lightgrey')
    ##print("Created the padding")
    ##Defining characteristics for the padding and creating it
    outputIm_local = widthPadding.copy()
    ##print("Copying the padding")
    ##Copying widthPadding image
    outputIm_local.paste(inputIm, ((int((newWidth-imWidth)/2),0)))
    ##print("Output picture assembled!")
    ##Pasting testIm in the center of the padding
    return outputIm_local

def output_saver(outputIm):
    outputIm.save(os.path.join('resized_pictures', filename + '_resized.jpg'), quality=95)
    print("Output picture saved!")

for filename in os.listdir('.'):
    ##Cycling through every file in the folder
    if not (filename.endswith('.bmp') or filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.webp')):
        continue # Skipping files that are not bmp, jpg, png or webp

    ##Loading the first filename into the filename variable
    inputIm = Image.open(filename)
    ##Opening the picture attached to filename as testIm
    imWidth, imHeight = dimensions_getter(inputIm)
    ##Loading the dimensions of testIm and attributing width and size to the imWidth and imHeight variables
    ##print(imWidth, imHeight)
    ##Printing the collected dimensions from testIm image
    targetRatio = (4/3)
    ratio_check = ratio_checker(imWidth, imHeight, targetRatio)
##    print("The source picture ratio is " + str(imRatio))
##    print("The target picture ratio is " + str(targetRatio))
    if ratio_check == True:
        print("This picture is already the right size! Let's just move it over.")
        output_saver(inputIm)
    if ratio_check == False:
        print("This is not 4:3 standard!. Let's adjust for that!")
        if imHeight < imWidth:
            outputIm = widthPadding(inputIm, imWidth, imHeight, targetRatio)
            ##outputIm.show()
        if imWidth < imHeight:
            outputIm = heightPadding(inputIm, imWidth, imHeight, targetRatio)
            ##outputIm.show()
        output_saver(outputIm)
        ##Saving output picture to the target folder
print("All done!")
