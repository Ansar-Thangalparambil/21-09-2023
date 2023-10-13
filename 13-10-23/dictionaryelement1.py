#To generate and print a dictionary thth contains an element b/w 1&n (x,x*x)

n=int(input("Type a number"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
