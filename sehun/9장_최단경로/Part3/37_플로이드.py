n = int(input())
m = int(input())

INF = (1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  if c< graph[a][b]:
    graph[a][b] = c

#플로이드 알고리즘
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    print(graph[a][b], end=" ")
  print()