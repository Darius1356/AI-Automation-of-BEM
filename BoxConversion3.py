import os, matplotlib.pyplot as plt, numpy as np, math
from PIL import Image

def openImage(filename):
    global drawing, original_X, original_Y
    drawing = Image.open(os.path.join(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\SLDs\\" + filename))
    original_X, original_Y = drawing.size
    drawing = drawing.convert('L')
    drawing = np.array(drawing)

def openLabel():
    # Create a list of lists to store the labels of bounding boxes
    global features
    features = []
    label = open(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\Labels\\" + labels[count], "r") 
    print(labels[count])
    content = label.read()
    CoList = content.split("\n")
    for i in range(len(CoList)-1):
        line = CoList[i].split(" ")
        features.append(line)
    return features
        
def fetchPixels(features):
    global x, y, width, height
    x = float(features[1]) * original_X
    y = float(features[2]) * original_Y
    width = math.floor(float(features[3]) * original_X)
    height = math.floor(float(features[4]) * original_Y)

def findTile():
    global X, Y, tileOriginX, tileOriginY, title
    # Find the tile
    tileOriginX = (math.floor(x/1200) * 1200)
    tileOriginY = (math.floor(y/1200) * 1200)
    X = math.floor(x - tileOriginX)
    Y = math.floor(y - tileOriginY)
    title = str(count) + "_" + str(tileOriginX) + "_" + str(tileOriginY)
    #print(X,Y)

def saveBoundingBox():
    global txt
    # Convert to percentage
    xBB = X/1280
    yBB = Y/1280
    # Save bounding box
    part = np.ascontiguousarray(drawing[math.floor(y-height/2):math.floor(y+height/2), math.floor(x-width/2):math.floor(x+width/2)])
    plt.imsave(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\test" + str(n) + ".png", part, cmap='gray') 
    #print(X, width, Y, height)
    if (x+width/2) < (tileOriginX+1280) and (x-width/2) > tileOriginX and (y+height/2) < tileOriginY and (Y-height/2) > tileOriginY:
        txt = str(features[n][0]) + " " + str(xBB) + " " + str(yBB) + " " + str(features[n][3]) + " " + str(features[n][4])
        print(X-width)
    else:
        txt = ""
    
def openNewLabels():
    num = 0
    sizes = [1,1,1,0,0,0,0,0,0,0,1,1,1,1]
    for size in sizes:
            if size == 1:
                for i in range(0, 8400, 1200):
                    for j in range(0, 6000, 1200):
                        name = str(num)+"_"+str(i)+"_"+str(j)
                        open(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\newLabels/" + name +".txt", "w")
            else:   
                for i in range(0, 6000, 1200):
                    for j in range(0, 3600, 1200):
                        name = str(num)+"_"+str(i)+"_"+str(j)
                        open(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\newLabels/" + name +".txt", "w")
            num = num + 1

    
def main():
    global count, n, labels
    count = 0
    folderPath = r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\SLDs"
    labels = os.listdir(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\Labels")
    openNewLabels()
    for SLD in os.listdir(folderPath):
        n = 0
        openImage(SLD)
        features = openLabel()
        for label in features:
            fetchPixels(label)
            findTile()
            saveBoundingBox()
            f = open(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\newLabels/" + title + ".txt", "a")
            f.write(txt + "\n")
            f = open(title + ".txt", "a")
            n = n + 1
        count = count + 1

        
if __name__ == "__main__":
    main()

# TEST Accuracy of the centre
#n = n + 1
#tile = Image.open(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\Tiles\0_" + str(tileOriginX) + "_" + str#(tileOriginY) + ".png")
#tile = np.array(tile)
#part = np.ascontiguousarray(tile[math.floor(Y-height/2):math.floor(Y+height/2), math.floor(X-width/2):math.floor(X+width/2)])
#plt.imsave(r"C:\Users\dariu\Documents\UCL\3rd Year\Project\Image Processing\Object Labelling\Bounding Box Conversion\test" + str(n) + ".png", part) 