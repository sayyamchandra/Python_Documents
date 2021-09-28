name =  input("Enter the file name")
try:
    handle = open(name)
    for line in handle:
        print(line)

except:print("FILE_NOT_FOUND")
