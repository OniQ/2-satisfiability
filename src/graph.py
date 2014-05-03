from dfs import DFS

class Vertex:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.color = None
    def __str__(self):
        return self.name

class Graph:

    def negateVertex(self, vertex):
        """
		Negates vertex
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

    def __init__(self):
        self.nodes = {}
        self.adj = {}
        self.is_satisfiable = True

    def construct(self, fileName):
        f = open(fileName, 'r');

        for line in f:
            n = line.split()
            self.nodes[n[0]] = Vertex(n[0])

        f.seek(0)

        for line in f:
            line = line.replace(':', ' ')
            vertex = line.split()
            n = self.nodes[vertex[0]]
            del vertex[0]
            self.adj[n] = set()
            for v in vertex:
                self.adj[n].add(self.nodes[v])

        f.close()

    def create(self, expression):
        expression = expression.replace('(', ' ')
        expression = expression.replace(')', ' ')
        expression = expression.replace('+', ' ')
        expression = expression.split()
        for v in set(expression):
            self.nodes[v] = Vertex(v)

        for n_key in self.nodes.keys():
            self.adj[self.nodes[n_key]] = set()

        v_expression = []
        for v in expression:
            v_expression.append(self.nodes[v])
        #create graph edges based on clauses
        i = 0
        while i < len(v_expression):
            v1 = v_expression[i]
            v2 = v_expression[i + 1]
            _v1 = self.negateVertex(v1)
            _v2 = self.negateVertex(v2)
            if _v1 not in self.adj:
                self.adj[_v1] = set()
            self.adj[_v1].add(v2)  #edge (~x -> y) from (x + y)
            if _v2 not in self.adj:
                self.adj[_v2] = set()
            self.adj[_v2].add(v1) #edge (~y -> x) from (x + y)
            i += 2

    def transpose(self):
        self.adj_t = {}
        for v in self.nodes.itervalues():
            self.adj_t[v] = set()
        for n in self.adj.keys():
            for v in self.adj[n]:
                self.adj_t[v].add(n)

    def strongly_connected_components(self):
        self.DFS = DFS(self.adj, self.nodes)
        self.transpose()
        self.DFS_T = DFS(self.adj_t, self.DFS.f)
        self.scc = self.DFS_T.scc
        return self.scc

    def evaluate(self):
        for c in reversed(self.scc):
            for v in c:
                if v.value is None:
                    v.value = True
                    opposite = self.negateVertex(v)
                    opposite.value = False

    def sat2(self):
        scc = self.strongly_connected_components()
        for c in scc:
            for u in c:
                if c.count(self.negateVertex(u)) > 0:
                    self.is_satisfiable = False;
        self.evaluate()

    def get_graph_string(self, adj):
        graph_str = ""
        for k in adj.keys():
            graph_str += k.name + " : "
            for n in adj[k]:
                graph_str += n.name + ", "
            graph_str = graph_str.rstrip(', ')
            graph_str += '\n'
        return graph_str

    def __str__(self):
        display_str = ""
        display_str += self.get_graph_string(self.adj) + '\n'
        display_str += '\n'
        display_str += self.get_scc_list_string() + '\n'
        if self.is_satisfiable:
            display_str += "Satisfiable"
        else:
            display_str += "Not Satisfiable"
        return display_str

    def get_transpose_string(self):
        display_str = ""
        display_str += self.get_graph_string(self.adj_t) + '\n'
        return display_str

    def get_scc_list_string(self):
        i = 0
        display_str = ""
        for c in self.scc:
            i += 1
            component = ""
            for v in c:
                component += v.name + "{" + str(v.value) + "} "
            display_str += 'C' + str(i) + ': ' + component + '\n'
        return display_str
		