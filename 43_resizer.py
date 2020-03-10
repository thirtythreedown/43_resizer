#! python3

##Analyzes the dimensions ratio of a picture and, if it's not 4:3, adds a light grey padding to fix the ratio.

import os
from PIL import Image
os.makedirs('resized_pictures', exist_ok=True)

def dimensions_getter(inputImage):
    """Collects the dimensions from an input image"""
    imWidth_local, imHeight_local = inputImage.size
    return imWidth_local, imHeight_local

def ratio_checker(imWidth, imHeight, targetRatio):
    """Compares the dimensions ratio of an input image against a provided ratio"""
    imRatio = imWidth/imHeight
    if imRatio == targetRatio:
        return True
    else:
        return False

def widthPadding(inputIm, imWidth, imHeight, targetRatio):
    """Creates a background padding to extend the dimensions of a picture to a 4:3 ratio"""
    print("Padding for height!")
    newHeight = int(imWidth/targetRatio)
    heightPadding = Image.new('RGB', (imWidth,newHeight), 'lightgrey')
    outputIm_local = heightPadding.copy()
    outputIm_local.paste(inputIm, (0,(int((newHeight-imHeight)/2))))
    return outputIm_local

def heightPadding(inputIm, imWidth, imHeight, targetRatio):
    print("Padding for width!")
    newWidth = int(imHeight*targetRatio)
    widthPadding = Image.new('RGB', (newWidth, imHeight), 'lightgrey')
    outputIm_local = widthPadding.copy()
    outputIm_local.paste(inputIm, ((int((newWidth-imWidth)/2),0)))
    return outputIm_local

def output_saver(outputIm):
    outputIm.save(os.path.join('resized_pictures', filename + '_resized.jpg'), quality=95)
    print("Output picture saved!")

for filename in os.listdir('.'):
    ##Cycling through every file in the folder, skipping non-picture files based on filetype.
    if not (filename.endswith('.bmp') or filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.webp')):
        continue

    ##Comparing each file's ratio against the 4:3 ratio 
    inputIm = Image.open(filename)
    imWidth, imHeight = dimensions_getter(inputIm)
    targetRatio = (4/3)
    ratio_check = ratio_checker(imWidth, imHeight, targetRatio)

    ##Copying the picture to the target folder if ratio is 4:3
    if ratio_check == True:
        print("This picture is already the right size! Let's just move it over.")
        output_saver(inputIm)

    ##Padding the picture if ratio different from 4:3
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
