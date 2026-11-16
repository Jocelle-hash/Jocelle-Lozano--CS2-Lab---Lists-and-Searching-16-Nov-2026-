
entry = input("Name (or done): ")
Names = []

while entry != "done":
    Names.append(entry)
    entry = input("Name (or done) ")

search = input("find a name: ") 
def find(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return target  + "is member number"  + str(i + 1)
    return search  + "is not a member"

print(find(Names, search))
