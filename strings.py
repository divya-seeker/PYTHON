word="Divya"

#Error 
#para="I 
#am 
#Divya
#Dwivedi"

#MultiLine Strings
para='''I 
am 
Divya
Dwivedi'''

print(para)

print(word[3],word[-2])
print("Last letter :",word[-1])

word2="campore"
#Slicing
print(word2[1:5])
print(word2[:4])
print(word2[4:])
print(word2[0:5:2])

#Reversing
print(word2[::-1])
print(word2[5:1:-1])

#adding a string 
a="Hii Bro "
b="Hello"
print(a+b)
print(a*3)

# Loop over String
for charc in a:
    print(charc,end=" ")

c="23"
# is alphabet and isDigit
print(a.isalpha())
print(b.isalpha())
print(c.isdigit())
print(a.islower())

# Trimming
a="   Hi,Prayag    "
print(a,end=" ")
print(a.rstrip(),end=" ")
print(a.lstrip(),end=" ")







