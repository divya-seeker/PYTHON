range1=range(10)       # 0---9 with gap 1
range2=range(5,10)     # 5---9 with gap 1
range3=range(2,9,2)    # 2---8 with gap 2
print(list(range3))

for x in range(10):
    print(2**x,end=" ")

print()

names=["Divya","Dharm","Shaurya","Manish"]
for name in names:
    print(name,end=",")

print()

#while loop
n=6
while n>=0:
    print(n , end=",")
    n=n-1
