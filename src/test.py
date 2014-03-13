from graph import Graph

expression = "(u1 + u2)(u1 + ~u2)(u2 + u3)(~u1 + ~u3)"
#expression = "(u1 + u2)(~u1 + u3)(~u3 + ~u4)(u1 + u4)"
#"(~u2 + ~u5)(u5 + ~u6)(u2 + u6)(~u3 + u4)"
graph = Graph(expression)
print graph
