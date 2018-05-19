import random
import collections
from matplotlib import pyplot as plt
 
snakes_and_ladders = {98:78, 95:75, 93:73, 87:24, 64:60, 62:10, 56:53, 49:11, 48:26, 16:6, 80:100, 71:91, 28:84, 51:67, 21:42, 36:44, 9:31, 4:14, 1:38}
max_turns_per_game = 1000


# Simulates a single player game
# What is a??
def play():
    position = 0
    turns = 0
    while position < 100 and turns < max_turns_per_game:
        position += random.randint(1, 6)
        # Check for snakes and ladders
    if position in snakes_and_ladders:
            position = snakes_and_ladders[position]
    turns += 1
	
    return turns


# Gets data on n games
def get_data(n):
    data = [play() for i in range(n)]
    freq_count = [i/100 for i in collections.Counter(data.sort())]
    return counter.items()
    
data = get_data(10000)     


plt.title('Percent chance of finishing a game in n-moves')
plt.xlabel('Number of Moves')
plt.ylabel('Percent Chance')
plt.plot(*zip(*data))
plt.show()


plt.hist(data, cumulative=True)
