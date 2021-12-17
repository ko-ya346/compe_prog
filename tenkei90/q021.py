def dfs(s, g, graph):
    checked[s] = True
    for v in graph[s]:
        if checked[v]:
            continue
        dfs(v, g, graph)





n, m = map(int, input().split())
G = [[] for _ in range(n)]
rG = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    rG[b].append(a)

for i in 
