"""
ascii.py
A python program that convert images to ASCII art.
"""
#Last name,Student Number
#_________, _________
#_________, _________
#_________, _________
#_________, _________

#Please rename this file with your last names before submission.

import argparse
import numpy as np
from PIL import Image

# START OF PART TWO (15%)-------------------------------------------------------------------------
def getAverageL(image):
    """
    Given PIL Image, return average value of greyscale value
    """
    # get input image as numpy array
    im = ____
    # get shape of array using shape 
    w,h = ____
    # get average of reshaped array
    return ______
# END OF PART TWO ----------------------------------------------------------------------------

def convertImageToAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images 
    """
    # START OF PART ONE (20%)----------------------------------------------------------------------
    
    # grey scale level values from: 
    # http://paulbourke.net/dataformats/asciiart/
    
    # 70 levels of grey - THIS CODE DOES NOT NEED TO BE EDITED
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # 10 levels of grey - THIS CODE DOES NOT NEED TO BE EDITED
    gscale2 = '@%#*+=-:. '

    # open image in given file path and convert to greyscale - THIS CODE DOES NOT NEED TO BE EDITED
    image = Image.open(fileName).convert('L')

    # store dimensions of image using size method (returns a list)
    W, H = image.size()
    print("input image dims: %d x %d" % (W, H))
    # compute width of tile/column
    w = _______
    # compute tile/row height based on aspect ratio and scale
    h = _______
    # compute number of rows - must be an integer value
    rows = ______

    # These print statements tell the user the dimensions of the image and of the tiles
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
    
    # check if image size is too small for given cols or rows
    if _______:
        print("Image too small for specified cols!")
        exit(0)
        
    # END OF PART ONE -----------------------------------------------------------------------

    # START OF PART THREE (20%)-------------------------------------------------------------------
    # ascii image is a list of character strings
    aimg = []

    # generate list of dimensions using nested for loop
    # y1 pattern: 0, h, 2h, 3h, ...; y2 pattern: h, 2h, 3h, 4h, ...
    for j in range(rows):
        y1 = ____
        y2 = ____
        # correct last tile
        if j == rows-1:
            y2 = H
        # append an empty string
        aimg.append("")
        for i in range(cols):
            # crop image to tile
            x1 = ____
            x2 = ____
            # correct last tile
            if i == cols-1:
                x2 = W
            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            # get average luminance of cropped tile (it should be an integer)
            avg = ________
            # look up ascii char by generating a string index based on avg
            if moreLevels:
                gsval = gscale1[int((avg*_)/255)]
            else:
                gsval = gscale2[int((avg*_)/255)]
            # append ascii char to string
            aimg[j] += gsval
    
    # return txt image as a list of strings (1 string = 1 row of text file)
    return aimg
    # END OF PART THREE ----------------------------------------------------------------------
    
# START OF PART FOUR (30%)-------------------------------------------------------------------------
def main():
    # creates a command line parser object using built-in argparse library
    descStr = "This program converts an image into ASCII art."

    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments - the first is completed for you as an example
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('____', dest='____', required=_____)
    parser.add_argument('____', dest='____', required=_____)
    parser.add_argument('____', dest='____', required=_____)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')

    # parse args, stores ALL user input as strings
    args = parser.parse_args()
    
    imgFile = args.imgFile
    # set default output file
    outFile = 'out.txt'
    # Check if the user entered an input for outFile
    if args.outFile:
        outFile = args.outFile  # Rewrite default value with user value
        
    # set scale default as 0.43 (scale should always be a float)
    scale = 0.43
    if ______:
        scale = ______
    # set default cols as 80 (cols should always be an int)
    cols = 80
    if ______:
        cols = ______

    print('generating ASCII art...')
    # convert image to ascii txt
    aimg = convertImageToAscii(imgFile, cols, scale, args.moreLevels)

    # open output file in write mode
    f = open(_____, 'w')
    # write to file using aimg and the for loop
    for ___ in ____:
        f.write(___ + '\n')
    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)
#END OF PART FOUR -----------------------------------------------------------------------------
    
#Please also submit your output file (out.txt) (15%)
    
# call main
if __name__ == '__main__':
    main()
