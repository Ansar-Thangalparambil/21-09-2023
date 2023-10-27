#Create a list of colors from comma seperated color names  entered by user .Display the last colors

a=input("Enter the colors (use,for seperation)\n")
b=a.split(",")
print(b[0],b[-1])
