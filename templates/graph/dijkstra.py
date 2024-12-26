from  typing import *
import heapq
#dj单源最短路
#朴素o(n^2)做法
def djmins(n, source, edges):
    dis = [10 ** 12 for i in range(n)]
    visit = [0 for i in range(n)]
    graph = [[] for i in range(n)]
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    fals = [source for i in range(n)]
    dis[source] = 0
    u = source
    for i in range(n):
        visit[u] = 1
        for node, c in graph[u]:
            if not visit[node]:
                if dis[u] + c < dis[node]:
                    fals[node] = u
                    dis[node] = min(dis[node], dis[u] + c)
        minnode = -1
        mindis = 10 ** 19
        for node in range(n):
            if dis[node] < mindis and not visit[node]:
                minnode = node
                mindis = dis[node]
        u = minnode
    return dis

#堆优化o(nlogn)
def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

        graph = [[] for i in range(n)]
        mindic = {}
        for a, b, w in edges:
            if (a, b) in mindic:
                mindic[(a, b)] = min(mindic[(a, b)], w)
            else:
                mindic[(a, b)] = w
        for key in mindic:
            a, b = key
            graph[a].append((b, mindic[key]))
            graph[b].append((a, mindic[key]))
        #print(graph)
        dis = [10 ** 15 for i in range(n)]
        dis[0] = 0
        vis = set()
        q = [(0, 0)]
        while q:
            time, node = heapq.heappop(q)
            if node in vis:
                continue
            vis.add(node)
            for nxt, w in graph[node]:
                if disappear[nxt] > w + time and dis[nxt] > dis[node] + w:
                    dis[nxt] = dis[node] + w
                    heapq.heappush(q, (dis[nxt], nxt))
        # print(dis)
        ans = [-1] * n
        for i in range(n):
            if dis[i] < 10 ** 15:
                ans[i] = dis[i]
        return ans


