#bfs구현
from collections import deque
n, m, v = map(int, input().split()) #공백을 기준으로 구분하여입력

#n은 정점의 개수 (출력시 행의 개수)
#m은 간선의 개수 (입력시 열의 개수)
#v는 탐색을 시작할 정점의 개수

# graph를 입력받아서 list에 저장하기
# 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


# dfs 코딩
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end =" ")
                
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

# bfs 코딩
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end =" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)


