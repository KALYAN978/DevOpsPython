numbers = [1,3,4,5,6,7,8,9]
result = filter(lambda x:x<5,numbers)
print("Numbers smaller than 5 in the list are: ")
print(list(result))