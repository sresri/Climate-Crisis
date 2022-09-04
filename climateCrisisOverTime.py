import cv2 as cv
import sys
import numpy as np
from cv2 import destroyAllWindows


forestImgs = ["2000.jpeg","2005.jpeg","2008.jpeg","2012.jpeg","2016.jpeg","2019.jpeg"]
for img in forestImgs:
    img = cv.imread(img)

    if img is None:

        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)
    counts = {
        "g" : 0,
        "b" : 0,
        "r" : 0
    }

    for l in range(0,720):
        for w in range(0,800):
            b,g,r = (img[w,l])
            if g > r and g > b and g <= 80:
                counts["g"] += 1
            elif (b > g and b > r) or g > 80:
                counts["b"] += 1
            else:
                counts["r"] += 1
  


    top = counts["g"]
    bottom = counts["r"]+counts["b"]
    print(str((top/(top+bottom))*100)+"%")

lakeImages = ["lakeBefore.jpeg","lakeAfter.jpeg"]
for img in lakeImages:
    img = cv.imread(img)

    if img is None:

        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)
    counts = {
        "g" : 0,
        "b" : 0,
        "r" : 0
    }

    for l in range(0,1600):
        for w in range(0,1149):
            b,g,r = (img[w,l])
            if g > r and g > b:
                counts["g"] += 1
            elif (b > g and b > r):
                counts["b"] += 1
            else:
                counts["r"] += 1


    top = counts["b"]+counts["g"]
    bottom = counts["r"]
    print(str((top/(top+bottom))*100)+"%")
