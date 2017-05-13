"""
Graph-based solution to the water pouring problem in Peter Norvig's Udacity course. 

The problem: 

Given 2 glasses of capacities X and Y, find the minimum number of steps to measure an arbitrary quantity of water Q. In each step, the possible actions are: filled one of the glasses from a sink, empty a glass or pour the content of one glass into the other. 

"""

def pour_problem(X,Y,goal,start=(0,0)):
  """X and Y are the capacities of glasses.
    (x,y) are the current fill levels and represent a state
    The goal is the goal level of each glass
    Keep track of the frontier and previously explored."""
    
  if goal is start:
    return [start]
    
  explored = set() # set of states we've already visited
  frontier = [[start]] # ordered list of paths
  
  while frontier:
    
    path = frontier.pop(0)
    (x,y) = path[-1]
    
    for state, action in succesors(x,y,X,Y).items():
      
      if state not in explored:
        
        explored.add(state)
        
        path2 = path + [action,state]
        
        if goal in state:
          return path2
        else:
          frontier.append(path2)
          
  return Fail


def succesors(x,y,X,Y):
  """ Return a dictionary {state:action} pairs describing what can be reached from the (x,y) state and how"""
  return {( (0,y+x) if y+x<=Y else (x-(Y-y), y+(Y-y)) ):'X->Y',
          ( (x+y,0) if y+x<=X else (x+(X-x), y-(X-x)) ):'X<-Y',
          (X,y): 'fill X', (x,Y): 'fill Y',
          (0,y): 'empty X', (x,0): 'empty Y'}

Fail = []

if __name__ == '__main__':

  print pour_problem(4,9,3)


        
    
    
  
  
    
    
    
    
    
    
    
    
    
