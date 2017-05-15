def insertionsort(array):
  
  for i in range(1,len(array)):
    curr = array[i]
    j=i
    while j>0 and curr<array[j-1]:
      #array[j], array[j-1] = array[j-1], array[j]
      array[j] = array[j-1]
      j=j-1
    array[j] = curr
  return array
       


def merge(half1,half2):
  
  result = half1+half2
  k = i = j = 0
  while k<len(half1)+len(half2):
    if i<len(half1) and (j==len(half2) or half1[i]<=half2[j]): 
      result[k] = half1[i]
      i=i+1
    else:
      result[k]=half2[j]
      j=j+1
    k=k+1
  #print half1, half2, result
  return result
     
  
def mergesort(array):

  if len(array)<2:
    return array
    
  #1. divide in halves

  k = len(array)//2
 
  
  half1 = array[0:k] 
  half2 = array[k:len(array)]
  
  #2. sort each half
  sorted_half1 = mergesort(half1)
  sorted_half2 = mergesort(half2)
    
  #3. merge sorted halfs
  m = merge(sorted_half1,sorted_half2) 
  return m

def tests():

  a = [5,4,1,0,3,2]
  print a
  print insertionsort(a)    
  print mergesort(a)
  print merge([1,0],[2,3])
    
  'All tests passed :)'
    
if __name__ == '__main__':
  tests()  

