a = int(input("Enter the first No:"))
b = int(input("Enter a second No:"))

if (a>b):
    min = a
else:
    min = b
    
while (1):
    if(min % a == 0 and min % b == 0):
        print("lcm is: " + min)
        break
    min = min + 1