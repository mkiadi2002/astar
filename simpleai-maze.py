import math
from models import SearchProblem # it is in the models
from traditional import astar # it is in the traditional
#import threading
#from termcolor import colored
#import time
#import numpy as np
#import pandas as pd
import os
# Class containing the methods to solve the maze
class MazeSolver(SearchProblem): # the class MazeSolver contains the methods that we need to solve the problem
#class MazeSolver(SearchProblem, threading.Thread): # the class MazeSolver contains the methods that we need to solve the problem
    # Initialize the class. Board is the MAP
    def __init__(self, board):
        #threading.Thread.__init__(self)
        self.board = board
        # the print (board) shows the list of lists, in which each sub-list is one row in the MAP
#        print(f"The thread in the main file is {threading.current_thread().name}")

        self.goal = (0, 0)

        # now extract the start and goal positions
        for y in range(len(self.board)):
            # y is number of rows. So it is from (0,11). print (range(len(self.board)))
            for x in range(len(self.board[y])):
                # each x is from (0,33), that is # of columns . print (x)
                if self.board[y][x].lower() == os.getenv('agent_start'):
                    self.initial = (x, y)
                    print ("")
                    print ("%% found o %%")
                    print ("||I am in the main file in the init() method||")
                    print ("================================================")
                    print (f"The start point is {self.initial} and is:<< {self.board[y][x].lower()}>>")
                    print ("")
#                elif self.board[y][x].lower() == "a":
#                    self.initial = (x, y)
#                    print("")
#                    print ("%% found a %%")
#                    print ("||I am in the main file in the init() method||")
#                    print ("================================================")
#                    print (f"The start point is {self.initial} and is:<< {self.board[y][x].lower()}>>")
#                elif self.board[y][x].lower() == "c":
#                    self.initial = (x, y)
                elif self.board[y][x].lower() == os.getenv('agent_finish'):
                    self.goal = (x, y)
#                elif self.board[y][x].lower() == "b":
#                    self.goal = (x, y)
#                elif self.board[y][x].lower() == "d":
#                    self.goal = (x, y)
#                    #print (f"The goal is {self.goal}")
                    #print ("")
        # the Mazesolver inherits the SearchProblme class

        #print(threading.current_thread().name)
        super(MazeSolver, self).__init__(initial_state=self.initial)

        #super(MazeSolver, self).__init__(initial_state=self.initial)
    #threading.Thread.actions(initial_state)
    # Define the method that generates the list of actions that can be performed from that particular state. We override the action method
#    def run(self):
#        pass
        #print(str(self.thread_name) +"  "+ str(self.thread_ID));
##       super(MazeSolver, self).__init__(initial_state=self.initial1)
#       t1 = threading.Thread(target=problem1.actions, args=(self.initial,), name='t1')
#       t1.start() #When a thread instance is created, it doesn’t start executing until its start()
#       #method (which invokes the target function with the arguments you supplied) is invoked.
##       problem1.join()
##       super(MazeSolver, self).__init__(initial_state=self.initial2)
#       t2 = threading.Thread(target=problem2.actions, args=(self.initial,), name='t2')
#       t2.start()
#       problem2.join()

    def actions(self, state):
        actions = [] # the list of valid actions for this state
        print("")
        print ("||I am in the main file in the action() method||")
        #print(f"The thread in the actions method of the main file is {threading.current_thread().name}")
        print ("============valid and invalid moves======================================")
        for action in COSTS.keys(): #COSTS is a dictoinary defined later down
            newx, newy = self.result(state, action) #result method is defined in the following. It gets a state and generates an action
            if self.board[newy][newx] != "#": # remove the actions that result in an obstacle
                actions.append(action)
            if self.board[newy][newx] == "#": # remove the actions that result in an obstacle
                print (f"`{action}` hits the obstacle")
        # you can print the candidate actions of a state. print (actions). The possible actions are like a list for each state
        print (f"Generated actions to generate the successors of the {state} are: {actions}")
        print (f"The successors of the {state} are" , actions)
        print ("")
        return actions

    # Getting the new state if an action is taken. We do not really pick the action now. This is just to simulate the action to get the valid moves.
    def result(self, state, action):
        x, y = state

        if action.count("up"):
            y -= 1
        if action.count("down"):
            y += 1
        if action.count("left"):
            x -= 1
        if action.count("right"):
            x += 1

        new_state = (x, y)

        return new_state

    # Check if we have reached the goal
    def is_goal(self, state):
        return state == self.goal

    # Compute the cost of taking an action to move to the neighbour nodes
    def cost(self, state, action, state2):
        return COSTS[action]

    # Heuristic that we use to arrive at the solution. We use Euclidian distance in this case
    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal

        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2) # we use this in the models, class SearchNodeHeuristicOrdered

