from random import randint
import matplotlib.pyplot as plt

record = [[0,0] for x in range(1000)]

its=200000
for iteration in range(its):
	houses = [100 for x in range(1000)]
	for h in range(1000):
		target = randint(0,998)
		target = 999 if h == target else target #ensure no house robs itself
		houses[h] += houses[target]
		houses[target] = 0
	winner = max(houses)
	for i in range(1000):
		record[i][1]+=houses[i]/its
		if houses[i] == winner:
			record[i][0]+=1.0/its

maxidx=0
for x in range(1000):
	if record[x][1]>=record[maxidx][1]:
		maxidx = x
print(maxidx, record[maxidx])
plt.plot([r[1] for r in record],'bo')
plt.xlabel('House #')
plt.ylabel('Expected winnings')
plt.show()

