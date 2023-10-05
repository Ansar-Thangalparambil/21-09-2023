a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if(a>b)&(a>c):
    print("First number is greater:",a)
elif(b>a)&(b>c):
    print("Second number is greater: ",b)
else:
    print("Third number is greater:",c)

