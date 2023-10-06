a=[]
n=int(input("Enter the list size"))
c="overlimit"
for i in range(0,n):
    element = int(input("Enter the elements of the list"))
    if element<100:
        a.append(element)
    else:
        a.append(c)

print(a)
