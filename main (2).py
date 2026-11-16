scores = []
count = 0
for i in range(5):
    score = int(input("please enter score: "))
    scores.append(score)

for s in scores:
    if s >= 75:
        count = count + 1

print(count, "of 5 passed")