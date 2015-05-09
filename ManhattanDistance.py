# -*- coding: UTF-8 -*-
from Node import Node

class ManhattanDistance:
    """
    Implementation of Manhattan distance heuristic
    for 15-puzzle positions
    """

    def __init__(self):
        self._goal = Node([
            [ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15,  0]
        ], [], self)

    def compute(self, node):
        """
        Computes Manhattan distance of the given Node
        """
        score = 0
        for value in range(1, 16):
            iGoal, jGoal = self._goal.getCoordByValue(value)
            iActual, jActual = node.getCoordByValue(value)
            score += abs(iGoal - iActual) + abs(jGoal - jActual)
        return score