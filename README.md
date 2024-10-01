# hex_player_RL
Reinforcement Learning Agent to play a game of Hex board game with Alpha-Beta Pruning Search

### Introduction:
This project implements a text-based version of the **Hex** board game, where a human player competes against a computer-controlled agent. The computer agent uses the **Alpha-Beta pruning** algorithm and a basic evaluation function to select its next move. The game logic and board management are handled by the `HexBoard` class.

### How to Play:
1. The game is initiated with a board of size `n x n` (defined by the user).
2. The user is prompted to decide whether they want to play first or let the computer go first.
3. Players alternate making moves on the board:
   - The human player plays as **BLUE**.
   - The computer agent plays as **RED** using the Alpha-Beta pruning algorithm to choose its moves.
4. The game continues until either the human player or the computer wins by completing a connected path between their assigned sides on the Hex board.

### Files:
- **hex_skeleton.py**: Contains the `HexBoard` class, which handles the core mechanics of the Hex game, including move validation, board representation, and win condition checking.
- **main.py**: The main game logic, where the human player interacts with the game, and the computer agent makes decisions based on Alpha-Beta pruning.

### Key Functions:
- **getMoves(board)**: Returns all available moves on the current board.
- **makeMove(move, color, board)**: Places a piece of the given color on the board at the specified move location.
- **unmakeMove(move, board)**: Removes a piece from the specified move location, restoring the spot to empty.
- **alphabeta(eval_f, board, a, b, depth, is_max, color)**: Recursively searches for the best possible move using Alpha-Beta pruning, evaluating board states based on a dummy evaluation function.
- **nextMove(eval_f, board, d, c)**: Determines the computer's next best move using the Alpha-Beta pruning algorithm.
- **main(boardsize)**: The main function that initiates the game, allowing human and computer players to take turns.

### How to Run:
1. Run the `main.py` file to start the game.
2. Select whether you want to play first or allow the computer to go first.
3. Input your moves by entering the x and y coordinates of the hexagon where you want to place your piece.
4. The game will alternate between the human player and the computer until a winner is determined.

### Requirements:
- Python 3.x
- The `hex_skeleton.py` file containing the `HexBoard` class should be in the same directory as `main.py`.

### Future Improvements:
- Implement a more advanced evaluation function for better decision-making by the computer agent.
- Allow for adjustable difficulty by varying the depth of the Alpha-Beta search.
- Add a graphical interface to enhance the user experience.

### Acknowledgements:
This project is part of a study on board games and reinforcement learning algorithms. The basic evaluation function in this code is a placeholder for future more sophisticated algorithms.
