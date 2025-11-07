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
    print(nums)
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

print(clampValueToRange(234.5, 0, 255))
print(clampValueToRange(-10, 100.5, 200))
print(clampValueToRange(500, 0, 200))

print(returnColor("1 2 3 4 5"))

print(returnLocation("1 2 3 4 5"))

print(locationValid(-1, 10, 0, 20))
print(locationValid(20, 10, 0, 20))
print(locationValid(-5, 10, 5, 20))
print(locationValid(0, 10, 2, 20))

print(convertPixel([-10, 100.5, 300]))
print(convertPixel([500, -5, 25.5]))

print(positionPixel(2, 3, {'r': 0, 'g': 100, 'b': 255}))

updateChangeList({'pixel': {'r': 0, 'g': 100, 'b': 255}, 'x': 2, 'y': 3}, [{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 4, 'y': 5}])

pixels = []
readPixelFile(pixels, "example.txt")
print("TESTING JGBUIAORHIPWOHFUIQOWIHDOIQHDBOIHQDIO")
print(pixels)