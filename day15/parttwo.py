from my_utils import draw
import math

filename = 'input.txt'


def get_point(matrix, point):
	(x, y) = point
	if y < 0 or x < 0:
		return None
	if y >= len(matrix)*5:
		return None
	row = matrix[y % len(matrix)]
	if x >= len(row) * 5:
		return None
	val = (row[x%len(row)] + math.floor(x/len(row)) + math.floor(y/len(matrix)))
	return (val -1 ) % 9 + 1

def get_adj(matrix, point):
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	points = [(point[0] + x, point[1] + y) for (x, y) in directions]
	return [(x, y) for (x, y) in points if get_point(matrix, (x, y))]

def get_shortest_path():
	matrix = [[int(g) for g in l.strip()] for l in open(filename)]
	start = (0, 0)
	end = (len(matrix[-1])*5-1, len(matrix)*5-1)
	explorer = [{"path": [start], "value": 0}]	
	visited = set()

	while len(explorer) > 0:
		explorer.sort(key=lambda x:x["value"])
		explore = explorer[0]
		explorer = explorer[1:]
		path = explore["path"]
		value = explore["value"]
		node = path[-1]
		if node in visited:
			continue
	
		visited.add(node)
		
		new_paths = []
		for adj in get_adj(matrix, node):
			if adj in visited:
				continue
			adj_value = get_point(matrix, adj)
			new_path = {"path": path + [adj], "value": value + adj_value}
			if adj == end:
				return new_path
			new_paths += [new_path]
		explorer += new_paths

draw.grid(get_shortest_path()['path'])
