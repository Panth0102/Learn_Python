a = {
    "Key1" : "Value1",
    "Key2" : "Value2",
    "Key3" : "Value3"
}

b = a["Key1"]
print(b)

#Get Method
c = a.get("Key1")
print(c)

#Get only keys
d = a.keys()
print(d)

#Get only values
e = a.values()
print(e)

#Get key value pair
f = a.items()
print(f)