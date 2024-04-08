import random

class Ludo:
    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.players = ['Red', 'Green', 'Yellow', 'Blue']
        self.positions = {'Red': [(-1, -1), (-1, -1), (-1, -1), (-1, -1)],
                          'Green': [(-1, -1), (-1, -1), (-1, -1), (-1, -1)],
                          'Yellow': [(-1, -1), (-1, -1), (-1, -1), (-1, -1)],
                          'Blue': [(-1, -1), (-1, -1), (-1, -1), (-1, -1)]}

    def print_board(self):
        print("\nLudo Board:")
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

    def roll_dice(self):
        return random.randint(1, 6)

    def move_piece(self, player, piece_index, steps):
        current_row, current_col = self.positions[player][piece_index]
        if current_row == -1 and current_col == -1:
            return False  # Piece not on the board yet
        new_row, new_col = self.get_new_position(current_row, current_col, steps)
        if not self.is_valid_move(new_row, new_col, player):
            return False
        self.board[current_row][current_col] = 0
        self.board[new_row][new_col] = player[0]
        self.positions[player][piece_index] = (new_row, new_col)
        return True

    def get_new_position(self, row, col, steps):
        if row == 0 and 0 <= col + steps < 6:
            return row, col + steps
        elif row == 0 and col + steps >= 6:
            return row + 1, 11 - (col + steps)
        elif 0 <= row + steps < 6 and col == 6:
            return row + steps, col
        elif row + steps >= 6 and col == 6:
            return 11 - (row + steps), col - 1

    def is_valid_move(self, row, col, player):
        if 0 <= row < 7 and 0 <= col < 7:
            if self.board[row][col] == 0 or self.board[row][col] == player[0]:
                return True
        return False

    def play(self):
        print("Welcome to Ludo!")
        while True:
            for player in self.players:
                print(f"\n{player}'s turn:")
                input("Press Enter to roll the dice...")
                dice_roll = self.roll_dice()
                print(f"You rolled a {dice_roll}")
                piece_index = int(input("Enter piece index to move (0-3): "))
                moved = self.move_piece(player, piece_index, dice_roll)
                if not moved:
                    print("Invalid move! Try again.")
                else:
                    self.print_board()
                if all(self.board[row][col] == player[0] for row, col in self.positions[player]):
                    print(f"{player} wins!")
                    return

if __name__ == "__main__":
    game = Ludo()
    game.play()
