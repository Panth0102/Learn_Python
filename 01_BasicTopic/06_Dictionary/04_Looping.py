a = {
    "Key1" : "Value1",
    "Key2" : "Value2",
    "Key3" : "Value3"
}

#Basic for loop #returns keys
for i in a:
    print(i)

for i in a.keys():
    print(i)

#Returns only value
for i in a:
    print(a[i])

for i in a.values():
    print(i)

#returns key-value pair
for i,j in a.items():
    print(i,j)