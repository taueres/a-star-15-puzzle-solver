# -*- coding: UTF-8 -*-
from NodeBuilder import NodeBuilder
from NodePool import NodePool
from Node import Node

class AStar:
    def __init__(self, heuristic):
        self._nodePool = NodePool()
        self._nodeBuilder = NodeBuilder()
        self._minScore = 100
        self._heuristic = heuristic

    def solve(self, position):
        self._bootstrap(position)
        while True:
            currentNode = self._nodePool.pop()
            if currentNode.getFScore() < self._minScore:
                self._minScore = currentNode.getFScore()
                print(self._minScore)
            if currentNode.getFScore() == 0:
                # Solution found!
                return currentNode
            children = self._nodeBuilder.getChildNodes(currentNode)
            for child in children:
                self._nodePool.add(child)

    def _bootstrap(self, position):
        node = Node(position, [], self._heuristic)
        self._nodePool.add(node)