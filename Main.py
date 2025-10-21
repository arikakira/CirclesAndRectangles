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

print(clampValueToRange(234.5, 0, 255))
print(clampValueToRange(-10, 100.5, 200))
print(clampValueToRange(500, 0, 200))

print(returnColor("1 2 3 4 5"))

print(returnLocation("1 2 3 4 5"))

print(locationValid(-1, 10, 0, 20))
print(locationValid(20, 10, 0, 20))
print(locationValid(-5, 10, 5, 20))
print(locationValid(0, 10, 2, 20))