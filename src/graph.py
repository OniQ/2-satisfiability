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
    
    def negateVertex(self, vertex):
        """Negates vertex
        Returns vertex
        with same name from nodes
        Or creates new node if not found
        """
        var = vertex.name
        if var.find('~') != -1:
            var = var.lstrip('~')
        else:
            var = '~' + var
        if var not in self.nodes:
            self.nodes[var] = Vertex(var)
        return self.nodes[var]
    
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
        #same expression but with Vertex instead of strings    
        v_expression = []
        for v in expression:
            v_expression.append(self.nodes[v])
        #create graph edges based on expression clauses
        i = 0
        while i < len(v_expression):
            v1 = v_expression[i]
            v2 = v_expression[i + 1]
            _v1 = self.negateVertex(v1)
            _v2 = self.negateVertex(v2)
            if _v1 not in self.neighbours:
                self.neighbours[_v1] = set()
            self.neighbours[_v1].add(v2)#edge (~x -> y) from (x + y)
            if _v2 not in self.neighbours:
                self.neighbours[_v2] = set()
            self.neighbours[_v2].add(v1)#edge (~y -> x) from (x + y)
            i += 2#move to next clause
