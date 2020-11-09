# Max-flow Ford-Fulkerson Algorithm
class Path:
    def __init__(self, path_flow):
        self.val = path_flow


def update(s, t, path_flow, parent, graph, res_net):
    if t == s:
        return
    update(s, parent[t], path_flow, parent, graph, res_net)
    res_net[parent[t]][t] -= path_flow.val
    res_net[t][parent[t]] += path_flow.val


def find_path(res_net, s, t, path_flow, visited, parent):
    # print("vertex:", s, end=" ")
    if s == t:
        return True
    visited[s] = True
    for u in range(len(res_net)):
        if res_net[s][u] > 0:
            if not visited[u]:
                parent[u] = s
                path_flow.val = min(path_flow.val, res_net[s][u])
                if find_path(res_net, u, t, path_flow, visited, parent):
                    return True
    return False


def ford_fulkerson(graph, s, t):
    res_net = [[graph[i][j] for j in range(len(graph))] for i in range(len(graph))]
    max_flow = 0
    path_flow = Path(float('inf'))
    while True:
        visited = [False for _ in range(len(graph))]
        parent = [-1 for _ in range(len(graph))]
        path_flow.val = float('inf')

        exist = find_path(res_net, s, t, path_flow, visited, parent)
        # print("\n", path_flow.val, "\n")

        if not exist:
            break
        else:
            max_flow += path_flow.val
            update(s, t, path_flow, parent, graph, res_net)

    return max_flow


graph = [
    [0, 4, 0, 0, 3, 0],
    [0, 0, 2, 0, 2, 0],
    [0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 2],
    [0, 0, 0, 5, 0, 0],
]
graph2 = [
    [0, 16, 0, 0, 13, 0],
    [0, 0, 12, 0, 0, 0],
    [0, 0, 0, 20, 9, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 14],
    [0, 0, 7, 4, 0, 0],
]

graph3 = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2

s1 = 0
t1 = 3
print(ford_fulkerson(c, s1, t1))  # wypisze 3

s2 = 0
t2 = 5
print(ford_fulkerson(graph3, s2, t2))

