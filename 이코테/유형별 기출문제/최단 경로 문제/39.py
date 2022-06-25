#
# 이코테 - 유형별 기출 문제
# DP
# 39. 정확한 순위
#
"""
아이디어 : 플로이드 워셜 알고리즘 O(n^3), 성적 비교를 그래프로 표현
"""
INF = int(1e9)

n, m = map(int, input().split())

graph = [
    [INF] * (n+1)
    for _ in range(n+1)
]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans=0
for a in range(1, n+1):
    tmp = True  # 기록 모두 아는지
    for b in range(1, n+1):
        if graph[a][b] >= INF and graph[b][a] >= INF:
            tmp = False
    if tmp:
        ans += 1
            
print(ans)
