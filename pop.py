a = [1, 2, 3]
index = int(input("index -> "))

for i, e in enumerate(a):
    if i == index:
        del a[i]
        print(a)
        exit()