if __name__ == "__main__":
    # Define the map
    MAP1 = """
    ##############################
    #         #              #   #
    # ####    ########        #  #
    #    #    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #           #
    #  o   #     #   #  #  #   ###
    #     #####    #    #  # x   #
    #              #       #     #
    ##############################
    """
#    MAP2 = """
#    ##############################
#    #         #              #   #
#    # ####    ########        #  #
#    #    #    #             #    #
#    #    ###     #####  ######   #
#    #      #   ###   #           #
#    #      #     #   #b #  #   ###
#    #  a  #####    #    #  #     #
#    #              #       #     #
#    ##############################
#    """
#    MAP3 = """
#    ##############################
#    #         #              #   #
#    # ####    ########        #  #
#    #     #    #             #   #
#    #    ###     #####  ######   #
#    # c    #   ###  #            #
#    #      #     #   # d#  #   ###
#    #     #####    #    #  #     #
#    #              #       #     #
#    ##############################
#    """

    # Convert map to a list
    print(MAP1)
    MAP1 = [list(x) for x in MAP1.split("\n") if x]

#    print(MAP2)
#    MAP2 = [list(x) for x in MAP2.split("\n") if x]
#
#    print(MAP3)
#    MAP3 = [list(x) for x in MAP3.split("\n") if x]
#    #     Define cost of moving around the map. The diagonal moves is more expensive than vertical moves
    cost_regular = 1.0
    cost_diagonal = 1.7

    # Create the cost dictionary
    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular,
        "up left": cost_diagonal,
        "up right": cost_diagonal,
        "down left": cost_diagonal,
        "down right": cost_diagonal,
    }

    # Create maze solver object
    #problem1=threading.Thread(target=MazeSolver, args=(MAP1,), kwargs={})
    problem1 = MazeSolver(MAP1)
#    problem1.start()
#    problem1.join()
#    problem2=threading.Thread(target=MazeSolver, args=(MAP2,), kwargs={})
#    problem2 = MazeSolver(MAP2)
##    time.sleep(20)
##    problem2.start()
##    print("")
#
#    problem3 = MazeSolver(MAP3)
#

#    t1 = threading.Thread(target=problem.actions, args=(MAP2), kwargs={})
#    t2 = threading.Thread(target=problem.actions, args=(MAP2), kwargs={})
#    t1.start()
#    t2.start()

    # Run the solver to get the result
#    result = astar(problem1, graph_search=True)

    print ("||In the main now we instantiate the astar() for problem 1||")
    result1 = astar(problem1, graph_search=True)# the astart() method is part of traditional.py library
    print ("||In the main now we instantiate the astar() for problem 2||")
#    result2 = astar(problem2, graph_search=True)
#    result3 = astar(problem3, graph_search=True)

    # Extract the path from the result
    path1 = [x[1] for x in result1.path()]
#    print (f"path 1 is: {path1}")
#    print (type(path1))
#    path2 = [x[1] for x in result2.path()]
#    path3 = [x[1] for x in result3.path()]

    # Print the result
    print()
    for y in range(len(MAP1)):
        for x in range(len(MAP1[y])):
            if (x, y) == problem1.initial:
                print('o', end='')
            elif (x, y) == problem1.goal:
                print('x', end='')
            elif (x, y) in path1:
                print('·', end='')
            else:
                print(MAP1[y][x], end='')

        print()

    print()

#    for y in range(len(MAP2)):
#        for x in range(len(MAP2[y])):
#            if (x, y) == problem2.initial:
#                print('a', end='')
#            elif (x, y) == problem2.goal:
#                print('b', end='')
#            elif (x, y) in path2:
#                print ('*', end='')
#            else:
#                print(MAP2[y][x], end='')
#        print()
#
#    for y in range(len(MAP3)):
#        for x in range(len(MAP3[y])):
#            if (x, y) == problem3.initial:
#                print('c', end='')
#            elif (x, y) == problem3.goal:
#                print('d', end='')
#            elif (x, y) in path3:
#                print ('+', end='')
#            else:
#                print(MAP3[y][x], end='')
#        print()
#    print("")
# Metaplanner
    #check if the goal of one agent is in the path of other agent.
    #In that case, there may be an issue as one agent may block other agent path forever
    #we need to detect this issue and let one agent goes after another
