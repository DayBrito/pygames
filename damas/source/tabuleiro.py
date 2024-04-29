import pygame
from .constantes import BLACK, ROWS, GREEN, L_GREEN, SQUARE_SIZE, COLS, WHITE, RED
from .peca import Piece
from source import peca
class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares (self, win):
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, L_GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def move(self, peca, row, col):
        self.board[peca.row][peca.col], self.board[row][col] = self.board[row][col], self.board[peca.row][peca.col]
        peca.move(row, col)

        if row == ROWS or row == 0:
            peca.make_king()
            if peca.color == WHITE:
                self.white_kings +=1
            else:
                self.red_kings +=1
    
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece !=0:
                    piece.draw(win)

    def get_valid_moves(self,peca):
        moves = {}
        left = peca.col -1
        rigth = peca.col +1
        row = peca.row
        
        if peca.color == RED or peca.king:
            pass
        
        if peca.color == WHITE or peca.king:
            pass

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        pass

    def _traverse_right(self, start, stop, step, color, left, skipped=[]):
        pass
