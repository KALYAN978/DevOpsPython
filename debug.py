class MyNumbers:
    
    def __iter__(self):
        self.a = 1     #initializing a attribute a to 1
        return self
    
    def __next__(self):   #we are getting the next item in the iteration
        x = self.a        #self.a represents current number in the sequence & starts at 1
        self.a += 1     
        return x         # previous value before incrementing is the "next" value in the iteration.         
    

numbers = MyNumbers()
myiter = iter(numbers)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))