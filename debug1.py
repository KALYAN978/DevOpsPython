def double(n):
    return lambda a:a * n

cal = double(2)
print("Result: ",cal(4))