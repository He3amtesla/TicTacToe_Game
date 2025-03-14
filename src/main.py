import random

class TicTacToe():
    def __init__(self):
        """
        Initialize the TicTacToe game with an empty board and random first player.
        
        The board is represented as a list of 10 elements, with index 0 being ignored
        for easier mapping of positions 1-9 to the board.
        """
        self.board = [' '] * 10 #index 0th is ignore
        self.user_turn = self.get_random_first_player()
        
    def get_random_first_player(self) -> chr:
        """
        Randomly select which player goes first.
        """
        return random.choice(['O', 'X'])
        
    def show_board(self):
        print("\n")
        print((self.board[1] if self.board[1] != ' ' else '1') +'  |  '+ (self.board[2] if self.board[2] != ' ' else '2') +'  |  '+ (self.board[3] if self.board[3] != ' ' else '3'))
        print("-- -- -- -- -")
        print((self.board[4] if self.board[4] != ' ' else '4') +'  |  '+ (self.board[5] if self.board[5] != ' ' else '5') +'  |  '+ (self.board[6] if self.board[6] != ' ' else '6'))
        print("-- -- -- -- -")
        print((self.board[7] if self.board[7] != ' ' else '7') +'  |  '+ (self.board[8] if self.board[8] != ' ' else '8') +'  |  '+ (self.board[9] if self.board[9] != ' ' else '9'))
        print("\n")
        
    def swap_player_turn(self) -> chr:
        self.user_turn = 'O' if self.user_turn == 'X' else 'X'
        return self.user_turn
    
    def is_board_filled(self) -> bool:
        return ' ' not in self.board[1: ]
    
    def fix_spot(self, cell: int, player: chr) -> None:
        self.board[cell] = player
        
    def has_player_won (self, player: chr) -> bool:

        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], #rows or the same Record
            [1, 4, 7], [2, 5, 8], [3, 6, 9], #colums or the same Fields
            [1, 5, 9], [3, 5, 7] #Diagonals
        ]
        
        for combination in win_combinations:
            if all([self.board[cceell] == player for cceell in combination]):
                return True
            
        return False
    
    def start(self):
        """
        Start and run the Tic-Tac-Toe game.
        
        This method manages the game loop, handling player input, updating the game state,
        checking for win/draw conditions, and switching player turns.
        """
        while True:
            self.show_board()
            print(f"player {self.user_turn} turn")
            cell = int(input("Enter cell number from 1 to 9: "))
            
            if self.board[cell] == " " and cell in range(1,10):
                self.fix_spot(cell, self.user_turn)
                
                if self.has_player_won(self.user_turn):
                    self.show_board()
                    print(f"player {self.user_turn} is won!")
                    break
                
                if self.is_board_filled():
                    print("Draw\n")
                    break
                
                self.swap_player_turn()

            else:
                print("invalid cell number؛ try again")
                    
     
                
if __name__ == "__main__":
    obj = TicTacToe()
    obj.start()