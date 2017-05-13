from collections import defaultdict
from heapq import *
import Queue

def dijkstra(g,start_node,end_node):

  if start_node == end_node: return 0    
  if start_node not in g: return False
  if end_node not in g: return False

  queue = Queue.PriorityQueue()
    
  distances={start_node: 0}
  queue.put((0, start_node))
  path = []      

  while not queue.empty():
     
    _, current_node = queue.get()
    path = path+list(current_node)
    
    if current_node == end_node:
      return path, distances[current_node]
      
    for nbr in g[current_node]:
    
      tentative_distance = distances[current_node] + g[current_node][nbr]
      
      if nbr not in distances.keys() or distances[nbr] > tentative_distance:
        distances[nbr] = tentative_distance
        queue.put((distances[nbr], nbr))

  return False
  
def tests():

  g = {'A' : {'B': 1, 'C': 5},
       'B' : {'A': 1, 'D': 1},
       'C' : {'A': 5, 'D': 1},
       'D' : {'B': 1, 'C': 1}}
    
  assert dijkstra(g,'A','C')[1]==3
  assert dijkstra(g,'A','C')[0]==['A','B','D','C']
  
  assert dijkstra(g,'A','G')==False
  assert dijkstra(g,'A','D')[1]==2
  
  print 'All tests passed :)'
  
if __name__ == "__main__":
  tests()

