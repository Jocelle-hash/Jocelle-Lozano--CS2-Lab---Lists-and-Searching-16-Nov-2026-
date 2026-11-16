
n = int(input("how many names? "))
names = []
for i in range(n):
    name = input("enter names ")
    names.append(name)

print(names,)
print(len(names), "names stored")