'''
@author: Devangini Patel
'''

from Node import Node
from State import State
from collections import deque
from classmates import *

def BFS_dongli(graph, initial, goal):
    """
    This function performs BFS search using a queue
    """
    '''
    Handel the arguments errors  
    '''
    if graph is None:
        print("Error: The graph is not provided.")
        return
    if initial not in graph or goal not in graph:
        print("Error: One or both of the passed names do not exist in the graph.")
        return
    #create queue
    queue = deque([]) 
    #since it is a graph, we create visited list
    visited = [] 
    #create root node
    initialState = State(initial)
    root = Node(initialState)
    #add to queue and visited list
    queue.append(root)    
    visited.append(root.state.name)
    reached = False
    # check if there is something in queue to dequeue
    while len(queue) > 0:
        
        #get first item in queue
        currentNode = queue.popleft()
        
        print (("-- dequeue --"), currentNode.state.name)
        
        #check if this is goal state
        if currentNode.state.checkGoalState(goal):
            print ("reached goal state")
            #print the path
            print ("----------------------")
            print ("Path")
            currentNode.printPath()
            reached = True
            break           
        #get the child nodes 
        childStates = currentNode.state.successorFunction(graph)
        for childState in childStates:
            
            childNode = Node(State(childState))
            
            #check if node is not visited
            if childNode.state.name not in visited:
                
                #add this node to visited nodes
                visited.append(childNode.state.name)
                
                
                #add to tree and queue
                currentNode.addChild(childNode)
                queue.append(childNode)                        
    #print tree
    print ("----------------------")
    if not reached:
        print(f'Sorry, {goal} cannot be reached.')
    else:
        print ("Tree")
        root.printTree()
        
    
BFS_dongli(relationships, 'Frank', 'Dolly')