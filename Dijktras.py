#!/usr/bin/env python
# coding: utf-8

# In[21]:


from numpy import Inf

def Dijkstra(graph, start):
    num_nodes = len(graph)
    distances = [Inf] * num_nodes
    distances[start] = 0
    visited = [False] * num_nodes
    
    for _ in range(num_nodes):
        current_node = -1
        
        for node in range(num_nodes):
            if not visited[node] and (current_node == -1 or distances[node] < distances[current_node]):
                current_node = node
        
        if distances[current_node] == Inf:
            break
        
        visited[current_node] = True
        
        for neighbor, dist in graph[current_node]:
            new_distance = distances[current_node] + dist
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    
    return distances

graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}

Dijkstra(graph, 0)


# In[48]:


from numpy import Inf

def Dijkstra(graph,start):
    N = len(graph)
    distances = [Inf] * N
    distances[start] = 0
    visited = [False] * N
    
    
    for _ in range(N):
        current_node = -1
        
        for i in range(N):
            if not visited[i] and (current_node == -1 or distances[i] < distances[current_node]):
                current_node = i
                
        if distances[current_node] == Inf:
                break
        visited[current_node] = True   
                
        for neighbour,dist in graph[current_node]:
            new_dist = distances[current_node] + dist
            if new_dist < distances[neighbour]:
                distances[neighbour] = new_dist
    return distances


graph = {
    0: [(1, 1),(2,2)],
    1: [(0, 1), (2, 3)],
    2: [(0, 2), (1, 3), (3, 2)],
    3: [(2, 2), (4, 1)],
    4: [(1, 2), (3, 1)]
}
 
Dijkstra(graph,0)


# In[ ]:




