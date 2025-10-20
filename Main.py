def clampValueToRange(value, low, high) :
    if value < low :
        return int(low)
    elif value > high :
        return int(high)
    else :
        return int(value)

print(clampValueToRange(234.5, 0, 255))
print(clampValueToRange(-10, 100.5, 200))
print(clampValueToRange(500, 0, 200))