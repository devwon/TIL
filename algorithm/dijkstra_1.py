# dijkstra algorithm 이용한 전보 문제
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)     # 무한 = 10억


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리(0) push -> 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 pop
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split(' '))
# n, m, start = map(int, f.read().split(' '))

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
c = 0
# 모든 간선 정보를 입력받기
# for _ in range(m):
# x, y, z = map(int, input().split(' '))
f = open("test.txt", "r")
for line in f.readlines():
    c += 1
    print('line {}:{}'.format(c, line.strip()))
    x, y, z = map(int, line.strip().split(' '))
    print('x:{} y:{} z:{}'.format(x, y, z))
    # x번 노드에서 y번 노드로 가는 비용은 z
    graph[x].append((y, z))
print('graph: ', graph)

# 다익스트라 알고리즘 실행
dijkstra(start)

count = 0  # 도달할 수 있는 노드의 개수
# 도달 할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1 출력
print(count - 1, max_distance)
