

from PIL import Image




def main():

    nameof= "ttt.png"

    cols = int(80)

    scale = float(0.32)

    image = convert(nameof, cols, scale, moreLevels)







def convert(fileName, cols, scale, moreLevels):

    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # 10 levels of grey - THIS CODE DOES NOT NEED TO BE EDITED
    gscale2 = '@%#*+=-:. '

    # open image in given file path and convert to greyscale - THIS CODE DOES NOT NEED TO BE EDITED
    image = Image.open(fileName).convert('L')

    '''

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
    '''
    
    return(1)

