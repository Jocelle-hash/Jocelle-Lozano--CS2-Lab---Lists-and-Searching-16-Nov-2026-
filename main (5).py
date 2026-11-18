
votes = []
entry = input("Vote (or done): ")
while entry != "done":
    votes.append(entry)
    entry = input("Vote (or done): ")


search = input("Which candidates votes do you want to see: ")
def count(items,search):
    total = 0
    for i in range(len(votes)):
        if votes[i] == search:
         total += 1
    return total

total = count(votes,search)
print(search, "has", total, "votes")



    

