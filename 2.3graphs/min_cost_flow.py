from queue import PriorityQueue


# we have a graph G = (V,E) given as adjacency matrix each cell represented as (flow, cost)
def relax(u, v, graph, res_net, distance, parents, visited, queue, flow):
    if distance[v] > distance[u] + graph[u][v][1]:
        distance[v] = distance[u] + graph[u][v][1]
        flow[v] = min(flow[v], res_net[u][v])
        parents[v] = u
        if not visited[v]:
            queue.put((distance[v], v))


def find_path(graph, res_net, s, t, distance, visited, parents):
    queue = PriorityQueue()
    distance[s] = 0
    queue.put((distance[s], s))
    flow = [float('inf') for _ in range(len(graph))]

    while not queue.empty():
        u = queue.get()[1]
        if not visited[u]:
            visited[u] = True
            for v in range(len(graph)):
                if res_net[u][v] > 0:
                    relax(u, v, graph, res_net, distance, parents, visited, queue, flow)
    return distance[t], flow[t]


def update_resnet(s, t, res_net, parents, path_flow):
    if t == s:
        return
    update_resnet(s, parents[t], res_net, parents, path_flow)
    res_net[parents[t]][t] -= path_flow
    res_net[t][parents[t]] += path_flow


def min_cost_flow(graph, s, t, expected_flow):
    res_net = [[graph[i][j][0] for j in range(len(graph))] for i in range(len(graph))]
    curr_flow = 0
    total_cost = 0
    lap = 1

    while curr_flow < expected_flow:
        visited = [False for _ in range(len(graph))]
        parents = [-1 for _ in range(len(graph))]
        distance = [float('inf') for _ in range(len(graph))]

        cost, path_flow = find_path(graph, res_net, s, t, distance, visited, parents)

        print("lap: ", lap, "cost: ", cost, "path flow: ", path_flow)
        lap += 1

        if cost == float('inf'):
            print("Total possible flow is smaller than searched flow")
            break

        if curr_flow + path_flow < expected_flow:
            total_cost += cost * path_flow
        else:
            total_cost += cost * (expected_flow - curr_flow)

        curr_flow += path_flow

        update_resnet(s, t, res_net, parents, path_flow)

    return total_cost


# edges represented as (max_flow, cost)
graph = [
    [(0, 0), (3, 2), (3, 8), (3, 1), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (1, 10), (5, 5), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (1, 1), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (1, 10), (2, 3), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 7)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 4)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
]

s = 0
t = 6
expected_flow = 5
print(min_cost_flow(graph, s, t, expected_flow))
