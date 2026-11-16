
names = []

enter = input("Name (done to stop): ")
while enter != "done":
    names.append(enter)
    enter = input("Name (done to stop): ")
print(names)