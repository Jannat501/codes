#!/usr/bin/env python
# coding: utf-8

# In[8]:


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


# In[ ]:





# In[11]:


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

print("BFS is :")     
BFS(visited,graph,'5')


# In[13]:


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

print("Bfs is :")
Bfs(visited,graph,'5')


# In[ ]:




