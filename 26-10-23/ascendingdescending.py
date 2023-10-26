#sort a dictionary in ascending order and descending order
import operator
dict={1:2,5:4,4:3,2:1,0:0}
print("Original dictionary",dict)
sorted_dict=sorted(dict.items(),key=operator.itemgetter(1))
print("Ascending order ",sorted_dict)
sorted_dict =sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
print("Descending order by :",sorted_dict)
