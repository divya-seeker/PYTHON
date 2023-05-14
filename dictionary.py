marks={
    "Arun":23,
    "Anant":37,
    "Divyansh":39,
    "Divya":37,
    "Divyanshi":38
}
print(marks)
print(marks["Divya"])
for x in marks:
    print(x,marks[x])

#Mutable
marks["Anant"]=40
#Adding
marks["Samay"]=41
print(marks)