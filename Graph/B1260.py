# DFS와 BFS
# dictionary 이용해서 간선, 방문 check 표현
# list 를 queue 방식으로 사용

graph = dict()  # graph expression
check = dict()  # visiting check dictionary


def dfs(x):
    check[x] = 1
    print(x, end=" ")
    for nextItem in graph[x]:
        if check[nextItem] == 0:
            dfs(nextItem)


def bfs(start):
    q = []
    check[start] = 1
    q.append(start)
    while len(q) != 0:
        x = q.pop(0)
        print(x, end=" ")
        for i in graph[x]:
            if check[i] == 0:
                check[i] = 1
                q.append(i)


if __name__ == "__main__":
    n, m, start = map(int, input().split())
    for i in range(m):
        fromN, toN = map(int, input().split())
        check[fromN] = 0    # check 딕셔너리에 등록
        check[toN] = 0      # check 딕셔너리에 등록
        if fromN not in graph:
            graph[fromN] = [toN]
        else:
            graph[fromN].append(toN)
        if toN not in graph:
            graph[toN] = [fromN]
        else:
            graph[toN].append(fromN)
    for i in graph:
        graph[i].sort()     # 딕셔너리 value 부분 정렬
    dfs(start)
    print()
    for i in check.keys():  # check 딕셔너리 초기화
        check[i] = 0
    bfs(start)