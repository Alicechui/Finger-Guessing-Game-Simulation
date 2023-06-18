"""
 Project: Finger Guessing Game Simulation
 The project aims to simulate 10,000 games between two players, P1 and P2, following specific rules. 
 The players simultaneously show and guess the number of fingers the other player will display. 
 Based on their correct or incorrect guesses, winnings are calculated and plotted in a histogram to visualize the distribution of P1's winnings.
 Author: Alice Chui

"""
import numpy as np
import matplotlib.pyplot as plt

# random number generator
rng = np.random.default_rng()


def get_move():
    """
    Generate a player move represented as a list of length 2. The first element
    of the list is the number of fingers shown, and the second element is the
    number of fingers guessed. Both values are chosen independently and at random.

    :return: a list of length 2 representing a player's random move [fingers shown, fingers guessed]
    """
    rints = rng.integers(low=1, high=3, size=2)
    return list(rints)


def get_outcome(p1_move, p2_move):
    """
    Determine the winner and the sum of fingers shown in one game.

    :param p1_move: a list of length 2 representing player1 fingers [shown, guessed]
    :param p2_move: a list of length 2 representing player2 fingers [shown, guessed]
    :return: the winner (1, 2, 0 for no winner) and the sum of fingers shown
    """
    sum = p1_move[0]+p2_move[0]
    if p1_move[0] == p2_move[1] and p1_move[1] == p2_move[0]:
        return (0,sum)
    elif p1_move[0] != p2_move[1] and p1_move[1] != p2_move[0]:
        return (0,sum)
    elif p1_move[1] == p2_move[0] and p1_move[0] != p2_move[1]:
        return (1, sum)
    else:
    # elif p1_move[1] != p2_move[0] and p1_move[0] == p2_move[1]:
        return (2, sum)

    


def play_once():
    """
    Play the finger game once. Each player randomly chooses
    the number of fingers shown and guessed. Returns the winner
    and the amount won.

    :return: the winner (1, 2, or 0 if no winner), and the amount won
    """
    return get_outcome(get_move(),get_move())


def calc_winnings(player, winner, amount):
    """
    Calculate the winnings of player based on the game
    winner and the amount won.

    :param player: 1 or 2
    :param winner: 1,2, or 0 if no winner
    :param amount: amount won by winner, 0 if tie
    :return: player winnings - negative if player lost, 0 in case of a tie
    """
    # winner, amount = play_once()
    # print(result[0])

    if winner == 0:
        return 0

    if player == winner:
        return amount
    
    return -amount



def play_multiple(num_simulations):
    """
    Simulate playing the game num_simulations times. A list of
    player1's winnings for each game is returned. For example,
    if two games are played and player1 won 4 in the first game
    and lost 2 in the second game, [4, -2] is returned.

    :param num_simulations: number of simulations
    :return: a list containing the winnings of player1 in each game played
    """
    record = []
    for n in range(num_simulations):
        winner, winnings = play_once()
        # calc_winnings(2,1,rints)
        record.append(int(calc_winnings(1,winner,winnings)))

    return record
        


def simulate():
    """
    Simulate playing the game 10000 times.
    Also plot a histogram of the winnings, which can be done with
    two lines of code (see documentation of matplotlib.hist() and matplotlib.show()).
    """
    x = play_multiple(10000)
    num_bins = 300
    weights = np.ones_like(x) / len(x)
   
    n, bins, patches = plt.hist(x,bins = num_bins, weights = weights, align='left')

    plt.show()


if __name__ == '__main__':
    # simulate()
    # print(get_move())
    # print(get_outcome([2,2],[1,1]))
    # print(play_multiple(10))
    simulate()
    # print(calc_winnings(2,1,2))

