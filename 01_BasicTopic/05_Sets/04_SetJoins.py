a = {1,2,3}
b = {'A','b','c',1}
z = {'P',1,'Q',2}

#Union can also join set and tuples
c = a.union(b)      #Union
print(c)

y = a.union(b,z)    #Multiple union
print(y)

d = a|b             #Union
print(d)

e = a.intersection(b)   #Intersect
print(e)

f = a&b                 #Intersect
print(f)

a.update(b)             #Works like union
print(a)

a = {1,2,3}

g=a.difference(b)       #Returns only value that are in set 1 and not in set 2
print(g)

h = a-b                 #Same as Difference
print(h)

i = a.symmetric_difference(b)   #Returns a union set of both uncommon values
print(i)

j = a^b                 #Same as Symetric Difference
print(j)

k = a<=b                #Sub Set
print(k)

l =a.issubset(b)        #Sub Set
print(l)

m = a.issuperset(b)     #Super Set
print(m)

n = a>=b                #Super Set
print(n)