class Vertex:
    def __init__(self, name):
        self.name = name     # vertex name refers an expression variable
        self.index = None    # index used by Tarjan's algorithm
        self.lowlink = None  # lowlink used by Tarjan's algorithm
        self.value = None    # logical value of variable


class Graph:
    nodes = {}               # string variable marks it's vertex object
    neighbours = {}          # dict of vertices with set of directed vertices
                             # it can be used to construct graph
    is_satisfiable = None    # boolean satisfiability indicator
                             # it is None while it's value not known
    stack = []               # stack used by tarjan algorithm
    index = 0                # used by tarjan algorithm
    scc_list = []            # strong connected components list

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
            self.neighbours[_v1].add(v2)  # edge (~x -> y) from (x + y)
            if _v2 not in self.neighbours:
                self.neighbours[_v2] = set()
            self.neighbours[_v2].add(v1)  # edge (~y -> x) from (x + y)
            i += 2                        # move to next clause

    def strong_connect(self, v):
        v.index = self.index
        v.lowlink = self.index
        self.index += 1
        self.stack.append(v)
        for w in self.neighbours[v]:
            if w.index is None:
                self.strong_connect(w)
                v.lowlink = min(v.lowlink, w.lowlink)
            elif w in self.stack:
                v.lowlink = min(v.lowlink, w.lowlink)
        if (v.lowlink == v.index):
            scc = []
            while True:
                w = self.stack.pop()
                if self.negateVertex(w) in scc:
                    is_satisfiable = False
                scc.append(w)
                if w == v:
                    break
            self.scc_list.append(scc)

    def tarjan(self):
        self.is_satisfiable = True
        for v in self.neighbours.keys():
            if v.index is None:
                self.strong_connect(v)

    def evaluate(self):
        for scc in self.scc_list:
            for v in scc:
                if v.value is None:
                    v.value = True
                    opposite = self.negateVertex(v)
                    opposite.value = False

    def get_graph_string(self):
        graph_str = "node : directions\n"
        for k in self.neighbours.keys():
            graph_str += k.name + " : "
            for n in self.neighbours[k]:
                graph_str += n.name + ", "
            graph_str = graph_str.rstrip(', ')
            graph_str += '\n'
        return graph_str

    def get_scc_list_string(self):
        list_str = ""
        for scc in self.scc_list:
            list_str += 'Strong connected component %d:\n'\
                        % (self.scc_list.index(scc) + 1)
            for c in scc:
                list_str += "%s(%s) " % (c.name, c.value)
            list_str += '\n'*2
        return list_str

    def __str__(self):
        display_str = "%s\n%sSatisfiable: %s\n" % (self.get_graph_string(),
                                                   self.get_scc_list_string(),
                                                   self.is_satisfiable
                                                   )
        return display_str
