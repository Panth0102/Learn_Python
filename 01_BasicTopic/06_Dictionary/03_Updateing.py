a = {
    "Key1" : "Value1",
    "Key2" : "Value2",
    "Key3" : "Value3"
}

#Changes value
print(a)
a["Key1"] = "valueN"
print(a)

a.update({"Key3":"Value12"})
print(a)

#Adding value
a["Key4"] = "Value4"
print(a)

#Popping value excepts a argument
a.pop("Key2")
print(a)

#Popitem removes last value
a.popitem()
print(a)

#deleting a item
del a["Key3"]
print(a)

#Copy 
b = a.copy()
print(b)

c = dict(b)
print(c)

#Clear
a.clear()
print(a)

#del the dictionary
del a