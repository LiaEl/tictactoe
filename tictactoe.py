#!/usr/bin/env python3

def check_row(board, smb, row_num):
    for i in board[row_num]:
        if i != smb:
            return False
    else:
        return True

def check_column(board, smb, clmn_num):
    for i in range(len(board)):
        if board[i][clmn_num] != smb:
            return False
    else:
        return True

def check_diag_1(board, smb):
    if board[0][0] == smb and board[1][1] == smb and board[2][2] == smb:
        return True
    else:
        return False

def check_diag_2(board, smb):
    if board[2][0] == smb and board[1][1] == smb and board[0][2] == smb:
        return True
    else:
        return False


class Game():
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.checklist = [
            check_diag_1,
            check_diag_2,
            lambda board, smb: check_row(board, smb, 0),
            lambda board, smb: check_row(board, smb, 1),
            lambda board, smb: check_row(board, smb, 2),
            lambda board, smb: check_column(board, smb, 0),
            lambda board, smb: check_column(board, smb, 1),
            lambda board, smb: check_column(board, smb, 2)
        ]

    def is_winner(self, smb):
        for func in self.checklist:
            if func(self.board, smb):
                print("YOU WON")
                return True
        else:
            print("Next player, please")
            return False


    def make_step(self, smb, x, y):
        self.board[x][y] = smb

    def print_game(self):
        print("-------------")
        for i in self.board[0]:
            print('|', i, end=' ')
        print('|')
        print("-------------")
        for j in self.board[1]:
            print('|', j, end=' ')
        print('|')
        print("-------------")
        for k in self.board[2]:
            print('|', k, end=' ')
        print('|')
        print("-------------")

class Player():
    def __init__(self, smb):
        self.smb = smb

    def get_smb(self):
        return self.smb

if __name__ == '__main__':
    the_game = Game()
    end_game = False

    player1 = Player('X')
    the_game.print_game()

    while end_game != True:
        while True:
            try:
                print("Enter the next step coordinates (x, y): ", end="")
                x, y = [int(i) for i in input().split()]

                if x < 0 or x > 2 or y < 0 or y > 2:
                    raise ValueError(
                        "Please, enter the two numbers in range 0 - 2."
                    )

                if the_game.board[x][y] != ' ':
                    raise ValueError("Field is not empty.")

            except ValueError as e:
                print(e)
            else:
                break

        the_game.make_step(player1.get_smb(), x, y)
        the_game.print_game()

        end_game = the_game.is_winner(player1.get_smb())