# -*- coding: UTF-8 -*-
class NodePool:
    """
    Contains list of Nodes used by A* algorithm.

    This is an enhanced implementation of a priority queue
    designed especially to solve 15-puzzle problems
    """

    def __init__(self):
        self._pool = []
        self._history = {}

    def add(self, node):
        """
        Add new Node to the pool
        Nodes previously added will not be added again
        """
        if str(node.getPosition()) in self._history:
            # duplicate entry
            return
        self._history[str(node.getPosition())] = True
        self._insort(node)

    def pop(self):
        """
        Pop the node with best score (first in the pool)
        """
        return self._pool.pop(0)

    def isEmpty(self):
        """
        Return true if the priority queue does not contain any node
        """
        return len(self._pool) == 0

    def _insort(self, node):
        """
        Insert the node in the pool while keeping the list ordered
        """
        lo = 0
        hi = len(self._pool)
        while lo < hi:
            mid = (lo+hi)//2
            if node.getFScore() < self._pool[mid].getFScore(): hi = mid
            else: lo = mid + 1
        self._pool.insert(lo, node)