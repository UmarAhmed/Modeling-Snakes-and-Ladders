' Simulates a game of snakes and ladders and produces a frequency graph '

import random
from matplotlib import pyplot as plt
 
snakes_and_ladders = {98:78, 95:75, 93:73, 87:24, 64:60, 62:10, 56:53, 49:11, 48:26, 16:6, 
		      80:100, 71:91, 28:84, 51:67, 21:42, 36:44, 9:31, 4:14, 1:38}
max_turns_per_game = 1000


# Simulates a single player game and returns how long it lasted
def play(sl=True):
    position = 0
    turns = 0
    while position < 100 and turns < max_turns_per_game:
        position += random.randint(1, 6)
        # Check for snakes and ladders
        if sl and position in snakes_and_ladders:
            position = snakes_and_ladders[position]
        turns += 1
    return turns


# Gets data on n games
def get_data(n, sl=True):
    data = [play() for _ in range(n)]
    freq = [data.count(i) for i in set(data)]
    data = list(set(data))
    mean = sum([data[i] * freq[i] for i in range(len(data))]) / n
    mode = data[freq.index(max(freq))]
    minimum = min(data)
    maximum = max(data)
    return {'data': data, 'freq': freq, 'mean': mean, 'mode': mode, 'max':
            maximum, 'min': minimum, 'iterations': n}


# Makes a probability graph, showing how often a game lasts n turns
def make_graph(dict_of_data):
    freq = dict_of_data['freq']
    total = dict_of_data['iterations']
    prob = [100 * (freq[i] / total) for i in range(len(freq))]
    plt.title('MC Simulation - Chance of a Game Ending in n Moves')
    plt.xlabel('Turns')
    plt.ylabel('Percent Chance')
    plt.plot(dict_of_data['data'], prob)
    plt.show()


def make_cum_graph(dict_of_data):
    freq = dict_of_data['freq']
    prob = [100 * (freq[i] / dict_of_data['iterations']) for i in
            range(len(freq))]
    cum_prob = [sum(prob[:i]) for i in range(len(freq))]
    plt.plot(dict_of_data['data'], cum_prob)
    plt.xlabel('Turns')
    plt.ylabel('Percent Chance')
    plt.title('MC Simulation - Cumulative Probability Distribution')
    plt.show()

