#!/usr/bin/env python

# Travelling knight
#
# A knight on a N*N chess board must visit all squares once
# using only valid moves
#
# This version uses the heuristic when chosing the next move
# Whichever square has the least possible moves is chosen.
# If no free squares are available the knight is taken back one
# move and another path is taken.

import random
import tree
import sys
import os

class Square:
    def __init__(self):
        self.visited = False;

class Chessboard:
    def __init__(self, size=8, knight_start=None):
        self.size = size

        self.knight_start = knight_start
        if self.knight_start is None:
            self.knight_start = (random.randint(0, size-1), 
                                 random.randint(0, size-1))
        
        self.move_history = tree.Tree()
        self. history_pos = -1
        self.initBoard()
        self.current_move = None
        self.moveKnight(self.knight_start)
        self.visited_squares = 0
        self.target = size * size

    def initBoard(self):
        self.board = []
        for width in range(0, self.size):
            self.board.append([]);
            for height in range(0, self.size):
                self.board[width].append(Square())
    
    def moveKnight(self, dest, add_node = True):
        self.knight = dest
        if add_node is True:
            new_node = tree.Node(dest)
            self.move_history.addChild(new_node, self.current_move)
            self.current_move = new_node
        self.board[dest[0]][dest[1]].visited = True;

    def numVisited(self):
        # There's probably a better way to do this
        count = 0
        for width in range(0, self.size):
            for height in range(0, self.size):
                if self.board[width][height].visited:
                    count = count + 1
        return count

    def getValidMovesFromSquare(self, square):
        next_squares = []

        move_long = 2
        move_short = 1

        # move_long right, move_short up
        if (square[0] + move_long < self.size and 
                square[1] + move_short < self.size):
            next_squares.append(
                    (square[0] + move_long, 
                        square[1] + move_short))

        # move_long right, move_short down
        if (square[0] + move_long < self.size and 
                square[move_short] - move_short >= 0):
            next_squares.append(
                    (square[0] + move_long, 
                        square[move_short] - move_short))
        
        # move_long left, move_short up
        if (square[0] - move_long >= 0 and 
                square[move_short] + move_short < self.size):
            next_squares.append((square[0] - move_long, 
                square[move_short] + move_short))

        # move_long left, move_short down
        if (square[0] - move_long >= 0 and 
                square[move_short] - move_short >= 0):
            next_squares.append(
                    (square[0] - move_long, 
                        square[move_short] - move_short))

        # move_short left, move_long up
        if (square[0] - move_short >= 0 and 
                square[move_short] + move_long < self.size):
            next_squares.append(
                    (square[0] - move_short, 
                        square[move_short] + move_long))

        # move_short right, move_long up
        if (square[0] + move_short < self.size and 
                square[move_short] + move_long < self.size):
            next_squares.append(
                    (square[0] + move_short, 
                        square[move_short] + move_long))

        # move_short left, move_long down
        if (square[0] - move_short >= 0 and 
                square[move_short] - move_long >= 0):
            next_squares.append(
                    (square[0] - move_short, 
                        square[move_short] - move_long))

        # move_short right, move_long down
        if (square[0] + move_short < self.size and 
                square[move_short] - move_long >= 0):
            next_squares.append(
                    (square[0] + move_short, 
                        square[move_short] - move_long))
        
        return next_squares

    def nextMove(self):
        knight_next = self.getValidMovesFromSquare(self.knight)
        # now we have all possible valid moves
        # which one is the best?
        best_weight = 999999
        best_move = None
        for move in knight_next:
            if (self.board[move[0]][move[1]].visited is False 
                    and self.move_history.findImmediateChild(self.current_move, (move[0], move[1])) is None):
                weight = len(self.getValidMovesFromSquare(move))
                if weight < best_weight:
                    best_weight = weight
                    best_move = move

        if best_move is None:
            # Couldn't find a good move, are we done?
            if self.numVisited() == (self.size ** 2):
                print "done. Started at", self.knight_start
                return False
            
            # Nope, are we at the top of the tree?
            if self.current_move.parent is None:
                # Also no search space left. End
                self.printIt()
                print "the end"
                return False

            # Nope, go back one and try a different path
            self.board[self.current_move.data[0]][self.current_move.data[1]].visited = False
            self.current_move = self.current_move.parent
            # But don't add this to the tree again.
            self.moveKnight(self.current_move.data, False)
            return True
       
        self.moveKnight(best_move)
        self.printIt()
        return True

    def printIt(self):
        # Simple screen clear (nix only)
        # * is visited and 0 is not visited
        os.system('clear')
        height = 0
        for width in range(0, self.size):
            for height in range(0, self.size):
                if self.board[width][height].visited:
                    print '*',
                else:
                    print 'O',
            
            print ":",width
        for i in range(0, self.size):
            print i,

        print "+"

if __name__ == "__main__":
    size = 6
    if len(sys.argv) > 1:
        size = int(sys.argv[1])

    cb = Chessboard(size=size)
    print 
    while cb.nextMove():
        pass
    print
