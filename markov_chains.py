' Produces markov chain for snakes and ladders, calculates probabilities '
import numpy as np
import matplotlib.pyplot as plt 

snakes_and_ladders = {98:78, 95:75, 93:73, 87:24, 64:60, 62:10, 56:53, 49:11, 48:26, 16:6, 80:100, 71:91, 28:84, 51:67, 21:42, 36:44,  9:31, 4:14, 1:38}  

'''
def make_row(i):
    ' Returns an array of probabilities, where the element at index j is the probability of moving from square i to square j '
    ' Requires 0 <= i <= 100 '
    if i == 99: 
        return 81 * [0] + [1]
    elif i == 100:
        return [0] * 82
    elif i == 97:
        row = [0] * 78 + [1/6] + [0] * 20 + [1/6, 4/6]
    elif i == 96:
        row = [0] * 78 + [1/6] + [0] * 18 + [1/6, 0, 1/6, 3/6]
    else:
        row = [1/6 if (i < j < i + 7) else 0 for j in range(101)]
        for i in range(len(row)):
            if row[i] and i in snakes_and_ladders:
                row[snakes_and_ladders.get(i)] += 1/6
    return [row[j] for j in range(len(row)) if j not in snakes_and_ladders]


def make_efficient_matrix():
    ' Make a 82 x 82 right stochastic matrix '
    return np.array([make_row(i) for i in range(101) if i not in snakes_and_ladders])
'''

def get_matrix():
    ' Make a 101 x 101 left stochastic matrix '
    # Initialize matrix
    matrix = np.zeros((101, 101))
    for i in range(101):
        matrix[i + 1: i + 7, i] = (1 / 6)
    matrix[range(101), range(101)] += 1 - matrix.sum(0)
    # Make matrix to account for snakes and ladders
    sl_matrix = np.zeros((101, 101))
    positions = [snakes_and_ladders.get(i, i) for i in range(101)]
    sl_matrix[positions, range(101)] = 1
    # Return the product of the two matrices
    return sl_matrix @ matrix


def calc_prob(matrix, n, v): 
    ' Multiply vector with transition matrix to calculate probabilities '
    return (np.linalg.matrix_power(matrix, n) @ v)[-1] 


def make_graph(n):
    matrix = get_matrix()
    v = np.array([1] + [0] * 100)
    probs = [calc_prob(matrix, i, v) for i in range(n)]
    plt.plot(np.arange(1, n), np.diff(probs), color='blue')
    plt.xlabel('Turns')
    plt.ylabel('Probability')
    plt.title('Markov Chain Probability Distribution')
    plt.show()


def get_expected_dist():
    # E(k) = (I + M + M**2 + ...)[1] = (I - M)**-1[1]
    matrix = get_matrix()
    one = np.array([1] * 100)
    expected_dist =  np.linalg.inv(np.identity(100) - matrix[:100, :100]).T @ one
    return expected_dist
