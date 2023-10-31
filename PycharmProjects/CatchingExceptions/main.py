#FileNotFound

try:
    file = open("a_file.txt")  #opening a file with the openfunction
    a_ditionary = {"key":"value"}
    value = a_ditionary["dashdk"]
# except:
#     file = open("a_file.txt","w")  #"w" = write mode --> It will create the file
#     file.write("something")
except FileNotFoundError:
    file = open("a_file.txt","w")  #"w" = write mode --> It will create the file
    file.write("something")
# except KeyError:
#     print("That entered key doesnot exist")
except KeyError as error_message:  #we are printing the error as error message
    print(f"That entered key {error_message} doesnot exist")
else:
    content = file.read()
    print(content)
# finally:
#     file.close()  #we are closing the file manually bcoz we didnt use with open function
#     print("File was closed")  #file has closed apart from with or without execution of except and else

finally :
    #raise KeyError
    raise TypeError("This is an error that i made up.")