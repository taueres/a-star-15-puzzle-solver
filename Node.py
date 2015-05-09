# -*- coding: UTF-8 -*-
import copy

class Node:
    """
    A node is a position (immutable) in the puzzle
    It also contains the gScore, hScore, fScore and
    the list of moves which bring us to this position
    """

    def __init__(self, position, moves, heuristic):
        """
        Builds a new node
        """
        self._position = position
        self._moves = moves
        self._heuristic = heuristic
        self._hScore = None

    def getPosition(self):
        """
        Get position of the Node (nested list of integers)
        """
        return copy.deepcopy(self._position)

    def getGScore(self):
        """
        Get gScore of the Node
        """
        return len(self._moves)

    def getHScore(self):
        """
        Get hScore of this Node. Heuristic passed in
        the constructor will be used for computation
        """
        if self._hScore is None:
            self._hScore = self._heuristic.compute(self)
        return self._hScore

    def getFScore(self):
        """
        Get fScore of the Node
        fScore = gScore + hScore
        """
        return self.getGScore() + self.getHScore()

    def getMoves(self):
        """
        Return list of moves which bring us to
        this position
        """
        return copy.copy(self._moves)

    def getHeuristic(self):
        """
        Return heuristic used to compute hScore for this node
        """
        return self._heuristic

    def getCoordByValue(self, value):
        """
        Get i and j coord of the given value
        """
        i = 0
        for row in self._position:
            j = 0
            for cell in row:
                if cell == value:
                    return [i, j]
                j += 1
            i += 1