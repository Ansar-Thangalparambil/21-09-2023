list=['ansar','shamas','shafeen','shahala','vinayak']
count=0
a='a'

print(list)
for i in list:
    for f in i:
        if (f == a):
            count=count+1;

print("The number of ",a,"in",list,"is",count)
