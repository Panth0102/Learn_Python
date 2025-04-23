i = 1
while i < 6:
    print(i)
    i += 1

#break
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1


#continue
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
