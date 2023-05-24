graph = [[1, 2, 5], [ 4, 7, 1], [ 9, 7, 5], [ 4, 6, 8], [ 3, 10, 3]]

def bfs(graph, v):
	visited = {v}
	to_explore = [v]
	while to_explore:
		u = to_explore.pop(0)
		print(u)
		new_vertices = [i for i in graph[u] if i not in visited]
		to_explore.extend(new_vertices)
		visited.update(new_vertices)
		
bfs( graph, 0)

