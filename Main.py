def clampValueToRange(value, low, high) :
    if value < low :
        return int(low)
    elif value > high :
        return int(high)
    else :
        return int(value)

def returnColor(line) :
    result = line.split()
    for i in range(len(result)) :
       result[i] = int(result[i])
    result = result[:3]
    return result

def returnLocation(line) :
    result = line.split()
    for i in range(len(result)) :
       result[i] = int(result[i])
    result = result[3:]
    return result

def locationValid(x, width, y, height) :
    return (x >= 0 and y >= 0) and (x < width and y < height)

def convertPixel(color) :
    result = {}
    nums = []
    for i in range(len(color)) :
        val = clampValueToRange(color[i], 0, 255)
        nums.append(val)
    result["r"] = nums[0]
    result["g"] = nums[1]
    result["b"] = nums[2]
    return result

def positionPixel(x, y, color) :
    result = {}
    result["pixel"] = color
    result["x"] = x
    result["y"] = y
    return result

def updateChangeList(pixel, pixelList) :
    pixelList.append(pixel)

def readPixelFile(pixels, filename) :
    with open(filename, "r") as info :
        for line in info :
            rgbList = returnColor(line)
            rgbDict = convertPixel(rgbList)
            xANDy = returnLocation(line)
            updateChangeList(positionPixel(xANDy[0], xANDy[1], rgbDict), pixels)

def generateEmptyPicture(width, height):
    img = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(convertPixel([0, 0, 0]))
        img.append(row)
    return img

def insertPixelList(pixels, image):
    for px in pixels:
        if locationValid(px["x"], len(image[0]), px["y"], len(image)):
            image[px["y"]][px["x"]] = px["pixel"]

def writePPM(image, filename):
    height = len(image)
    width = len(image[0])
    with open(filename, "w") as f:
        f.write("P3\n")
        f.write(str(width) + " " + str(height) + "\n")
        f.write("255\n")
        for y in range(height):
            for x in range(width):
                f.write(str(image[y][x]["r"]) + " ")
                f.write(str(image[y][x]["g"]) + " ")
                f.write(str(image[y][x]["b"]) + " ")
            f.write("\n")

def addCircleToList(x, y, r, color, pixels):
    for yVal in range(y - r, y + r + 1):
        for xVal in range(x - r, x + r + 1):
            if (yVal - y) ** 2 + (xVal - x) ** 2 <= r ** 2:
                px = {}
                px["x"] = xVal
                px["y"] = yVal
                px["pixel"] = color
                pixels.append(px)

def addRectangleToList(x1, x2, y1, y2, pixel, pixels):
    if x1 < x2:
        for xVal in range(x1, x2 + 1):
            if y1 < y2:
                for yVal in range(y1, y2 + 1):
                    px = {}
                    px["x"] = xVal
                    px["y"] = yVal
                    px["pixel"] = pixel
                    pixels.append(px)
            else:
                for yVal in range(y2, y1 + 1):
                    px = {}
                    px["x"] = xVal
                    px["y"] = yVal
                    px["pixel"] = pixel
                    pixels.append(px)
    if x2 < x1:
        for xVal in range(x2, x1 + 1):
            if y1 < y2:
                for yVal in range(y1, y2 + 1):
                    px = {}
                    px["x"] = xVal
                    px["y"] = yVal
                    px["pixel"] = pixel
                    pixels.append(px)
            else:
                for yVal in range(y2, y1 + 1):
                    px = {}
                    px["x"] = xVal
                    px["y"] = yVal
                    px["pixel"] = pixel
                    pixels.append(px)

def yourPictureFunction():
    im1=generateEmptyPicture(150,100)

    pixels=[]
    addRectangleToList(100, 130, 80, 95, convertPixel([255, 0, 0]), pixels) # red rectangle
    addRectangleToList(10, 25, 50, 80, convertPixel([0,255,0]), pixels)   # left rectangle
    addRectangleToList(10, 120, 80, 70, convertPixel([0,255,0]), pixels) # bottom rectangle
    addRectangleToList(120, 135, 80, 50, convertPixel([0,255,0]), pixels) # right rectangle
    addCircleToList(40, 30, 15, convertPixel([111, 230, 178]), pixels)  # blue green
    addCircleToList(100, 40, 15, convertPixel([76, 36, 156]), pixels)    # ourple
    addRectangleToList(35, 45, 25, 35, convertPixel([10, 25, 125]), pixels) # blue rectangle in circle
    insertPixelList(pixels,im1)
    writePPM(im1,"im1.ppm")

print("clampValueToRange")
print(clampValueToRange(234.5, 0, 255))
print(clampValueToRange(-10, 100.5, 200))
print(clampValueToRange(500, 0, 200))

print("returnColor")
print(returnColor("1 2 3 4 5"))

print("returnLocation")
print(returnLocation("1 2 3 4 5"))

print("locationValid")
print(locationValid(-1, 10, 0, 20))
print(locationValid(20, 10, 0, 20))
print(locationValid(-5, 10, 5, 20))
print(locationValid(0, 10, 2, 20))

print("convertPixel")
print(convertPixel([-10, 100.5, 300]))
print(convertPixel([500, -5, 25.5]))

print("positionPixel")
print(positionPixel(2, 3, {'r': 0, 'g': 100, 'b': 255}))

print("updateChangeList")
updateChangeList({'pixel': {'r': 0, 'g': 100, 'b': 255}, 'x': 2, 'y': 3}, [{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 4, 'y': 5}])

print("readPixelFile")
pixels = []
readPixelFile(pixels, "example.txt")
print(pixels)

print("generateEmptyPicture")
print(generateEmptyPicture(2,3))

print("insertPixelList")
test = generateEmptyPicture(2,3)
insertPixelList([{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 0, 'y': 0}, {'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 1, 'y': 1}], test)
print(test)
test = generateEmptyPicture(2,3)
insertPixelList([{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x':-1, 'y': 0}, {'pixel': {'r': 4, 'g': 5, 'b': 6}, 'x': 1, 'y': 0}], test)
print(test)

print("generateEmptyPicture")
test = generateEmptyPicture(3, 4)
print(test)
writePPM(test, "image.ppm")

print("addCircleToList")
test = []
addCircleToList(0, 0, 2, {"r": 1, "g": 1, "b": 1}, test)
print(test)
print("TESTING")
test = [{'pixel': 59, 'x': {'r': 63, 'g': 82, 'b': 255}, 'y': 89}]
addCircleToList(2, 1, 5, {'r': 60, 'g': 161, 'b': 77}, test)
print(test)

print("addRectangleToList")
test = []
addRectangleToList(0, 2, 1, 2, {"r": 1, "g": 1, "b": 1}, test)
print(test)

yourPictureFunction()