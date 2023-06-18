# Finger-Guessing-Game-Simulation
The project aims to simulate 10,000 games between two players, P1 and P2, following specific rules. The players simultaneously show and guess the number of fingers the other player will display. Based on their correct or incorrect guesses, winnings are calculated and plotted in a histogram to visualize the distribution of P1's winnings.

# Finger Game Simulation

This project simulates the Finger Game, where two players (P1 and P2) simultaneously show and guess the number of fingers the other player will display. The objective is to simulate 10,000 games and plot a histogram showcasing the distribution of Player 1's winnings.

## Getting Started

To run the simulation and generate the histogram, follow the instructions below.

### Prerequisites

- Python 3.x
- matplotlib library

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/finger-game.git
   ```
   
2. Change into the project directory:
   ```
   cd finger-game
   ```

3. Install the required dependencies:
   ```
   pip install matplotlib
   ```

### Usage

1. Open `hw5.py` and implement the required functions: `get_move()`, `get_outcome(p1_move, p2_move)`, `play_once()`, `calc_winnings(player, winner, fingers)`, `play_multiple(num_simulations)`, and `simulate()`. Refer to the function documentation for details on their parameters and return values.

2. Run the simulation:
   ```
   python hw5.py
   ```

3. The program will simulate 10,000 games and display the resulting histogram, showcasing the distribution of Player 1's winnings.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements

The starter code and tests for this project were provided as part of a previous homework assignment. Special thanks to the course instructor and teaching staff for providing the materials.
