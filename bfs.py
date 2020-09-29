from collections import defaultdict 

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.queue=[]
        self.stack=[]
       
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
       
    
    def bfsSearch(self, key): 
        printTrees(self.graph)
        print("BFS search")
        self.queue.append(key)
        while(self.queue != []):
            
            
            popped = self.queue.pop(0)
            for i in self.graph[popped]:
            
                self.queue.append(i)
            if(self.queue == []):
                print(popped)
            else:
                print(popped, end='->')

    def dfsSearch(self, key, reverse=False): 
        print("\nDFS search")
        self.stack.append(key)
        while(self.stack != []):
            popped = self.stack.pop()
            
            if(reverse):
                childList = reversed(self.graph[popped])
            else:
                childList = self.graph[popped]
            for i in childList:
            
                self.stack.append(i)
           
            if(self.stack == []):
                print(popped)
            else:
                print(popped, end='->') 
    

def printTrees(t,c=0):
    r=0
    for key in t:
        if(c%2==0):
            
            if(r==1):
               print ("\t"*7+str(key)) 
            else:
                print ("\t"*5+str(key))
        else:
            print("\t"*3+str(key))
            r=1
            c=c+1

        if not isinstance(t,list):
            
            printTrees(t[key],c+1)


g = Graph() 
g.addEdge("A", "B") 
g.addEdge("A", "C") 
g.addEdge("B", "D") 
g.addEdge("B", "E") 
g.addEdge("C", "F") 
g.addEdge("C", "G")

g.bfsSearch("A") 

g.dfsSearch("A",reverse=True)
