from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c

graph = csr_matrix(graph)

x = dijkstra(csgraph=graph, directed=False, indices=0)
y = dijkstra(csgraph=graph, directed=False, indices=n - 1)
print(x)
print(y)
for i in range(n):
    print(int(x[i] + y[i]))
