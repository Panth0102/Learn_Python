a = ('A','B','C')

(p,q,r) = a
print(p)
print(q)
print(r)

b = ('A','B','C','D','E','F')

# * assigning any extra value to *object
(x,*y,z) = b        
print(x)
print(y)
print(z)