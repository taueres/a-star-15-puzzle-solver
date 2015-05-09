# -*- coding: UTF-8 -*-
import time
from ManhattanDistance import ManhattanDistance
from AStar import AStar
from Node import Node
from pprint import pprint

heuristic = ManhattanDistance()
astar = AStar(heuristic)
start = [
            [ 1,  6,  7,  5],
            [ 9,  3, 10,  2],
            [13,  8,  4, 12],
            [14, 11, 15,  0]
        ]

startTime = time.time()
startComplexity = heuristic.compute(
    Node(start, [], None)
)

result = astar.solve(start)

if result is None:
    print('No solution found')
else:
    pprint(result)
    print('Heuristic said at least %d moves were needed.' % startComplexity)
    print('Actually solution is %d moves away. Best solution found guaranteed!' % len(result))
    print('Solved in %d seconds.' % (time.time() - startTime))
