a = {"apple", "banana", "cherry"}
a.add("orange")             #Add a single value
print(a)

b = {"pineapple", "mango", "papaya"}
a.update(b)                 #Used to add another set
print(a)

mylist = ["kiwi", "orange"]
a.update(mylist)            #Addding a list
print(a)


a.remove("banana")
print(a)                    #Removes value of name

a.discard("apple")
print(a)                    #Discards memory of value

x = a.pop()                 #Deletes the first element
print(x)
print(a)

a.clear()                   #Clears the whole list
print(a)
del a                       #Deletes the list