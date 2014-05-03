class DFS(object):

    def __init__(self, adj, order):
       self.parents = {}
       self.f = []
       self.i = 0
       if type(order) is dict:
           self.order = list(order.values())
           self.scc = None
       else:
           self.order = order[::-1]
           self.scc = []

       for u in self.order:
           u.color = "balta"
           self.parents[u] = None
       self.time = 0
       self.adj = adj
       
       for u in self.order:
           if u.color == "balta":
              if (self.scc != None):
                 self.scc.append([])
              self.DFS_visit(u)
              self.i += 1

    def DFS_visit(self, u):
        #print("d[" + u.name + "]")
        u.color = "pilka"
        self.time += 1
        for v in self.adj[u]:
            if v.color == "balta":
                self.parents[v] = u
                self.DFS_visit(v)
        u.color = "juoda"
        self.time += 1
        self.f.append(u)
        if (self.scc != None):
            self.scc[self.i].append(u)
        #print("f[" + u.name + "]")
		