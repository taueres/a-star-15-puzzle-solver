# -*- coding: UTF-8 -*-
from Node import Node

class NodeBuilder:
    """
    Build child nodes for 15-puzzle
    """

    def getChildNodes(self, node):
        """
        Return list of valid child nodes
        """
        children = []
        iSpace, jSpace = node.getCoordByValue(0)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i * j != 0 or i == j:
                    continue
                iSwap, jSwap = iSpace + i, jSpace + j
                if not (0 <= iSwap <= 3) or not (0 <= jSwap <= 3):
                    continue
                position = node.getPosition()
                position[iSpace][jSpace] = position[iSwap][jSwap]
                position[iSwap][jSwap] = 0
                moves = node.getMoves()
                moves.append(self._getMoveNameFromDelta(i, j))
                child = Node(
                    position,
                    moves,
                    node.getHeuristic()
                )
                children.append(child)
        return children

    def _getMoveNameFromDelta(self, iDelta, jDelta):
        if iDelta == -1:
            return 'up'
        if iDelta == 1:
            return 'down'
        if jDelta == -1:
            return 'left'
        if jDelta == 1:
            return 'right'
