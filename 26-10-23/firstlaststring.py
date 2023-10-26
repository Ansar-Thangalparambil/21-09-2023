#create a string frim given string where first and last character exchanged


text=input("Enter a string")
newstring = text[-1]+text[1:-1]+text[0]
print('Newstring:',newstring)
