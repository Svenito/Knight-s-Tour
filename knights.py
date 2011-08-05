#!/usr/bin/env python


class Square:
    def __init__(self):
        self.visited = False;

class Chessboard:
    def __init__(self, size=8, knight_start=(0,0)):
        self.size = size
        self.initBoard()
        self.knight = knight_start

    def initBoard(self):
        self.board = []
        for width in range(0, self.size):
            self.board.append([]);
            for height in range(0, self.size):
                self.board[width].append(Square())
    
    def getValidMovesFromSquare(self, square):
        next_squares = [] 
        # 3 right, 1 up
        if (square[0] + 3 < self.size and square[1] + 1 < self.size):
            next_squares.append((square[0] + 3, square[1] + 1))

        # 3 right, 1 down
        if (square[0] + 3 < self.size and square[1] - 1 > 0):
            next_squares.append((square[0] + 3, square[1] - 1))
        
        # 3 left, 1 up
        if (square[0] - 3 > 0 and square[1] + 1 < self.size):
            next_squares.append((square[0] - 3, square[1] + 1))

        # 3 left, 1 down
        if (square[0] - 3 > 0 and square[1] - 1 > 0):
            next_squares.append((square[0] - 3, square[1] - 1))

        # 1 left, 3 up
        if (square[0] - 1 > 0 and square[1] + 3 < self.size):
            next_squares.append((square[0] - 1, square[1] + 3))

        # 1 right, 3 up
        if (square[0] + 1 < self.size and square[1] + 3 < self.size):
            next_squares.append((square[0] + 1, square[1] + 3))

        # 1 left, 3 down
        if (square[0] - 1 > 0 and square[1] - 3 > 0):
            next_squares.append((square[0] - 1, square[1] - 3))

        # 1 right, 3 down
        if (square[0] + 1 < self.size and square[1] - 3 > 0):
            next_squares.append((square[0] + 1, square[1] - 3))
        
        return next_squares

    def nextMove(self):
        knight_next = self.getValidMovesFromSquare(self.knight)
        # now we have all possibly valid moves
        # which one is the best?
        best_weight = -1
        best_move = None
        for move in knight_next:
            if self.board[move[0]][move[1]].visited is False:
                weight = len(self.getValidMovesFromSquare(move))
                if weight > best_weight:
                    best_weight = weight
                    best_move = move
        if move is None:
            return False

        self.knight = move
        print self.knight
        return True

if __name__ == "__main__":
    cb = Chessboard()
    
    while cb.nextMove():
        print "working"
