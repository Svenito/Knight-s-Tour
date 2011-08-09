#!/usr/bin/env python
import tree

class Square:
    def __init__(self):
        self.visited = False;

class Chessboard:
    def __init__(self, size=8, knight_start=(0,0)):
        self.size = size
        self.move_history = tree.Tree()
        self. history_pos = -1
        self.initBoard()
        self.current_move = None
        self.moveKnight(knight_start)
        self.visited_squares = 0
        self.target = size * size

    def initBoard(self):
        self.board = []
        for width in range(0, self.size):
            self.board.append([]);
            for height in range(0, self.size):
                self.board[width].append(Square())
    
    def moveKnight(self, dest):
        self.knight = dest
        new_node = tree.Node(dest)
        self.move_history.addChild(new_node, self.current_move)
        self.current_move = new_node
        self.board[dest[0]][dest[1]].visited = True;

    def getValidMovesFromSquare(self, square):
        next_squares = [] 
        # 3 right, 1 up
        if (square[0] + 3 < self.size and square[1] + 1 < self.size):
            next_squares.append((square[0] + 3, square[1] + 1))

        # 3 right, 1 down
        if (square[0] + 3 < self.size and square[1] - 1 >= 0):
            next_squares.append((square[0] + 3, square[1] - 1))
        
        # 3 left, 1 up
        if (square[0] - 3 >= 0 and square[1] + 1 < self.size):
            next_squares.append((square[0] - 3, square[1] + 1))

        # 3 left, 1 down
        if (square[0] - 3 >= 0 and square[1] - 1 >= 0):
            next_squares.append((square[0] - 3, square[1] - 1))

        # 1 left, 3 up
        if (square[0] - 1 >= 0 and square[1] + 3 < self.size):
            next_squares.append((square[0] - 1, square[1] + 3))

        # 1 right, 3 up
        if (square[0] + 1 < self.size and square[1] + 3 < self.size):
            next_squares.append((square[0] + 1, square[1] + 3))

        # 1 left, 3 down
        if (square[0] - 1 >= 0 and square[1] - 3 >= 0):
            next_squares.append((square[0] - 1, square[1] - 3))

        # 1 right, 3 down
        if (square[0] + 1 < self.size and square[1] - 3 >= 0):
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

        '''if best_move is None:
            if self.visited_squares < self.target:
                #go back one.
                if not self.move_history.isEmpty():
                    self.moveKnight(self.move_history[-1])
                    self.move_history.pop()
                    self.nextMove()
                    return True 
            return False'''
        if best_move is None:
             
            print "the end"
            #self.move_history.printIt(self.move_history.root)
            self.printIt()
            return False

        self.moveKnight(best_move)
        print self.knight
        
        return True

    def printIt(self):
        height = 0
        for width in range(0, self.size):
            
            for height in range(0, self.size):
                if self.board[width][height].visited:
                    print '*',
                else:
                    print 'O',

            print ":",width

if __name__ == "__main__":
    cb = Chessboard()
    
    while cb.nextMove():
        print "working"
