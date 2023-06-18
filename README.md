# Finger-Guessing-Game-Simulation
The project aims to simulate 10,000 games between two players, P1 and P2, following specific rules. The players simultaneously show and guess the number of fingers the other player will display. Based on their correct or incorrect guesses, winnings are calculated and plotted in a histogram to visualize the distribution of P1's winnings.



## Getting Started

To run the simulation and generate the histogram, follow the instructions below.

### Prerequisites

- Python 3.x
- matplotlib library
- numpy library

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Alicechui/Finger-Guessing-Game-Simulation

   ```
   
2. Change into the project directory:
   ```
   cd Finger-Guessing-Game-Simulation
   ```

3. Install the required dependencies:
   ```
   pip install matplotlib
   ```
   ```
   pip install numpy
   ```
### Usage

1. Open `game.py` and implement the required functions: `get_move()`, `get_outcome(p1_move, p2_move)`, `play_once()`, `calc_winnings(player, winner, fingers)`, `play_multiple(num_simulations)`, and `simulate()`. Refer to the function documentation for details on their parameters and return values.

2. Run the simulation:
   ```
   python game.py
   ```

3. The program will simulate 10,000 games and display the resulting histogram, showcasing the distribution of Player 1's winnings.


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

