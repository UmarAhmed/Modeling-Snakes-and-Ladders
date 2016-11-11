#Umar Ahmed - Math Ia - Python 3.5.2
import random
import collections
import matplotlib
z = [ ] 
snakes = {98:78,95:75,93:73,87:24,64:60,62:10,56:53,49:11,48:26,16:6}
ladders = {80:100, 71:91,28:84, 51:67, 21:42,36:44,9:31,4:14, 1:38}

def rollDice(): #This rolls a dice for the player
    roll = random.randint(1,6)
    return roll
        
    
def checkSL(n): #Checks if a certain space has a S/L
	if n in ladders:
		n = ladders[n]
	elif n in snakes:
		n = snakes[n]
	return n


def play(): 
    x = 0
    y = 0
    a = 0
    while x<100 and y<1000:
        x += rollDice()
        a = a +1
        x = checkSL(x)
        y = y+1
    z.append(y)
    b.append(a)
    
    
b = []

while len(z)<10000:
    play()


z.sort()
counter = collections.Counter(z)
# Counter({n-rolls:freq}) 

for key in counter:    
    counter[key] /= 100.0

#print(counter)
#print(sum(b))
w = counter.items()
import matplotlib.pyplot as plt

print(w)
plt.title('Percent chance of finishing a game in n-moves')
plt.xlabel('Number of Moves')
plt.ylabel('Percent Chance')
plt.plot(*zip(*w))
plt.show()

from matplotlib import pyplot as plt
plt.hist(w, cumulative=True)
