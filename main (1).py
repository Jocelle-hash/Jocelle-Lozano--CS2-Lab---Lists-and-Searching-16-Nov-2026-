scores = []
total = 0
for i in range(5):
    score = int(input("please enter score: "))
    scores.append(score)

for s in scores:
    total = total + s
    
print("Total:", total)
print("Average:", total / len(scores))