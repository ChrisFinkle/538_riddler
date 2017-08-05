import random
numPlayers = 31

winners = [0 for w in range(0,numPlayers)]
turns = 0

for i in range(10000):
	t = 0
	students = [0 for s in range(numPlayers)]
	potato = numPlayers//2
	students[potato] = 1
	while sum(students) < numPlayers-1:
		lr = random.choice([-1,1])
		potato = (potato + lr) % numPlayers
		students[potato] = 1
		t += 1
	winner = students.index(0)
	winners[winner] += 1
	turns += t

print(turns/10000)
print(winners)
