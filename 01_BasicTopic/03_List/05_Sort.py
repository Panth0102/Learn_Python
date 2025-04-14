a = ['B','A','E','D','C']

#Ascending soret, it alpha numberic
a.sort()
print(a)

b = [10,5,1,3,7,9,2,4]
b.sort()
print(b)

#Not possible with multiple datatypes
# c = ['B','A','E','D','C',10,5,1,3,7,9,2,4]
# c.sort()
# print(c)

#Reverse Sort
b.sort(reverse=True)
print(b)


a.reverse()
print(a)

#Sorts Upeer case first, looks on Ascii value
d = ['a','B','c','d','E']
d.sort()
print(d)

#Need to do this for case insensitive
d.sort(key= str.lower)
print(d)