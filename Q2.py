file1 = open('graph.txt', 'r')

Lines = file1.readlines() 
Lines2 = []
for line in Lines:
    line = line.strip()
    Lines2.append(line)
Lines2

class Graph:
    def __init__(self,V):
        self.vertices = V
        self.graph = dict(zip(V,([] for _ in V)))
        
    def addedge(self, u, v):
        self.graph[u].append(v)
    #pop for key, remove for value in list
    def removeedge(self, u, v):
        self.graph[u].remove(v)
    #pop for key, remove for value in list
    def removenode(self, u):
        self.graph.pop(u)
        
s = []
for line in Lines2:
    s.append(line.split(',')[0])
    s.append(line.split(',')[1])
v = set(s)
g = Graph(v)
g_inv = Graph(v)

for line in Lines2:
    g.addedge(line.split(',')[1],line.split(',')[0])
    

def gettoposort(g):
    L = []
    S = []
    for n_vert in g.vertices:
        if g.graph[n_vert] == []:
            S.append(n_vert)
    while S:
        n_vert = S[0]
        S.remove(n_vert)
        L.append(n_vert)
        for m_vert in g.vertices:
            if n_vert in g.graph[m_vert]:
                g.removeedge(m_vert, n_vert)
                if g.graph[m_vert] == []:
                    S.append(m_vert)
    for vert in g.vertices:
        if g.graph[vert] != []:
            return "graph has at least one cycle"
    return L

result = gettoposort(g)

with open('topological_sort.txt','w') as f:
    f.write(str(result))