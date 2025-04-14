x = "awesome"
y = "A"

def myfunc():
    print(y)
    global x
    print("Python is " + x)
    x = "fantastic"

myfunc()

print("Python is " + x)



