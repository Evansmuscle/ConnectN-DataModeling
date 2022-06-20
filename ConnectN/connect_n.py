print("Welcome to Connect N! Please input to the console how my connects there should be to win the game!")
n = int(input())

print("Now please input the amount of players that will play the game!")
player_amount = int(input())

print("Good luck! Remember, every turn you play, you must input a column and a row respectively, seperated by a space")

class ConnectN:
    n
    player_amount
    row_width=7
    col_height=6
    board=""
    current_player = 1
    game_over = False

    def __init__(self, n=int, player_amount=int):
        self.n = n
        self.player_amount = player_amount
        self.row_width = 7
        self.col_height = 6
        self.board = self.generate_board(self.col_height, self.row_width)
        self.current_player = 1
        self.player_turn()

    def generate_board(self, col_height=int, row_width=int):
        return "0"*row_width*col_height
    
    def print_board(self):
        for idx, _ in enumerate(self.board[0:len(self.board)-1:7]):
            print(self.board[idx*7:(idx*7)+7])
    
    def add_connect(self, row, col):
        if self.board[((row-1) * self.row_width)+(col-1)] == "0":
            self.board = self.board[:((row-1) * self.row_width)+(col-1)] + str(self.current_player) + self.board[((row-1) * self.row_width)+(col-1)+1:]
            self.print_board()
        else:
            print("Invalid Move!")
    
    def calc_horizontal(self, current_row=int, current_col=int):
        connect_amount = 1
        for idx, x in enumerate(self.board[self.row_width*current_row-self.row_width:self.row_width*current_row]):
            if idx == (current_col-1):
                continue
            
            if not abs((current_col-1) - idx) < self.n:
                continue
            
            if x == str(self.current_player):
                connect_amount += 1
                if connect_amount == self.n:
                    return True
                continue
            
            connect_amount = 1
        
        return False

    def calc_vertical(self, current_row=int, current_col=int):
        connect_amount = 1
        for idx, x in enumerate(self.board[current_col-1:(self.row_width*(self.col_height - 1))*current_col:self.row_width]):
            if idx == (current_row-1):
                continue
            
            if not abs((current_row-1) - idx) < self.n:
                continue
            
            if x == str(self.current_player):
                connect_amount += 1
                if connect_amount == self.n:
                    return True
                continue
            
            connect_amount = 1
        
        return False
    
    # Unfortunately i could not finish the diagonal calculation.
    def calc_diagonal(self, current_row=int, current_col=int):
        connect_amount = 1

    def calculate_connect(self, current_row=int, current_col=int):
        score_horizontal = self.calc_horizontal(current_row, current_col)
        score_vertical = self.calc_vertical(current_row, current_col)
        score_diagonal = self.calc_diagonal(current_row, current_col)
        
        if score_horizontal or score_vertical or score_diagonal:
            self.game_over = True
        else:
            if self.current_player == self.player_amount:
                self.current_player = 1
            else:
                self.current_player += 1

        
    def player_turn(self):
        if self.game_over:
            print("Player " + str(self.current_player) + " won!")
            return

        print("Player " + str(self.current_player) + "'s turn:")
        print("Please input the row you want to play in")
        row = int(input())
        print("Please input the column you want to play in")
        column = int(input())
        self.add_connect(row, column)
        self.calculate_connect(row, column)
        self.player_turn()
        

connect_n = ConnectN(n, player_amount)
