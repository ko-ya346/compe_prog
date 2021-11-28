# https://atcoder.jp/contests/typical90/tasks/typical90_m
import heapq
from typing import List, Tuple


def dijkstra(size: int, graph: List[List[Tuple]], start: int) -> List[int]:
    """
    startを起点として、各頂点への最短距離を求める

    Parameters
    ----------
    size: 頂点の数
    graph:
        ([[(iと繋がってる点, 距離)...]
            for i in range(n)])
    start: 開始地点
    """
    dist = [float("inf")] * size  # startからiまでの最短距離
    dist[start] = 0
    h = []  # 探索候補のedgeを入れていく
    heapq.heappush(h, start)

    while len(h) != 0:
        # 現在の頂点
        v = heapq.heappop(h)
        for nv, weight in graph[v]:
            if dist[v] + weight < dist[nv]:
                # よりコストの低いルートが見つかれば更新し、探索候補に追加する
                dist[nv] = dist[v] + weight
                heapq.heappush(h, nv)
    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))


y = dijkstra(n, graph, n - 1)
x = dijkstra(n, graph, 0)
for i in range(n):
    print(x[i] + y[i])
