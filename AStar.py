# -*- coding: UTF-8 -*-
from NodeBuilder import NodeBuilder
from NodePool import NodePool
from Node import Node

class AStar:
    """
    Python implementation of A* algorithm
    """

    def __init__(self, heuristic):
        self._nodePool = NodePool()
        self._nodeBuilder = NodeBuilder()
        self._heuristic = heuristic

    def solve(self, position):
        """
        Solve the given starting position and
        return the list of moves.
        Return None if no solution has been found.
        """
        self._bootstrap(position)
        while not self._nodePool.isEmpty():
            # Pop best node from priority queue
            currentNode = self._nodePool.pop()
            if currentNode.getHScore() == 0:
                # Solution found!
                return currentNode.getMoves()
            # Compute child nodes and add them to the queue
            children = self._nodeBuilder.getChildNodes(currentNode)
            for child in children:
                self._nodePool.add(child)
        # No solution has been found
        return None

    def _bootstrap(self, position):
        """
        Create the initial Node from the given position.
        Add the initial node to the queue.
        """
        node = Node(position, [], self._heuristic)
        self._nodePool.add(node)