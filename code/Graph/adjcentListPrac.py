graph = [[1,2],[2,3],[2],[],[5],[6],[]]

# 0 = not visited, 1 = visiting, -1 = safe
visited = [ 0 ] * len(graph)
result = []
def dfs(node):
    if visited[node] == -1:
        return True
    if visited[node] == 1:
        return False
    visited[node] = 1
    for neighbor in graph[node]:
        if not dfs(neighbor):
            return False
    visited[node] = -1  # mark as safe
    return True

for i in range(len(graph)):
    if dfs(i):
        result.append(i)
print(result)
