#Accept a filename  from user and print extension of that

a=input("Enter the file name")
if '.' in a :
    b=a.split(".")
    print(b)
    print(b[1])
else:
    print("Format is wrong")
