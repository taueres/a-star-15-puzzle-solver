# -*- coding: UTF-8 -*-
from ManhattanDistance import ManhattanDistance
from AStar import AStar
from pprint import pprint

heuristic = ManhattanDistance()
astar = AStar(heuristic)
start = [
            [ 1,  6,  7,  5],
            [ 9,  3, 10,  2],
            [13,  8,  4, 12],
            [14, 11, 15,  0]
        ]

result = astar.solve(start)
pprint(result.getMoves())
