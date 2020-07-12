from collections import Counter, defaultdict

def dfs(current, color=0):
    if color == 1:    
        colored[current - 1] = 1
    is_visited[current - 1] = True
    for vert in adj_list[current]:
        if not is_visited[vert - 1]:
            adj_list[current][vert] -= 1
            adj_list[vert][current] -= 1
            dfs(vert, color=(color+1)%2)

def check_visit(current):
    while sum(is_visited) != num_vert:
        if not is_visited[current - 1]:
            dfs(current)
        current += 1

num_vert, num_edge = [int(i) for i in input().split()]
is_visited = [False] * num_vert
colored = [0] * num_vert
adj_list = defaultdict(Counter)

for i in range(num_edge):
    first, second = [int(i) for i in input().split()]
    adj_list[first][second] += 1
    adj_list[second][first] += 1

check_visit(1)

flag = True
for first, adj in adj_list.items():
    if flag:
        for second in adj:
            if adj_list[first][second] > 0:
                if colored[first - 1] == colored[second - 1]:
                    flag = False
                    break

print('YES' if flag else 'NO')
