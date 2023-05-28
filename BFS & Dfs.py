
graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = []
queue = []

def Bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m,end = " ")
              
        for neighbour in graph[m]:
            if neighbour not in visited:
              visited.append(neighbour)
              queue.append(neighbour)

print("BFS is :")  
Bfs(visited,graph,'5')             



###DFS#####


graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = set()


def Dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            Dfs(visited ,graph,neighbour)
print("DFS:") 
Dfs(visited ,graph,'5')

