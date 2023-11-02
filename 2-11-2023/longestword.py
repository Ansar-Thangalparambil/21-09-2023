#Accept a list of word and return longest word
def longestword(lis):
    max1 = len(lis[0])
    temp=lis[0]
    for i in lis:
        if(len(i) > max1):
            max1= len(i)
            temp=i
    print("Longest word is ",temp)

lis=[]
n=int(input("Enter the size"))
for i in range(0,n):
    a=input("Enter the words")
    lis.append(a)

longestword(lis)
    
