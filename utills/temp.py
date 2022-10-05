res = []
for i in range(3):
    a = {'i': i}
    res.append(a)
    print(id(a))


print(res)
