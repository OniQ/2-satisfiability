class Vertex:
    def __init__(self, name):
        self.name = name    #vertex name refers an expression variable
        self.index = None   #index used by Tarjan's algorithm
        self.lowlink = None #lowlink used by Tarjan's algorithm
        self.value = None   #logical value of variable

class Graph:
    nodes = {}              #string variable marks it's vertex object
    neighbours = {}         #dictionary of vertices with set of directed vertices
                            #it can be used to construct graph
    is_satisfiable = None   #boolean satisfiability indicator
                            #it is None while it's value not known
    
    def __init__(self, expression):
        #transform expression string
        expression = expression.replace('(', ' ')
        expression = expression.replace(')', ' ')
        expression = expression.replace('+', ' ')
        expression = expression.split()
        #initialize nodes dictionary with unique nodes 
        for v in set(expression):
            self.nodes[v] = Vertex(v)
        #initialize 'vertices : set of neighbours' dictionary
        for n_key in self.nodes.keys():
            self.neighbours[self.nodes[n_key]] = set()