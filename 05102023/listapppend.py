#Program to generate positive list of number from a given lis of integers

list=[-3,7,6,8,9,-8,-7]
n=[]
for i in list:
    if i > 0:
        n.append(i)

print(n)
