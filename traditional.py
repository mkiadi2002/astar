# coding=utf-8
from utils import FifoList, BoundedPriorityQueue, LifoList
from models import (SearchNode, SearchNodeHeuristicOrdered,
                                    SearchNodeStarOrdered,
                                    SearchNodeCostOrdered)
#import threading


def breadth_first(problem, graph_search=False, viewer=None):
    '''
    Breadth first search.
    If graph_search=True, will avoid exploring repeated states.
    Requires: SearchProblem.actions, SearchProblem.result, and
    SearchProblem.is_goal.
    '''
    return _search(problem,
                   FifoList(),
                   graph_search=graph_search,
                   viewer=viewer)


def depth_first(problem, graph_search=False, viewer=None):
    '''
    Depth first search.
    If graph_search=True, will avoid exploring repeated states.
    Requires: SearchProblem.actions, SearchProblem.result, and
    SearchProblem.is_goal.
    '''
    return _search(problem,
                   LifoList(),
                   graph_search=graph_search,
                   viewer=viewer)


def limited_depth_first(problem, depth_limit, graph_search=False, viewer=None):
    '''
    Limited depth first search.
    Depth_limit is the maximum depth allowed, being depth 0 the initial state.
    If graph_search=True, will avoid exploring repeated states.
    Requires: SearchProblem.actions, SearchProblem.result, and
    SearchProblem.is_goal.
    '''
    return _search(problem,
                   LifoList(),
                   graph_search=graph_search,
                   depth_limit=depth_limit,
                   viewer=viewer)


def iterative_limited_depth_first(problem, graph_search=False, viewer=None):
    '''
    Iterative limited depth first search.
    If graph_search=True, will avoid exploring repeated states.
    Requires: SearchProblem.actions, SearchProblem.result, and
    SearchProblem.is_goal.
    '''
    solution = None
    limit = 0

    while not solution:
        solution = limited_depth_first(problem,
                                       depth_limit=limit,
                                       graph_search=graph_search,
                                       viewer=viewer)
        limit += 1

    if viewer:
        viewer.event('no_more_runs', solution, 'returned after %i runs' % limit)

    return solution


def uniform_cost(problem, graph_search=False, viewer=None):
    '''
    Uniform cost search.
    If graph_search=True, will avoid exploring repeated states.
    Requires: SearchProblem.actions, SearchProblem.result,
    SearchProblem.is_goal, and SearchProblem.cost.
    '''
    return _search(problem,
                   BoundedPriorityQueue(),
                   graph_search=graph_search,
                   node_factory=SearchNodeCostOrdered,
                   graph_replace_when_better=True,
                   viewer=viewer)


def greedy(problem, graph_search=False, viewer=None):
    '''
    Greedy search.
    If graph_search=True, will avoid exploring repeated states.
    Requires: SearchProblem.actions, SearchProblem.result,
    SearchProblem.is_goal, SearchProblem.cost, and SearchProblem.heuristic.
    '''
    return _search(problem,
                   BoundedPriorityQueue(),
                   graph_search=graph_search,
                   node_factory=SearchNodeHeuristicOrdered,
                   graph_replace_when_better=True,
                   viewer=viewer)


def astar(problem, graph_search=False, viewer=None):
    '''
    A* search.
    If graph_search=True, will avoid exploring repeated states.
    Requires: SearchProblem.actions, SearchProblem.result,
    SearchProblem.is_goal, SearchProblem.cost, and SearchProblem.heuristic.
    '''
    print ("I am in astar() now in traditional")
    return _search(problem,
                   BoundedPriorityQueue(), # this is defined in the utils
                   graph_search=graph_search,
                   node_factory=SearchNodeStarOrdered, # this is defined in the models. This is a class name so an object of this class is created as it is passed as an argument to a function
                   graph_replace_when_better=True,
                   viewer=viewer)


def _search(problem, fringe, graph_search=False, depth_limit=None, #fring is the name of the boundedpriorityqueue())
            node_factory=SearchNode, graph_replace_when_better=False,
            viewer=None):
    '''
    Basic search algorithm, base of all the other search algorithms.
        '''
    print ("I am in the _search() in traditional")
    if viewer:
        viewer.event('started')

    memory = set() # this is same as CLOSED list
    initial_node = node_factory(state=problem.initial_state,  #nodefactory is in the model, where the nodes are expanded
                                problem=problem)

    fringe.append(initial_node)  #see the BoundedPriorityQueue().append in the utils. This is where the first node is pushed to heap

    while fringe:  # fring here is the priorityqueue that has the opened sucsessors 
        if viewer:
            viewer.event('new_iteration', fringe.sorted())

        node = fringe.pop() #see the BoundedPriorityQueue().pop in the utils. The smallest is poped from the queue. The node here is like the CLOSED list
        print ("||print from the traditional in the _search class, fringe loop||")
        print (f"The node to save in the CLOSED list is {node}")
        #print ("=================================================")
        #print (f" The node [ {node.state} ] has been popped up and returned to tradition. ")
        print ("")

        if problem.is_goal(node.state):
            if viewer:
                viewer.event('chosen_node', node, True)
                viewer.event('finished', fringe.sorted(), node, 'goal found')
            return node
        else:
            if viewer:
                viewer.event('chosen_node', node, False)

        memory.add(node.state)  # here rather than keeping the CLOSED list in a python list, we keep them in a python set
        print ("CLOSED List in traditional has these nodes:", *memory)

        if depth_limit is None or node.depth < depth_limit:
            expanded = node.expand()
            #print (*expanded)
            if viewer:
                viewer.event('expanded', [node], [expanded])

            for n in expanded:
                if graph_search:
                    others = [x for x in fringe if x.state == n.state]
                    assert len(others) in (0, 1)
                    if n.state not in memory and len(others) == 0:
                        fringe.append(n)
                    elif graph_replace_when_better and len(others) > 0 and n < others[0]:
                        fringe.remove(others[0])
                        fringe.append(n)
                else:
                    fringe.append(n) # here we add each node to the OPEN list through the util module

    if viewer:
        viewer.event('finished', fringe.sorted(), None, 'goal not found')