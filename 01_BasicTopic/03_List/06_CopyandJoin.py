a = ['A','B','C','D','E']

#Copy Methods
print(a)
b = a.copy()
print(b)

c = list(a)
print(c)

d = a[:]
print(d)

p = ['a','b','c']
q = [1,2,3]

#Join methods
r = p + q
print(r)

for i in q:
    p.append(q)

print(p)

p = ['a','b','c']
p.extend(q)
print(p)