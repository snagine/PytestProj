import collections

def validPathBFS( n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # Store all edges in 'graph'.
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Store all the nodes to be visited in 'queue'.
    seen = [False] * n
    seen[source] = True
    queue = collections.deque([source])

    while queue:
        curr_node = queue.popleft()
        if curr_node == destination:
            return True

        # For all the neighbors of the current node, if we haven't visit it before,
        # add it to 'queue' and mark it as visited.
        for next_node in graph[curr_node]:
            if not seen[next_node]:
                seen[next_node] = True
                queue.append(next_node)

    return False

def validPathDFS( n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
# ans = validPathBFS(n, edges, source, destination)
ans = validPathDFS(n, edges, source, destination)
print(ans)

