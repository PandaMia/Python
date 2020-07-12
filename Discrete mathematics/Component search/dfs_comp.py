from collections import defaultdict

def dfs_comp(adj_list, start):
    is_visited[start - 1] = True
    for vert in adj_list[start]:
        if not is_visited[vert - 1]:
            dfs_comp(adj_list, vert)

num_vert, num_edges = [int(i) for i in input().split()]

comp_count = 0
is_visited = [False] * num_vert
adj_list = defaultdict(list)

for i in range(num_edges):
    first_vert, second_vert = [int(i) for i in input().split()]
    adj_list[first_vert].append(second_vert)
    adj_list[second_vert].append(first_vert)

for i in range(num_vert):
    if not is_visited[i]:
        dfs_comp(adj_list, i + 1)
        comp_count += 1

print(comp_count)