#    agent_num=3
##    AllPaths=[path1, path2, path3]
#    paths_priority=[] # this list sets which agents path has to be executed first due to blocking issue
#    #print (len(AllPaths))
#    #print (f" this is AllPaths: {AllPaths}")
#    for i in range(len(AllPaths)):
##        print (f"i is {i}")
#        #pick one of the paths
#        this_path= AllPaths[i]
#        #print (f"this_path is: {this_path}")
#        #create a list to hold the other paths
#        other_paths=[]
#        for j in range(len(AllPaths)):
##                print (f"j is {j}")
#                if i !=j:
##                continue
##            else
#                    other_paths.append(AllPaths[j])
#                    #print (f"other_path is: {other_paths}")
#                    #print (f"This is other_paths: {other_paths}")
#        for other_path in other_paths:
#            if this_path[-1] in other_path and (len(this_path) <= len(other_path)):
#               # if this_path is not other_path:
#                    #if (len(this_path) <= len(other_path)):
##                        print (this_path[-1] in other_path)
##                        print (len(this_path) <= len(other_path))
#                        paths_priority.append("low")
#

#        print ("I am in else")
#        paths_priority.append("no")
#    print (f"The agent1 has {paths_priority[0]} priority")
#    print (f"The agent2 has {paths_priority[1]} priority")
#    print (f"The agent3 has {paths_priority[2]} priority")
#    print ("---------------------------------")
#    #listing the steps and finding the waiting times
#    #print (l1size)
#    l1size=len(path1)
#    print (f"number of steps in path1 is: {l1size}")
#    l2size=len(path2)
#    print (f"number of steps in path2 is: {l2size}")
#    l3size=len(path3)
#    print (f"number of steps in path3 is: {l3size}")
#
    #print (l2size)
#    maxsize=max(l1size, l2size,l3size)
    #print (maxsize)
#    newpath1= path1[:maxsize] + [0]*(maxsize - len(path1))
#    newpath2= path2[:maxsize] + [0]*(maxsize - len(path2))
#    newpath3= path3[:maxsize] + [0]*(maxsize - len(path3))
#    for x in range(maxsize):
#        #print (x)
#        try:
#            newpath1[x]
#        except:
#            pass
#        try:
#            newpath2[x]
#        except:
#            pass
#        try:
#            newpath3[x]
#        except:
#            pass
#        if newpath1[x]==newpath2[x] and (newpath1[x]!=0 or newpath2[x]!=0 ) :
#            #push the path1 one step by adding a wait to current position
#            templst= newpath1[x:]
#            #print (path1[x])
#            #print(path2[x])
#            newpath1[x]=["w"]
#            newpath1=newpath1[0:x]+newpath1[x]+templst
#
#        if newpath1[x]==newpath3[x] and (newpath3[x]!=0 or newpath1[x]!=0):
#            #push the path3 one step by adding a wait to current position
#            templst= newpath3[x:]
#            #print (path1[x])
#            #print(path2[x])
#            newpath3[x]=["w"]
#            newpath3=newpath3[0:x]+newpath3[x]+templst
#
#        if newpath2[x]==newpath3[x] and (newpath2[x]!=0 or newpath3[x]!=0) :
#            #push the path2 one step by adding a wait to current position
#            templst= newpath2[x:]
#            #print (path1[x])
#            #print(path2[x])
#            newpath2[x]=["w"]
#            newpath2=newpath2[0:x]+newpath2[x]+templst
#        for i in range (3):
#            if newpath1[x]==newpath2[x] or newpath1[x]==newpath3[x] or newpath2[x]==newpath3[x] and (newpath1[x]!=0 and newpath2[x]!=0 and newpath3[x]!=0):
#                templst= newpath1[x:]
#                newpath1[x]=["w"]
#                newpath1=newpath1[0:x]+newpath1[x]+templst
#
#    print ("")
#    print (f"Path for Agent 1 is:")
#    for i in range(maxsize):
#        print (f"t{i}:{newpath1[i]}", end=' ')
#    print ("")
#    print("--------------")
#    print (f"Path for Agent 2 is:")
#    for i in range(maxsize):
#        print (f"t{i}:{newpath2[i]}", end=' ')
#    print ("")
#    print("--------------")
#    print (f"Path for Agent 3 is:")
#    for i in range(maxsize):
#        print (f"t{i}:{newpath3[i]}", end=' ')
#

