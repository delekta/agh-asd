# recursion stack, visited and on recursion stack


# using pointers to Time complexity: O(V^2), without Time complexity O(V^3)
# curr_elements keeps tracks of vertices currently in recursion
def dfs(G, v, visited, curr_elements, pointers):
    visited[v] = True
    curr_elements[v] = True
    for u in range(pointers[v], len(G)):
        pointers[v] = u
        if G[v][u] == 1:
            if not visited[u]:
                if dfs(G, u, visited, curr_elements, pointers):
                    return True
            if curr_elements[u]:
                return True
    curr_elements[v] = False
    return False


def is_cycle(G):
    visited = [False for _ in range(len(G))]
    curr_elements = [False for _ in range(len(G))]
    pointers = [0 for _ in range(len(G))]
    for v in range(len(G)):
        if not visited[v]:
            if dfs(G, v, visited, curr_elements, pointers):
                return True
    return False


G = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
]


print(is_cycle(G))



