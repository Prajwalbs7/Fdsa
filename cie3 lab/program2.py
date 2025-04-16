class edge
def __init__(self);
    self.adj_list = {}

    def add_edge(self,v,w):
        if v not in self.adjancency.list
            self.adjacency_list[v] = []
    self.adjacecny_list[v].append(w)

    if w not in self.adjacency_list:
        self.adjacency_list[w] = []
     self.adjacency_list[w].append(v) 

    def display(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}:{self.adjacency_list[vertex]}")

        
   # Example usage
   e = edge()
e.add_edge('A','B')
e.add_edge('A','C')
e.add_edge('B','D')
e.display()
