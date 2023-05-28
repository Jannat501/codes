

def graph_coloring(graph, colors):
    vertices = list(graph.keys())
    n = len(vertices)
    result = {}

    def is_safe(vertex, color):
        for neighbor in graph[vertex]:
            if neighbor in result and result[neighbor] == color:
                return False
        return True

    def backtrack(index):
        if index == n:
            return True
        
        vertex = vertices[index]
        for color in colors:
            if is_safe(vertex, color):
                result[vertex] = color

                if backtrack(index + 1):
                    return True

                del result[vertex]

        return False

    if backtrack(0):
        return result
    else:
        return "No solution found"

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

solution = graph_coloring(graph, colors)
print(solution)