class Graph:

	def __init__(self):
		self._graph = {}

	def add_edge(self, vertice, edge):
		if vertice not in self._graph:
			self._graph[vertice] = []
		self._graph[vertice].append(edge)

	def add_vertice(self, vertice):
		if vertice in self._graph:
			return "Vertice had in Graph"
		self._graph[vertice] = []

	def bfs(self, start_node):
		res = []
		queue = []
		queue.append(start_node)
		visited = [start_node]
		while queue:
			node = queue.pop(0)
			res.append(node)
			for nei in self._graph[node]:
				if nei not in visited:
					visited.append(nei)
					queue.append(nei)
		return res

	def dfs(self, start_node):
		res = []
		queue = []
		queue.append(start_node)
		visited = [start_node]
		while queue:
			node = queue.pop()
			res.append(node)
			for nei in self._graph[node]:
				if nei not in visited:
					visited.append(nei)
					queue.append(nei)
		return res


if __name__ == '__main__':
	graph = Graph()
	graph.add_edge(1, 2)
	graph.add_edge(1, 3)
	graph.add_edge(2, 4)
	graph.add_edge(3, 5)
	graph.add_edge(4, 5)
	graph.add_edge(5, 4)

	print(graph.bfs(1))
	print(graph.dfs(1))
