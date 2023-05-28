#!/usr/bin/env python
# coding: utf-8

# In[5]:


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


# In[6]:


graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = set()

def DFS(visited,graph,node):
    if node not in visited:
        print(node,end= " ")
        visited.add(node)
        
        
        for neighbour in graph[node]:
            DFS(visited ,graph,neighbour)
print("DFS") 
DFS(visited ,graph,'5')


# In[9]:


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


def BFS(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    
    while queue:
        m = queue.pop(0)
        print(m,end = " ")
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
print("BFS:") 
BFS(visited ,graph,'5')


# In[ ]:





# In[11]:


INF = 999999

N = 5

G = [
    [0,19,5,0,0],
    [19,0,5,9,2],
    [5,5,0,9,2],
    [0,9,1,0,1],
    [0,2,6,1,0]]

selected_node = [0,0,0,0,0]

no_edge = 0

selected_node[0] = True

print("Edge :  Weight\n")

while(no_edge < N - 1):
    
    minimum = INF;
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if (not selected_node[n] and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
                        
    print(str(a) + "-"+str(b)+":"+str(G[a][b]))  
    selected_node[b] = True
    no_edge += 1


# In[ ]:




