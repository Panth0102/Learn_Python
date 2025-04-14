a= ['A','B','C','D','E','F','G']

a[1] = 'P'
print(a)        #['A', 'P', 'C', 'D', 'E', 'F', 'G']

a[2:5] = ['Q','R','S']
print(a)        #['A', 'P', 'Q', 'R', 'S', 'F', 'G']


#Insert at a Index
a.insert(2,'Z')
print(a)         #['A', 'P', 'Z', 'Q', 'R', 'S', 'F', 'G']

#Adds at end
a.extend('Y')
print(a)    #['A', 'P', 'Z', 'Q', 'R', 'S', 'F', 'G', 'Y']


#Removes
a.remove('P')
print(a)    #['A', 'Z', 'Q', 'R', 'S', 'F', 'G', 'Y']

#Pop element at index
a.pop(1)
print(a)    #['A', 'Q', 'R', 'S', 'F', 'G', 'Y']

#Appending Lists
b=[1,2,3]
a.append(b)
print(a)

#Deleting a value at index
del a[0]
print(a)    #['Q', 'R', 'S', 'F', 'G', 'Y']

#Deleting entire list
del a
# print(a)    #Returns error as no list exsit

a= ['a','b','c']

#Clearing list - Makes list empty
a.clear()
print(a)    