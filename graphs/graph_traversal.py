from collections import deque
          
def dfs_with_recu(graph, start):
  discovered = set(start)
  path = []
  return dfs_helper(graph,start,discovered,path)
  
def dfs_helper(graph,start,discovered,path):
  
  path.append(start)    
  for neighbour in graph[start]:
    if neighbour not in discovered:
      discovered.add(neighbour)
      dfs_helper(graph,neighbour,discovered,path)
      
  return path

def dfs_with_stack(graph, start):
    path = []
    discovered = set()
    stack = list()
    stack.append(start)  
    discovered.add(start)
    while stack:
        vertex = stack.pop()
        path.append(vertex)
        for neighbour in graph[vertex]:
          if neighbour not in discovered:
            discovered.add(neighbour)
            stack.append(neighbour)
    return path   

def bfs(graph, start):
    path = []
    discovered = set(start)
    queue = deque(start)
    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for neighbour in graph[vertex]:
          if neighbour not in discovered:
            discovered.add(neighbour)
            queue.append(neighbour)
    return path
        
def test():
  
  graph = {'A': ['B','C','D'],
         'B': ['E', 'D','A'],
         'C': ['A', 'D'],
         'D': ['A','B','C'],
         'E': ['B','F'],
         'F': ['E']}

  assert dfs_with_recu(graph,'A') in [['A', 'B', 'E', 'F', 'D', 'C'],['A', 'D', 'C','B', 'E', 'F',]]
  assert dfs_with_stack(graph,'A') in [['A', 'B', 'E', 'F', 'D', 'C'],['A', 'D', 'C','B', 'E', 'F',]]
  
  assert bfs(graph,'A')==['A','B','C', 'D','E', 'F']
  
  print "All tests passed :)"

if __name__ == '__main__':
  test()



