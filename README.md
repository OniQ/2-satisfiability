2-satisfiability
================
Description:
-------
       Solves the 2-satisfiability problem by creating graph based on expression 
    and dividing it into strong components using [Tarjan's algorithm](http://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm).
graph.py:
-------
       Graph and Vertex class implementation. Expression must be passed to 
    Graph's constructor for graph to be generated. 
    
    Methods:
       *tarjan():
          divides graph into strong components and decides 
       if it's satisfiable or not by setting is_satisfiable variable
       which is None by default.
       
       *evaluate():
          sets variables(graph's vertices) to one of possible values for expression to be satisfiable.
test.py:
-------
    Provides example of Graph class usage and prints the result.
    