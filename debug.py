def commonFunction(value):
    return lambda a : a * value

DoubleIt = commonFunction(2)
TripleIt = commonFunction(3)

print(DoubleIt)
print(commonFunction(3))