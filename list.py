#declaration
my_list=["Divya",2,"Hoo  ",[2,7,"g"],"Divya",True,"Love",2+9j]
print(my_list[-1])
print(my_list[1])

#sublist
print(my_list[2:7:2])

#reverse
print(my_list[::-1])

#List is mutable
my_list[1]=10
print(my_list)

#Deletion of element
del my_list[3]
print(my_list)

#Deletion of list
del my_list

#List comprehension
a=[2*x for x in range(1000) if x%7==0 and x%3==0]
print(a)

#Append
a.append("Divya")
a.insert(1,"Hare Krishna")
print(a)
 
#sort
b=[7,33,2,7,9,-1,0]
b.sort()
print(b)

# pop and reverse func and count,index
print(b.pop())
b.reverse()
print("Reversed",b)
print("Count of 7:",b.count(7))
print("Index of 0:",b.index(0))

#length and sum of array
print("Length:",len(b))
print("maximum in array:",max(b))
print("Sum of array:",sum(b))
