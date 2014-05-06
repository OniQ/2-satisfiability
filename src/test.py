import sys

from graph import Graph

#expression = "(u1 + u2)(u1 + ~u2)(u2 + u3)(~u1 + ~u3)"
expression = "(u1 + u2)(~u1 + u3)(~u3 + ~u4)(u1 + u4)(~u2 + ~u5)(u5 + ~u6)(u2 + u6)(~u3 + ~u4)"
graph1 = Graph()
#graph1.construct('graph.txt')
graph1.create(expression)
graph1.sat2()
print graph1
