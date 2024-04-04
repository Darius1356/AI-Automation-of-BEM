# Correcting black spots in tiles
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import time, math, os, sys
from PIL import Image

callnum = 0
windowList, windowList2  = [], []
totalWindows, totalWindows2 = {}, {}

def convertToGreyscale(sketch):
    gray_img = sketch.convert('L')
    return np.array(gray_img)

def roundUp(x):
    return math.ceil(x / 1280.0) * 1280

def padDrawing(image):
    # Pad the image with 1280 pixels of white around the edges
    height, width = image.shape
    paddedWidth = roundUp(image.shape[1])
    paddedHeight = roundUp(image.shape[0])
    paddedDrawing = np.full([paddedHeight, paddedWidth], 255)
    paddedDrawing[:height, :width] = image
    return paddedDrawing

def traverse(image2):
    global callnum
    x = []
    y = []
    tilecount = 0
    # Create a temporary list to store the windows
    # Loop through the image in steps of 1280, creating adjacent 1280x1280 windows with slight 80 pixel overlap
    for i in range(0, image2.shape[0] - 1280, 1200):
        for j in range(0, image2.shape[1] - 1280, 1200):
            x.append(j)
            y.append(i)
            # Extract 1280x1280 window
            window = image2[i:i+1280, j:j+1280]
            windowList.append(window)
            tile = np.array(windowList)
            plt.imsave(r'C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Traversing Window\Tiles6\\' + str(callnum) + "_" + str(x[tilecount]) + "_" + str(y[tilecount]) + '.png', tile[tilecount], cmap=plt.cm.gray)
            tilecount = tilecount + 1
    callnum = callnum + 1

def main():
    time_start = time.time()
    folder_path = r'C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Traversing Window\Labelled SLDs'
    output_folder = r'C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Traversing Window\Tiles6'

    # Create the output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the folder
    count = 0
    for filename in os.listdir(folder_path):
        # Load the image
        print(os.path.join(folder_path, filename))
        drawing = Image.open(os.path.join(folder_path, filename))
        # Convert to greyscale
        greyscaleDrawing = convertToGreyscale(drawing)
        # Pad the image
        paddedDrawing = padDrawing(greyscaleDrawing)
        # Traverse the image and extract tiles
        traverse(paddedDrawing)
        windowList.clear()
        count = count + 1

    time_end = time.time()
    print("Runtime: ", round(time_end - time_start, 3), " seconds.")

if __name__ == "__main__":
    main()