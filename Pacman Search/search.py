# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    #getting the start state
    startstate=problem.getStartState

    #not going ahead if the goal state is the start state
    if problem.isGoalState(startstate()):
         return []
    
    #list of nodes to explored, we use stack because of DFS
    fringe = util.Stack()

    #list of nodes already traversed
    explorednodes = [] 

    #the steps taken from the start state to to the current state
    steps = [] 

    #start with 0 elements in the fringe
    fringe.push((startstate(),[]))
   
    
    #go ahead only if the fringe is not empty
    while not fringe.isEmpty():
        presentnode,steps = fringe.pop()

        #add the node to the explored nodes if traversed already
        if presentnode not in explorednodes:
            explorednodes.append(presentnode)

         
             #end if pacman reaches the goal node
            if problem.isGoalState(presentnode):
                return steps

            #add new states to the fringe and and calculate the new path
            for sucessors, action, stepCost in problem.getSuccessors(presentnode):
                fringe.push((sucessors, (steps + [action])))


def breadthFirstSearch(problem):
   
    #getting the start state
    startstate = problem.getStartState
    
    #not going ahead if the goal state is the start state
    if problem.isGoalState(startstate()):
         return []
    
    #list of nodes to explored, we use queue because of BFS
    fringe = util.Queue()

    #list of nodes already traversed
    explorednodes = [] 

    #the steps taken from the start state to to the current state
    steps = [] 

    #start with 0 elements in the fringe
    fringe.push((startstate(),[]))
   
    #go ahead only if the fringe is not empty
    while not fringe.isEmpty():
        presentnode,steps = fringe.pop()

        #add the node to the explored nodes if traversed already
        if presentnode not in explorednodes:
            explorednodes.append(presentnode)

             #end if pacman reaches the goal node
            if problem.isGoalState(presentnode):
                return steps

            #add new states to the fringe and and calculate the new path
            for successors, action, stepCost in problem.getSuccessors(presentnode):
                fringe.push((successors, (steps + [action])))


def uniformCostSearch(problem):
   
    #getting the start state
    startstate=problem.getStartState
    
    #not going ahead if the goal state is the start state
    if problem.isGoalState(startstate()):
         return []
    
    #list of nodes to explored, we use queue because of BFS
    fringe = util.PriorityQueue()

    #list of nodes already traversed
    explorednodes = [] 

    #the steps taken from the start state to to the current state
    steps = [] 

    #start with 0 elements in the fringe
    fringe.push((startstate(),[],0),0)
   
    #go ahead only if the fringe is not empty
    while not fringe.isEmpty():
        presentnode,steps,cumulativeCost = fringe.pop()

        #add the node to the explored nodes if traversed already
        if presentnode not in explorednodes:
            explorednodes.append(presentnode)

         
             #end if pacman reaches the goal node
            if problem.isGoalState(presentnode):
                return steps


            #add new states to the fringe and and calculate the new path
            for sucessors, action, stepCost in problem.getSuccessors(presentnode):
                g_n = cumulativeCost + stepCost #g_n is the cumulative cost
                fringe.push((sucessors, (steps + [action]), g_n),g_n)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    #getting the start state
    startstate = problem.getStartState
    
    #not going ahead if the goal state is the start state
    if problem.isGoalState(startstate()):
         return []
    
    #list of nodes to explored, we use queue because of BFS
    fringe = util.PriorityQueue()

    #list of nodes already traversed
    explorednodes = [] 

    #the steps taken from the start state to to the current state
    steps = [] 

    #start with 0 elements in the fringe
    fringe.push((startstate(),[],0),0)
   
    #go ahead only if the fringe is not empty
    while not fringe.isEmpty():
        presentnode, steps, cumulativeCost = fringe.pop() #cumulative cost before the current state

        #add the node to the explored nodes if traversed already
        if presentnode not in explorednodes:
            explorednodes.append(presentnode)

         
             #end if pacman reaches the goal node
            if problem.isGoalState(presentnode):
                return steps
                

            #find all the heirs of the present node
            heirs = problem.getSuccessors(presentnode)

            #add new states to the fringe and and calculate the new path
            for sucessors, action, stepCost in heirs:
                g_n = cumulativeCost + stepCost #g(n) is the cumulative cost to the current state
                f_n = g_n + heuristic(sucessors,problem) #since f(n)=g(n)+h(n)
                fringe.push((sucessors, (steps + [action]), g_n),f_n)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
