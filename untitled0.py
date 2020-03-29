I am in the SearchNodeStarOrdered class of the models


    ##############################
    #         #              #   #
    # ####    ########        #  #
    #    #    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #    o      #
    #      #     #   #  #  #   ###
    #     #####    #    #  # x   #
    #              #       #     #
    ##############################
    

    ##############################
    #         #              #   #
    # ####    ########        #  #
    #     #    #             #   #
    #    ###     #####  ######   #
    #      #   ###   #           #
    # a    #     #   #  #  #   ###
    #     #####    #    #  #     #
    #              #       #   b #
    ##############################
    

%% found o %%
||I am in the main file in the init() method||
================================================
The start point is (26, 5) and is:<< o>>

I am in the SearchProblem class of the models

The self.initial_state is (26, 5)

%% found a %%
||I am in the main file in the init() method||
================================================
The start point is (6, 6) and is:<< a>>
I am in the SearchProblem class of the models

The self.initial_state is (6, 6)

||In the main now we instantiate the astar() for problem 1||
I am in astar() now in traditional
I am in the _search() in traditional

I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 3.605551275463989

||From utils.append() method: we push the Node <(26, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 5)>


||From utils.pop() method: we pop() Node <(26, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(26, 5)>

CLOSED List in traditional has these nodes: (26, 5)
In the expand () method of the model now, we have this state: (26, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (26, 5) are: ['down', 'left', 'right', 'down left']
The successors of the (26, 5) are ['down', 'left', 'right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (26, 5) with action `down` toward ---> (26, 6)
cost from (26, 5) to --> (26, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 3.1622776601683795

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (26, 5) with action `left` toward ---> (25, 5)
cost from (26, 5) to --> (25, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 4.47213595499958


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 4.47213595499958

Node <(25, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>, Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (26, 5) with action `right` toward ---> (27, 5)
cost from (26, 5) to --> (27, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(27, 5)>, Node <(26, 6)>, Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (26, 5) with action `down left` toward ---> (25, 6)
cost from (26, 5) to --> (25, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 4.123105625617661


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 4.123105625617661

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(27, 5)>, Node <(25, 6)>, Node <(26, 6)>, Node <(25, 5)>}]

||From utils.append() method: we push the Node <(26, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)>

||From utils.append() method: we push the Node <(25, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)> Node <(25, 5)>

||From utils.append() method: we push the Node <(27, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(27, 5)> Node <(25, 5)> Node <(26, 6)>

||From utils.append() method: we push the Node <(25, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(27, 5)> Node <(25, 5)> Node <(26, 6)> Node <(25, 6)>


||From utils.pop() method: we pop() Node <(27, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(27, 5)>

CLOSED List in traditional has these nodes: (26, 5) (27, 5)
In the expand () method of the model now, we have this state: (27, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (27, 5) are: ['left', 'right', 'down left', 'down right']
The successors of the (27, 5) are ['left', 'right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (27, 5) with action `left` toward ---> (26, 5)
cost from (27, 5) to --> (26, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 3.605551275463989

Node <(26, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (27, 5) with action `right` toward ---> (28, 5)
cost from (27, 5) to --> (28, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 2.23606797749979

Node <(28, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (27, 5) with action `down left` toward ---> (26, 6)
cost from (27, 5) to --> (26, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 3.1622776601683795

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>, Node <(28, 5)>, Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (27, 5) with action `down right` toward ---> (28, 6)
cost from (27, 5) to --> (28, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 1.4142135623730951


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 1.4142135623730951

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 6)>, Node <(26, 6)>, Node <(28, 5)>, Node <(26, 5)>}]

||From utils.append() method: we push the Node <(28, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)> Node <(28, 5)> Node <(25, 6)> Node <(25, 5)>

||From utils.append() method: we push the Node <(28, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 6)> Node <(26, 6)> Node <(25, 6)> Node <(25, 5)> Node <(28, 5)>


||From utils.pop() method: we pop() Node <(28, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(28, 6)>

CLOSED List in traditional has these nodes: (26, 5) (28, 6) (27, 5)
In the expand () method of the model now, we have this state: (28, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (28, 6) are: ['up', 'down', 'right', 'up left', 'up right', 'down right']
The successors of the (28, 6) are ['up', 'down', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (28, 6) with action `up` toward ---> (28, 5)
cost from (28, 6) to --> (28, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 2.23606797749979

Node <(28, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (28, 6) with action `down` toward ---> (28, 7)
cost from (28, 6) to --> (28, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 1.0

Node <(28, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(28, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (28, 6) with action `right` toward ---> (29, 6)
cost from (28, 6) to --> (29, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 1.0

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(28, 7)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (28, 6) with action `up left` toward ---> (27, 5)
cost from (28, 6) to --> (27, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(28, 7)>, Node <(29, 6)>, Node <(27, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (28, 6) with action `up right` toward ---> (29, 5)
cost from (28, 6) to --> (29, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 2.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 2.0

Node <(29, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(27, 5)>, Node <(29, 5)>, Node <(28, 7)>, Node <(28, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (28, 6) with action `down right` toward ---> (29, 7)
cost from (28, 6) to --> (29, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 0.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 0.0

Node <(29, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(27, 5)>, Node <(29, 5)>, Node <(28, 7)>, Node <(28, 5)>, Node <(29, 7)>}]

||From utils.append() method: we push the Node <(28, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)> Node <(28, 5)> Node <(25, 6)> Node <(25, 5)> Node <(28, 7)>

||From utils.append() method: we push the Node <(29, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)> Node <(28, 5)> Node <(29, 6)> Node <(25, 5)> Node <(28, 7)> Node <(25, 6)>

||From utils.append() method: we push the Node <(29, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)> Node <(28, 5)> Node <(29, 6)> Node <(25, 5)> Node <(28, 7)> Node <(25, 6)> Node <(29, 5)>

||From utils.append() method: we push the Node <(29, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)> Node <(28, 5)> Node <(29, 6)> Node <(29, 7)> Node <(28, 7)> Node <(25, 6)> Node <(29, 5)> Node <(25, 5)>


||From utils.pop() method: we pop() Node <(26, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(26, 6)>

CLOSED List in traditional has these nodes: (26, 5) (26, 6) (28, 6) (27, 5)
In the expand () method of the model now, we have this state: (26, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (26, 6) are: ['up', 'down', 'left', 'up left', 'up right', 'down left']
The successors of the (26, 6) are ['up', 'down', 'left', 'up left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (26, 6) with action `up` toward ---> (26, 5)
cost from (26, 6) to --> (26, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 3.605551275463989

Node <(26, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (26, 6) with action `down` toward ---> (26, 7)
cost from (26, 6) to --> (26, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 3.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 3.0

Node <(26, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>, Node <(26, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (26, 6) with action `left` toward ---> (25, 6)
cost from (26, 6) to --> (25, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 4.123105625617661


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 4.123105625617661

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>, Node <(26, 7)>, Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (26, 6) with action `up left` toward ---> (25, 5)
cost from (26, 6) to --> (25, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 4.47213595499958


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 4.47213595499958

Node <(25, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>, Node <(25, 5)>, Node <(26, 7)>, Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (26, 6) with action `up right` toward ---> (27, 5)
cost from (26, 6) to --> (27, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(25, 5)>, Node <(26, 7)>, Node <(26, 5)>, Node <(27, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (26, 6) with action `down left` toward ---> (25, 7)
cost from (26, 6) to --> (25, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 4.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 4.0

Node <(25, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(25, 5)>, Node <(26, 7)>, Node <(25, 7)>, Node <(26, 5)>, Node <(27, 5)>}]

||From utils.append() method: we push the Node <(26, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 5)> Node <(29, 7)> Node <(29, 6)> Node <(26, 7)> Node <(28, 7)> Node <(25, 6)> Node <(29, 5)> Node <(25, 5)>

||From utils.append() method: we push the Node <(25, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 5)> Node <(29, 7)> Node <(29, 6)> Node <(26, 7)> Node <(28, 7)> Node <(25, 6)> Node <(29, 5)> Node <(25, 5)> Node <(25, 7)>


||From utils.pop() method: we pop() Node <(28, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(28, 5)>

CLOSED List in traditional has these nodes: (28, 5) (26, 5) (27, 5) (26, 6) (28, 6)
In the expand () method of the model now, we have this state: (28, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (28, 5) are: ['down', 'left', 'right', 'down right']
The successors of the (28, 5) are ['down', 'left', 'right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (28, 5) with action `down` toward ---> (28, 6)
cost from (28, 5) to --> (28, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 1.4142135623730951


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 1.4142135623730951

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (28, 5) with action `left` toward ---> (27, 5)
cost from (28, 5) to --> (27, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 2.8284271247461903

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 6)>, Node <(27, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (28, 5) with action `right` toward ---> (29, 5)
cost from (28, 5) to --> (29, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 2.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 2.0

Node <(29, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>, Node <(28, 6)>, Node <(27, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (28, 5) with action `down right` toward ---> (29, 6)
cost from (28, 5) to --> (29, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 1.0

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>, Node <(29, 6)>, Node <(28, 6)>, Node <(27, 5)>}]

||From utils.append() method: we push the Node <(29, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(29, 7)> Node <(28, 7)> Node <(29, 6)> Node <(26, 7)> Node <(25, 7)> Node <(25, 6)> Node <(25, 5)> Node <(29, 5)>


||From utils.pop() method: we pop() Node <(29, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(29, 7)>

||In the main now we instantiate the astar() for problem 2||
I am in astar() now in traditional
I am in the _search() in traditional

I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

||From utils.append() method: we push the Node <(6, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 6)>


||From utils.pop() method: we pop() Node <(6, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(6, 6)>

CLOSED List in traditional has these nodes: (6, 6)
In the expand () method of the model now, we have this state: (6, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (6, 6) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (6, 6) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (6, 6) with action `up` toward ---> (6, 5)
cost from (6, 6) to --> (6, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (6, 6) with action `down` toward ---> (6, 7)
cost from (6, 6) to --> (6, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 7)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (6, 6) with action `left` toward ---> (5, 6)
cost from (6, 6) to --> (5, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597

Node <(5, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 7)>, Node <(5, 6)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (6, 6) with action `right` toward ---> (7, 6)
cost from (6, 6) to --> (7, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(6, 7)>, Node <(5, 6)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (6, 6) with action `up left` toward ---> (5, 5)
cost from (6, 6) to --> (5, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048

Node <(5, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(5, 6)>, Node <(6, 7)>, Node <(5, 5)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (6, 6) with action `up right` toward ---> (7, 5)
cost from (6, 6) to --> (7, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(5, 6)>, Node <(7, 5)>, Node <(6, 7)>, Node <(5, 5)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (6, 6) with action `down left` toward ---> (5, 7)
cost from (6, 6) to --> (5, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376

Node <(5, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(5, 6)>, Node <(7, 5)>, Node <(6, 7)>, Node <(5, 7)>, Node <(5, 5)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (6, 6) with action `down right` toward ---> (7, 7)
cost from (6, 6) to --> (7, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(5, 6)>, Node <(7, 5)>, Node <(6, 7)>, Node <(5, 7)>, Node <(5, 5)>, Node <(6, 5)>, Node <(7, 7)>}]

||From utils.append() method: we push the Node <(6, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 5)>

||From utils.append() method: we push the Node <(6, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 7)> Node <(6, 5)>

||From utils.append() method: we push the Node <(5, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 7)> Node <(6, 5)> Node <(5, 6)>

||From utils.append() method: we push the Node <(7, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(7, 6)> Node <(6, 7)> Node <(5, 6)> Node <(6, 5)>

||From utils.append() method: we push the Node <(5, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(7, 6)> Node <(6, 7)> Node <(5, 6)> Node <(6, 5)> Node <(5, 5)>

||From utils.append() method: we push the Node <(7, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(7, 6)> Node <(6, 7)> Node <(7, 5)> Node <(6, 5)> Node <(5, 5)> Node <(5, 6)>

||From utils.append() method: we push the Node <(5, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(7, 6)> Node <(6, 7)> Node <(7, 5)> Node <(6, 5)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)>

||From utils.append() method: we push the Node <(7, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(7, 6)> Node <(7, 7)> Node <(7, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 5)>


||From utils.pop() method: we pop() Node <(7, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(7, 6)>

CLOSED List in traditional has these nodes: (7, 6) (6, 6)
In the expand () method of the model now, we have this state: (7, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (7, 6) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (7, 6) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (7, 6) with action `up` toward ---> (7, 5)
cost from (7, 6) to --> (7, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (7, 6) with action `down` toward ---> (7, 7)
cost from (7, 6) to --> (7, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 7)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (7, 6) with action `left` toward ---> (6, 6)
cost from (7, 6) to --> (6, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 7)>, Node <(6, 6)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (7, 6) with action `right` toward ---> (8, 6)
cost from (7, 6) to --> (8, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 7)>, Node <(8, 6)>, Node <(6, 6)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (7, 6) with action `up left` toward ---> (6, 5)
cost from (7, 6) to --> (6, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(7, 5)>, Node <(6, 5)>, Node <(7, 7)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (7, 6) with action `up right` toward ---> (8, 5)
cost from (7, 6) to --> (8, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403

Node <(8, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(7, 5)>, Node <(6, 5)>, Node <(7, 7)>, Node <(8, 5)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (7, 6) with action `down left` toward ---> (6, 7)
cost from (7, 6) to --> (6, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 7)>, Node <(8, 6)>, Node <(7, 5)>, Node <(6, 5)>, Node <(7, 7)>, Node <(8, 5)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (7, 6) with action `down right` toward ---> (8, 7)
cost from (7, 6) to --> (8, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 7)>, Node <(8, 6)>, Node <(8, 7)>, Node <(7, 5)>, Node <(6, 5)>, Node <(7, 7)>, Node <(8, 5)>, Node <(6, 6)>}]

||From utils.append() method: we push the Node <(8, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 6)> Node <(7, 7)> Node <(7, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 5)>

||From utils.append() method: we push the Node <(8, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 6)> Node <(7, 7)> Node <(7, 5)> Node <(8, 5)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)>

||From utils.append() method: we push the Node <(8, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 6)> Node <(7, 7)> Node <(7, 5)> Node <(8, 5)> Node <(8, 7)> Node <(5, 6)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)>


||From utils.pop() method: we pop() Node <(8, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(8, 6)>

CLOSED List in traditional has these nodes: (8, 6) (7, 6) (6, 6)
In the expand () method of the model now, we have this state: (8, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (8, 6) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (8, 6) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (8, 6) with action `up` toward ---> (8, 5)
cost from (8, 6) to --> (8, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403

Node <(8, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (8, 6) with action `down` toward ---> (8, 7)
cost from (8, 6) to --> (8, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 7)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (8, 6) with action `left` toward ---> (7, 6)
cost from (8, 6) to --> (7, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(8, 7)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (8, 6) with action `right` toward ---> (9, 6)
cost from (8, 6) to --> (9, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522

Node <(9, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(8, 7)>, Node <(8, 5)>, Node <(9, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (8, 6) with action `up left` toward ---> (7, 5)
cost from (8, 6) to --> (7, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(7, 5)>, Node <(8, 5)>, Node <(7, 6)>, Node <(8, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (8, 6) with action `up right` toward ---> (9, 5)
cost from (8, 6) to --> (9, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452

Node <(9, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(7, 5)>, Node <(8, 5)>, Node <(7, 6)>, Node <(9, 5)>, Node <(8, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (8, 6) with action `down left` toward ---> (7, 7)
cost from (8, 6) to --> (7, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(7, 5)>, Node <(8, 5)>, Node <(7, 6)>, Node <(9, 5)>, Node <(7, 7)>, Node <(8, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (8, 6) with action `down right` toward ---> (9, 7)
cost from (8, 6) to --> (9, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524

Node <(9, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(7, 5)>, Node <(8, 5)>, Node <(7, 6)>, Node <(9, 7)>, Node <(9, 5)>, Node <(7, 7)>, Node <(8, 7)>}]

||From utils.append() method: we push the Node <(9, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(9, 6)> Node <(7, 7)> Node <(7, 5)> Node <(8, 5)> Node <(8, 7)> Node <(5, 6)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)>

||From utils.append() method: we push the Node <(9, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(9, 6)> Node <(7, 7)> Node <(7, 5)> Node <(8, 5)> Node <(8, 7)> Node <(5, 6)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(9, 5)>

||From utils.append() method: we push the Node <(9, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(9, 6)> Node <(7, 7)> Node <(9, 7)> Node <(8, 5)> Node <(8, 7)> Node <(7, 5)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(9, 5)> Node <(5, 6)>


||From utils.pop() method: we pop() Node <(9, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(9, 6)>

CLOSED List in traditional has these nodes: (8, 6) (7, 6) (9, 6) (6, 6)
In the expand () method of the model now, we have this state: (9, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down right` hits the obstacle
Generated actions to generate the successors of the (9, 6) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left']
The successors of the (9, 6) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (9, 6) with action `up` toward ---> (9, 5)
cost from (9, 6) to --> (9, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452

Node <(9, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (9, 6) with action `down` toward ---> (9, 7)
cost from (9, 6) to --> (9, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524

Node <(9, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 5)>, Node <(9, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (9, 6) with action `left` toward ---> (8, 6)
cost from (9, 6) to --> (8, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 5)>, Node <(8, 6)>, Node <(9, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (9, 6) with action `right` toward ---> (10, 6)
cost from (9, 6) to --> (10, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988

Node <(10, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 5)>, Node <(10, 6)>, Node <(8, 6)>, Node <(9, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (9, 6) with action `up left` toward ---> (8, 5)
cost from (9, 6) to --> (8, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403

Node <(8, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 7)>, Node <(10, 6)>, Node <(8, 6)>, Node <(9, 5)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (9, 6) with action `up right` toward ---> (10, 5)
cost from (9, 6) to --> (10, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 5) is = 21.213203435596427


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 5) is = 21.213203435596427

Node <(10, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 7)>, Node <(10, 6)>, Node <(10, 5)>, Node <(8, 6)>, Node <(9, 5)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (9, 6) with action `down left` toward ---> (8, 7)
cost from (9, 6) to --> (8, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 7)>, Node <(8, 7)>, Node <(10, 6)>, Node <(10, 5)>, Node <(8, 6)>, Node <(9, 5)>, Node <(8, 5)>}]

||From utils.append() method: we push the Node <(10, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(10, 6)> Node <(8, 7)> Node <(7, 7)> Node <(8, 5)> Node <(9, 5)> Node <(9, 7)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(7, 5)>

||From utils.append() method: we push the Node <(10, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(10, 6)> Node <(8, 7)> Node <(7, 7)> Node <(8, 5)> Node <(9, 5)> Node <(9, 7)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(7, 5)> Node <(10, 5)>


||From utils.pop() method: we pop() Node <(10, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(10, 6)>

CLOSED List in traditional has these nodes: (6, 6) (7, 6) (10, 6) (8, 6) (9, 6)
In the expand () method of the model now, we have this state: (10, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`right` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (10, 6) are: ['up', 'left', 'up left', 'down left']
The successors of the (10, 6) are ['up', 'left', 'up left', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (10, 6) with action `up` toward ---> (10, 5)
cost from (10, 6) to --> (10, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 5) is = 21.213203435596427


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 5) is = 21.213203435596427

Node <(10, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (10, 6) with action `left` toward ---> (9, 6)
cost from (10, 6) to --> (9, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522

Node <(9, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(10, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (10, 6) with action `up left` toward ---> (9, 5)
cost from (10, 6) to --> (9, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452

Node <(9, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(10, 5)>, Node <(9, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (10, 6) with action `down left` toward ---> (9, 7)
cost from (10, 6) to --> (9, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524

Node <(9, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(10, 5)>, Node <(9, 5)>, Node <(9, 7)>}]


||From utils.pop() method: we pop() Node <(7, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(7, 7)>

CLOSED List in traditional has these nodes: (6, 6) (7, 6) (10, 6) (7, 7) (8, 6) (9, 6)
In the expand () method of the model now, we have this state: (7, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (7, 7) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (7, 7) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (7, 7) with action `up` toward ---> (7, 6)
cost from (7, 7) to --> (7, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (7, 7) with action `down` toward ---> (7, 8)
cost from (7, 7) to --> (7, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0

Node <(7, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 8)>, Node <(7, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (7, 7) with action `left` toward ---> (6, 7)
cost from (7, 7) to --> (6, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 8)>, Node <(7, 6)>, Node <(6, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (7, 7) with action `right` toward ---> (8, 7)
cost from (7, 7) to --> (8, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 8)>, Node <(8, 7)>, Node <(7, 6)>, Node <(6, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (7, 7) with action `up left` toward ---> (6, 6)
cost from (7, 7) to --> (6, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 7)>, Node <(7, 6)>, Node <(6, 6)>, Node <(7, 8)>, Node <(6, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (7, 7) with action `up right` toward ---> (8, 6)
cost from (7, 7) to --> (8, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(8, 7)>, Node <(7, 6)>, Node <(6, 6)>, Node <(7, 8)>, Node <(6, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (7, 7) with action `down left` toward ---> (6, 8)
cost from (7, 7) to --> (6, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0

Node <(6, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(8, 7)>, Node <(7, 6)>, Node <(6, 6)>, Node <(7, 8)>, Node <(6, 7)>, Node <(6, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (7, 7) with action `down right` toward ---> (8, 8)
cost from (7, 7) to --> (8, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0

Node <(8, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(8, 7)>, Node <(7, 6)>, Node <(8, 8)>, Node <(6, 6)>, Node <(7, 8)>, Node <(6, 7)>, Node <(6, 8)>}]

||From utils.append() method: we push the Node <(7, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 7)> Node <(8, 5)> Node <(9, 7)> Node <(10, 5)> Node <(9, 5)> Node <(7, 5)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(7, 8)>

||From utils.append() method: we push the Node <(6, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 7)> Node <(8, 5)> Node <(9, 7)> Node <(10, 5)> Node <(9, 5)> Node <(7, 5)> Node <(5, 7)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(7, 8)> Node <(6, 8)>

||From utils.append() method: we push the Node <(8, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 7)> Node <(8, 5)> Node <(9, 7)> Node <(10, 5)> Node <(9, 5)> Node <(7, 5)> Node <(8, 8)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(7, 8)> Node <(6, 8)> Node <(5, 7)>


||From utils.pop() method: we pop() Node <(8, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(8, 7)>

CLOSED List in traditional has these nodes: (6, 6) (7, 6) (10, 6) (7, 7) (8, 7) (8, 6) (9, 6)
In the expand () method of the model now, we have this state: (8, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (8, 7) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (8, 7) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (8, 7) with action `up` toward ---> (8, 6)
cost from (8, 7) to --> (8, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (8, 7) with action `down` toward ---> (8, 8)
cost from (8, 7) to --> (8, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0

Node <(8, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 8)>, Node <(8, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (8, 7) with action `left` toward ---> (7, 7)
cost from (8, 7) to --> (7, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 8)>, Node <(8, 6)>, Node <(7, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (8, 7) with action `right` toward ---> (9, 7)
cost from (8, 7) to --> (9, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524

Node <(9, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 7)>, Node <(8, 8)>, Node <(8, 6)>, Node <(7, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (8, 7) with action `up left` toward ---> (7, 6)
cost from (8, 7) to --> (7, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 8)>, Node <(8, 6)>, Node <(7, 7)>, Node <(9, 7)>, Node <(7, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (8, 7) with action `up right` toward ---> (9, 6)
cost from (8, 7) to --> (9, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522

Node <(9, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 8)>, Node <(9, 6)>, Node <(8, 6)>, Node <(7, 7)>, Node <(9, 7)>, Node <(7, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (8, 7) with action `down left` toward ---> (7, 8)
cost from (8, 7) to --> (7, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0

Node <(7, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 8)>, Node <(9, 6)>, Node <(8, 6)>, Node <(7, 7)>, Node <(9, 7)>, Node <(7, 6)>, Node <(7, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (8, 7) with action `down right` toward ---> (9, 8)
cost from (8, 7) to --> (9, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0

Node <(9, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 8)>, Node <(9, 6)>, Node <(8, 6)>, Node <(7, 7)>, Node <(9, 7)>, Node <(7, 6)>, Node <(9, 8)>, Node <(7, 8)>}]

||From utils.append() method: we push the Node <(9, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(9, 7)> Node <(8, 5)> Node <(7, 5)> Node <(10, 5)> Node <(9, 5)> Node <(7, 8)> Node <(8, 8)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 8)> Node <(9, 8)>


||From utils.pop() method: we pop() Node <(9, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(9, 7)>

CLOSED List in traditional has these nodes: (6, 6) (7, 6) (10, 6) (7, 7) (8, 7) (8, 6) (9, 6) (9, 7)
In the expand () method of the model now, we have this state: (9, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
Generated actions to generate the successors of the (9, 7) are: ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']
The successors of the (9, 7) are ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (9, 7) with action `up` toward ---> (9, 6)
cost from (9, 7) to --> (9, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522

Node <(9, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (9, 7) with action `down` toward ---> (9, 8)
cost from (9, 7) to --> (9, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0

Node <(9, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 8)>, Node <(9, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (9, 7) with action `left` toward ---> (8, 7)
cost from (9, 7) to --> (8, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 8)>, Node <(9, 6)>, Node <(8, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (9, 7) with action `up left` toward ---> (8, 6)
cost from (9, 7) to --> (8, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 8)>, Node <(9, 6)>, Node <(8, 6)>, Node <(8, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (9, 7) with action `up right` toward ---> (10, 6)
cost from (9, 7) to --> (10, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988

Node <(10, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 6)>, Node <(8, 7)>, Node <(9, 8)>, Node <(9, 6)>, Node <(8, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (9, 7) with action `down left` toward ---> (8, 8)
cost from (9, 7) to --> (8, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0

Node <(8, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 6)>, Node <(8, 8)>, Node <(8, 7)>, Node <(9, 8)>, Node <(9, 6)>, Node <(8, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (9, 7) with action `down right` toward ---> (10, 8)
cost from (9, 7) to --> (10, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 8) is = 21.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 8) is = 21.0

Node <(10, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 6)>, Node <(8, 8)>, Node <(8, 7)>, Node <(10, 8)>, Node <(9, 8)>, Node <(9, 6)>, Node <(8, 6)>}]

||From utils.append() method: we push the Node <(10, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(7, 5)> Node <(8, 5)> Node <(8, 8)> Node <(10, 5)> Node <(9, 5)> Node <(7, 8)> Node <(9, 8)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 8)> Node <(10, 8)>


||From utils.pop() method: we pop() Node <(7, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(7, 5)>

CLOSED List in traditional has these nodes: (6, 6) (7, 6) (10, 6) (7, 7) (7, 5) (8, 7) (8, 6) (9, 6) (9, 7)
In the expand () method of the model now, we have this state: (7, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (7, 5) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (7, 5) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (7, 5) with action `up` toward ---> (7, 4)
cost from (7, 5) to --> (7, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (7, 5) with action `down` toward ---> (7, 6)
cost from (7, 5) to --> (7, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (7, 5) with action `left` toward ---> (6, 5)
cost from (7, 5) to --> (6, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(7, 4)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (7, 5) with action `right` toward ---> (8, 5)
cost from (7, 5) to --> (8, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403

Node <(8, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(8, 5)>, Node <(7, 4)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (7, 5) with action `up left` toward ---> (6, 4)
cost from (7, 5) to --> (6, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(7, 6)>, Node <(6, 4)>, Node <(7, 4)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (7, 5) with action `up right` toward ---> (8, 4)
cost from (7, 5) to --> (8, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504

Node <(8, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(8, 4)>, Node <(7, 6)>, Node <(6, 4)>, Node <(7, 4)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (7, 5) with action `down left` toward ---> (6, 6)
cost from (7, 5) to --> (6, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(8, 4)>, Node <(6, 6)>, Node <(7, 6)>, Node <(6, 4)>, Node <(7, 4)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (7, 5) with action `down right` toward ---> (8, 6)
cost from (7, 5) to --> (8, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(8, 4)>, Node <(6, 6)>, Node <(7, 6)>, Node <(8, 6)>, Node <(6, 4)>, Node <(7, 4)>, Node <(8, 5)>}]

||From utils.append() method: we push the Node <(7, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 5)> Node <(9, 5)> Node <(8, 8)> Node <(10, 5)> Node <(10, 8)> Node <(7, 8)> Node <(9, 8)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 8)> Node <(7, 4)>

||From utils.append() method: we push the Node <(6, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 5)> Node <(9, 5)> Node <(8, 8)> Node <(10, 5)> Node <(10, 8)> Node <(7, 8)> Node <(9, 8)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 8)> Node <(7, 4)> Node <(6, 4)>

||From utils.append() method: we push the Node <(8, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 5)> Node <(9, 5)> Node <(8, 8)> Node <(10, 5)> Node <(10, 8)> Node <(7, 8)> Node <(9, 8)> Node <(6, 5)> Node <(6, 7)> Node <(5, 5)> Node <(5, 6)> Node <(5, 7)> Node <(6, 8)> Node <(7, 4)> Node <(6, 4)> Node <(8, 4)>


||From utils.pop() method: we pop() Node <(8, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(8, 5)>

CLOSED List in traditional has these nodes: (6, 6) (7, 6) (10, 6) (7, 7) (8, 5) (7, 5) (8, 7) (8, 6) (9, 6) (9, 7)
In the expand () method of the model now, we have this state: (8, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up right` hits the obstacle
Generated actions to generate the successors of the (8, 5) are: ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']
The successors of the (8, 5) are ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (8, 5) with action `up` toward ---> (8, 4)
cost from (8, 5) to --> (8, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504

Node <(8, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (8, 5) with action `down` toward ---> (8, 6)
cost from (8, 5) to --> (8, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(8, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (8, 5) with action `left` toward ---> (7, 5)
cost from (8, 5) to --> (7, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(8, 4)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (8, 5) with action `right` toward ---> (9, 5)
cost from (8, 5) to --> (9, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452

Node <(9, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(9, 5)>, Node <(8, 4)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (8, 5) with action `up left` toward ---> (7, 4)
cost from (8, 5) to --> (7, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(8, 4)>, Node <(9, 5)>, Node <(7, 4)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (8, 5) with action `down left` toward ---> (7, 6)
cost from (8, 5) to --> (7, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(8, 6)>, Node <(8, 4)>, Node <(9, 5)>, Node <(7, 4)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (8, 5) with action `down right` toward ---> (9, 6)
cost from (8, 5) to --> (9, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522

Node <(9, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 6)>, Node <(8, 6)>, Node <(8, 4)>, Node <(9, 6)>, Node <(9, 5)>, Node <(7, 4)>, Node <(7, 5)>}]


||From utils.pop() method: we pop() Node <(9, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(9, 5)>

CLOSED List in traditional has these nodes: (6, 6) (7, 6) (10, 6) (7, 7) (8, 5) (9, 5) (7, 5) (8, 7) (8, 6) (9, 6) (9, 7)
In the expand () method of the model now, we have this state: (9, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (9, 5) are: ['down', 'left', 'right', 'up left', 'down left', 'down right']
The successors of the (9, 5) are ['down', 'left', 'right', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (9, 5) with action `down` toward ---> (9, 6)
cost from (9, 5) to --> (9, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522

Node <(9, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (9, 5) with action `left` toward ---> (8, 5)
cost from (9, 5) to --> (8, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403

Node <(8, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (9, 5) with action `right` toward ---> (10, 5)
cost from (9, 5) to --> (10, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 5) is = 21.213203435596427


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 5) is = 21.213203435596427

Node <(10, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(8, 5)>, Node <(10, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (9, 5) with action `up left` toward ---> (8, 4)
cost from (9, 5) to --> (8, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504

Node <(8, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(8, 4)>, Node <(8, 5)>, Node <(10, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (9, 5) with action `down left` toward ---> (8, 6)
cost from (9, 5) to --> (8, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 6) is = 23.08679276123039

Node <(8, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 6)>, Node <(8, 5)>, Node <(10, 5)>, Node <(9, 6)>, Node <(8, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (9, 5) with action `down right` toward ---> (10, 6)
cost from (9, 5) to --> (10, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988

Node <(10, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 6)>, Node <(8, 6)>, Node <(8, 5)>, Node <(10, 5)>, Node <(9, 6)>, Node <(8, 4)>}]


||From utils.pop() method: we pop() Node <(10, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(10, 5)>

CLOSED List in traditional has these nodes: (10, 5) (6, 6) (7, 6) (10, 6) (7, 7) (8, 5) (9, 5) (7, 5) (8, 7) (8, 6) (9, 6) (9, 7)
In the expand () method of the model now, we have this state: (10, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`right` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (10, 5) are: ['down', 'left', 'down left']
The successors of the (10, 5) are ['down', 'left', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (10, 5) with action `down` toward ---> (10, 6)
cost from (10, 5) to --> (10, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 6) is = 21.095023109728988

Node <(10, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (10, 5) with action `left` toward ---> (9, 5)
cost from (10, 5) to --> (9, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452

Node <(9, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 5)>, Node <(10, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (10, 5) with action `down left` toward ---> (9, 6)
cost from (10, 5) to --> (9, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 6) is = 22.090722034374522

Node <(9, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 6)>, Node <(9, 5)>, Node <(10, 6)>}]


||From utils.pop() method: we pop() Node <(6, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(6, 7)>

CLOSED List in traditional has these nodes: (10, 5) (6, 7) (6, 6) (7, 6) (10, 6) (7, 7) (8, 5) (9, 5) (7, 5) (8, 7) (8, 6) (9, 6) (9, 7)
In the expand () method of the model now, we have this state: (6, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (6, 7) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (6, 7) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (6, 7) with action `up` toward ---> (6, 6)
cost from (6, 7) to --> (6, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (6, 7) with action `down` toward ---> (6, 8)
cost from (6, 7) to --> (6, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0

Node <(6, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 6)>, Node <(6, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (6, 7) with action `left` toward ---> (5, 7)
cost from (6, 7) to --> (5, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376

Node <(5, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 7)>, Node <(6, 6)>, Node <(6, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (6, 7) with action `right` toward ---> (7, 7)
cost from (6, 7) to --> (7, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 7)>, Node <(6, 6)>, Node <(6, 8)>, Node <(7, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (6, 7) with action `up left` toward ---> (5, 6)
cost from (6, 7) to --> (5, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597

Node <(5, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 8)>, Node <(5, 6)>, Node <(5, 7)>, Node <(7, 7)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (6, 7) with action `up right` toward ---> (7, 6)
cost from (6, 7) to --> (7, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 8)>, Node <(5, 6)>, Node <(5, 7)>, Node <(7, 6)>, Node <(7, 7)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (6, 7) with action `down left` toward ---> (5, 8)
cost from (6, 7) to --> (5, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 8) is = 26.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 8) is = 26.0

Node <(5, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 8)>, Node <(6, 8)>, Node <(5, 6)>, Node <(5, 7)>, Node <(7, 6)>, Node <(7, 7)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (6, 7) with action `down right` toward ---> (7, 8)
cost from (6, 7) to --> (7, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0

Node <(7, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 8)>, Node <(5, 8)>, Node <(6, 8)>, Node <(5, 6)>, Node <(5, 7)>, Node <(7, 6)>, Node <(7, 7)>, Node <(6, 6)>}]

||From utils.append() method: we push the Node <(6, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 5)> Node <(10, 8)> Node <(8, 8)> Node <(8, 4)> Node <(5, 6)> Node <(7, 8)> Node <(9, 8)> Node <(6, 4)> Node <(7, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 8)>

||From utils.append() method: we push the Node <(5, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 5)> Node <(10, 8)> Node <(8, 8)> Node <(8, 4)> Node <(5, 6)> Node <(7, 8)> Node <(9, 8)> Node <(6, 4)> Node <(7, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 8)> Node <(5, 8)>


||From utils.pop() method: we pop() Node <(6, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(6, 5)>

CLOSED List in traditional has these nodes: (10, 5) (6, 7) (6, 6) (7, 6) (10, 6) (7, 7) (8, 5) (9, 5) (7, 5) (8, 7) (8, 6) (9, 6) (6, 5) (9, 7)
In the expand () method of the model now, we have this state: (6, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (6, 5) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (6, 5) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (6, 5) with action `up` toward ---> (6, 4)
cost from (6, 5) to --> (6, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (6, 5) with action `down` toward ---> (6, 6)
cost from (6, 5) to --> (6, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 6)>, Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (6, 5) with action `left` toward ---> (5, 5)
cost from (6, 5) to --> (5, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048

Node <(5, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 6)>, Node <(5, 5)>, Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (6, 5) with action `right` toward ---> (7, 5)
cost from (6, 5) to --> (7, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 5)>, Node <(6, 6)>, Node <(5, 5)>, Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (6, 5) with action `up left` toward ---> (5, 4)
cost from (6, 5) to --> (5, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181

Node <(5, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(7, 5)>, Node <(6, 6)>, Node <(5, 5)>, Node <(5, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (6, 5) with action `up right` toward ---> (7, 4)
cost from (6, 5) to --> (7, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(7, 5)>, Node <(6, 6)>, Node <(5, 5)>, Node <(5, 4)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (6, 5) with action `down left` toward ---> (5, 6)
cost from (6, 5) to --> (5, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597

Node <(5, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(7, 5)>, Node <(6, 6)>, Node <(5, 5)>, Node <(5, 6)>, Node <(5, 4)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (6, 5) with action `down right` toward ---> (7, 6)
cost from (6, 5) to --> (7, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 6) is = 24.08318915758459

Node <(7, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(7, 5)>, Node <(6, 6)>, Node <(5, 5)>, Node <(5, 6)>, Node <(7, 6)>, Node <(5, 4)>, Node <(7, 4)>}]

||From utils.append() method: we push the Node <(6, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 8)> Node <(10, 8)> Node <(9, 8)> Node <(8, 4)> Node <(5, 6)> Node <(7, 8)> Node <(5, 8)> Node <(7, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 8)> Node <(6, 4)>

||From utils.append() method: we push the Node <(5, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(8, 8)> Node <(10, 8)> Node <(9, 8)> Node <(8, 4)> Node <(5, 6)> Node <(7, 8)> Node <(5, 8)> Node <(7, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 8)> Node <(6, 4)> Node <(5, 4)>


||From utils.pop() method: we pop() Node <(8, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(8, 8)>

CLOSED List in traditional has these nodes: (10, 5) (6, 7) (6, 6) (7, 6) (10, 6) (7, 7) (8, 5) (9, 5) (7, 5) (8, 8) (8, 7) (8, 6) (9, 6) (6, 5) (9, 7)
In the expand () method of the model now, we have this state: (8, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (8, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (8, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (8, 8) with action `up` toward ---> (8, 7)
cost from (8, 8) to --> (8, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (8, 8) with action `left` toward ---> (7, 8)
cost from (8, 8) to --> (7, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0

Node <(7, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 7)>, Node <(7, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (8, 8) with action `right` toward ---> (9, 8)
cost from (8, 8) to --> (9, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0

Node <(9, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 8)>, Node <(8, 7)>, Node <(7, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (8, 8) with action `up left` toward ---> (7, 7)
cost from (8, 8) to --> (7, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 8)>, Node <(7, 7)>, Node <(8, 7)>, Node <(7, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (8, 8) with action `up right` toward ---> (9, 7)
cost from (8, 8) to --> (9, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524

Node <(9, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 7)>, Node <(7, 7)>, Node <(9, 8)>, Node <(8, 7)>, Node <(7, 8)>}]


||From utils.pop() method: we pop() Node <(9, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(9, 8)>

CLOSED List in traditional has these nodes: (10, 5) (6, 7) (6, 6) (7, 6) (10, 6) (9, 8) (7, 7) (8, 5) (9, 5) (7, 5) (8, 8) (8, 7) (8, 6) (9, 6) (6, 5) (9, 7)
In the expand () method of the model now, we have this state: (9, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (9, 8) are: ['up', 'left', 'right', 'up left']
The successors of the (9, 8) are ['up', 'left', 'right', 'up left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (9, 8) with action `up` toward ---> (9, 7)
cost from (9, 8) to --> (9, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524

Node <(9, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (9, 8) with action `left` toward ---> (8, 8)
cost from (9, 8) to --> (8, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0

Node <(8, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 8)>, Node <(9, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (9, 8) with action `right` toward ---> (10, 8)
cost from (9, 8) to --> (10, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 8) is = 21.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 8) is = 21.0

Node <(10, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 8)>, Node <(8, 8)>, Node <(9, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (9, 8) with action `up left` toward ---> (8, 7)
cost from (9, 8) to --> (8, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 8)>, Node <(8, 7)>, Node <(8, 8)>, Node <(9, 7)>}]


||From utils.pop() method: we pop() Node <(10, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(10, 8)>

CLOSED List in traditional has these nodes: (10, 8) (10, 5) (6, 7) (6, 6) (7, 6) (10, 6) (9, 8) (7, 7) (8, 5) (9, 5) (7, 5) (8, 8) (8, 7) (8, 6) (9, 6) (6, 5) (9, 7)
In the expand () method of the model now, we have this state: (10, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (10, 8) are: ['left', 'right', 'up left']
The successors of the (10, 8) are ['left', 'right', 'up left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (10, 8) with action `left` toward ---> (9, 8)
cost from (10, 8) to --> (9, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 8) is = 22.0

Node <(9, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (10, 8) with action `right` toward ---> (11, 8)
cost from (10, 8) to --> (11, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 8) is = 20.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 8) is = 20.0

Node <(11, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 8)>, Node <(11, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (10, 8) with action `up left` toward ---> (9, 7)
cost from (10, 8) to --> (9, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 7) is = 22.02271554554524

Node <(9, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 7)>, Node <(9, 8)>, Node <(11, 8)>}]

||From utils.append() method: we push the Node <(11, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(11, 8)> Node <(7, 8)> Node <(6, 8)> Node <(7, 4)> Node <(8, 4)> Node <(6, 4)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(5, 6)>


||From utils.pop() method: we pop() Node <(11, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(11, 8)>

CLOSED List in traditional has these nodes: (10, 8) (10, 5) (6, 7) (6, 6) (11, 8) (7, 6) (10, 6) (9, 8) (7, 7) (8, 5) (9, 5) (7, 5) (8, 8) (8, 7) (8, 6) (9, 6) (6, 5) (9, 7)
In the expand () method of the model now, we have this state: (11, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (11, 8) are: ['left', 'right']
The successors of the (11, 8) are ['left', 'right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (11, 8) with action `left` toward ---> (10, 8)
cost from (11, 8) to --> (10, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 8) is = 21.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 8) is = 21.0

Node <(10, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (11, 8) with action `right` toward ---> (12, 8)
cost from (11, 8) to --> (12, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 8) is = 19.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 8) is = 19.0

Node <(12, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 8)>, Node <(10, 8)>}]

||From utils.append() method: we push the Node <(12, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(12, 8)> Node <(7, 8)> Node <(6, 8)> Node <(7, 4)> Node <(8, 4)> Node <(6, 4)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(5, 6)>


||From utils.pop() method: we pop() Node <(12, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(12, 8)>

CLOSED List in traditional has these nodes: (10, 8) (10, 5) (6, 7) (6, 6) (11, 8) (7, 6) (10, 6) (9, 8) (7, 7) (8, 5) (9, 5) (7, 5) (8, 8) (8, 7) (12, 8) (8, 6) (9, 6) (6, 5) (9, 7)
In the expand () method of the model now, we have this state: (12, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (12, 8) are: ['left', 'right']
The successors of the (12, 8) are ['left', 'right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (12, 8) with action `left` toward ---> (11, 8)
cost from (12, 8) to --> (11, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 8) is = 20.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 8) is = 20.0

Node <(11, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (12, 8) with action `right` toward ---> (13, 8)
cost from (12, 8) to --> (13, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 8) is = 18.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 8) is = 18.0

Node <(13, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 8)>, Node <(11, 8)>}]

||From utils.append() method: we push the Node <(13, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(13, 8)> Node <(7, 8)> Node <(6, 8)> Node <(7, 4)> Node <(8, 4)> Node <(6, 4)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(5, 6)>


||From utils.pop() method: we pop() Node <(13, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(13, 8)>

CLOSED List in traditional has these nodes: (10, 8) (10, 5) (6, 7) (6, 6) (11, 8) (7, 6) (10, 6) (9, 8) (7, 7) (8, 5) (9, 5) (7, 5) (8, 8) (8, 7) (12, 8) (13, 8) (8, 6) (9, 6) (6, 5) (9, 7)
In the expand () method of the model now, we have this state: (13, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (13, 8) are: ['left', 'right']
The successors of the (13, 8) are ['left', 'right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (13, 8) with action `left` toward ---> (12, 8)
cost from (13, 8) to --> (12, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 8) is = 19.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 8) is = 19.0

Node <(12, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (13, 8) with action `right` toward ---> (14, 8)
cost from (13, 8) to --> (14, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 8) is = 17.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 8) is = 17.0

Node <(14, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 8)>, Node <(12, 8)>}]

||From utils.append() method: we push the Node <(14, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(14, 8)> Node <(7, 8)> Node <(6, 8)> Node <(7, 4)> Node <(8, 4)> Node <(6, 4)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(5, 6)>


||From utils.pop() method: we pop() Node <(14, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(14, 8)>

CLOSED List in traditional has these nodes: (6, 6) (9, 8) (10, 6) (7, 7) (13, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (11, 8) (8, 8) (9, 5) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (14, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (14, 8) are: ['left', 'right', 'up right']
The successors of the (14, 8) are ['left', 'right', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (14, 8) with action `left` toward ---> (13, 8)
cost from (14, 8) to --> (13, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 8) is = 18.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 8) is = 18.0

Node <(13, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (14, 8) with action `right` toward ---> (15, 8)
cost from (14, 8) to --> (15, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0

Node <(15, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 8)>, Node <(13, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (14, 8) with action `up right` toward ---> (15, 7)
cost from (14, 8) to --> (15, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814

Node <(15, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 8)>, Node <(15, 7)>, Node <(13, 8)>}]

||From utils.append() method: we push the Node <(15, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(15, 8)> Node <(7, 8)> Node <(6, 8)> Node <(7, 4)> Node <(8, 4)> Node <(6, 4)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(5, 6)>

||From utils.append() method: we push the Node <(15, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(15, 8)> Node <(7, 8)> Node <(6, 8)> Node <(7, 4)> Node <(8, 4)> Node <(15, 7)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(5, 6)> Node <(6, 4)>


||From utils.pop() method: we pop() Node <(15, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(15, 8)>

CLOSED List in traditional has these nodes: (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (11, 8) (8, 8) (9, 5) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (15, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (15, 8) are: ['up', 'left', 'right', 'up right']
The successors of the (15, 8) are ['up', 'left', 'right', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (15, 8) with action `up` toward ---> (15, 7)
cost from (15, 8) to --> (15, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814

Node <(15, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (15, 8) with action `left` toward ---> (14, 8)
cost from (15, 8) to --> (14, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 8) is = 17.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 8) is = 17.0

Node <(14, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 8)>, Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (15, 8) with action `right` toward ---> (16, 8)
cost from (15, 8) to --> (16, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0

Node <(16, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 8)>, Node <(14, 8)>, Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (15, 8) with action `up right` toward ---> (16, 7)
cost from (15, 8) to --> (16, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908

Node <(16, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 8)>, Node <(14, 8)>, Node <(16, 7)>, Node <(15, 7)>}]

||From utils.append() method: we push the Node <(16, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 8)> Node <(8, 4)> Node <(7, 8)> Node <(7, 4)> Node <(5, 6)> Node <(6, 8)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(15, 7)>

||From utils.append() method: we push the Node <(16, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 8)> Node <(8, 4)> Node <(7, 8)> Node <(7, 4)> Node <(5, 6)> Node <(6, 8)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(15, 7)> Node <(16, 7)>


||From utils.pop() method: we pop() Node <(16, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(16, 8)>

CLOSED List in traditional has these nodes: (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (11, 8) (16, 8) (8, 8) (9, 5) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (16, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (16, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (16, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (16, 8) with action `up` toward ---> (16, 7)
cost from (16, 8) to --> (16, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908

Node <(16, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (16, 8) with action `left` toward ---> (15, 8)
cost from (16, 8) to --> (15, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0

Node <(15, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(15, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (16, 8) with action `right` toward ---> (17, 8)
cost from (16, 8) to --> (17, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0

Node <(17, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(15, 8)>, Node <(17, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (16, 8) with action `up left` toward ---> (15, 7)
cost from (16, 8) to --> (15, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814

Node <(15, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 7)>, Node <(16, 7)>, Node <(15, 8)>, Node <(17, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (16, 8) with action `up right` toward ---> (17, 7)
cost from (16, 8) to --> (17, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199

Node <(17, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(15, 8)>, Node <(17, 8)>, Node <(15, 7)>, Node <(17, 7)>}]

||From utils.append() method: we push the Node <(17, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(17, 8)> Node <(8, 4)> Node <(7, 8)> Node <(7, 4)> Node <(5, 6)> Node <(6, 8)> Node <(5, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(16, 7)> Node <(15, 7)>

||From utils.append() method: we push the Node <(17, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(17, 8)> Node <(8, 4)> Node <(7, 8)> Node <(7, 4)> Node <(5, 6)> Node <(6, 8)> Node <(17, 7)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(16, 7)> Node <(15, 7)> Node <(5, 8)>


||From utils.pop() method: we pop() Node <(17, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(17, 8)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (11, 8) (16, 8) (8, 8) (9, 5) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (17, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (17, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (17, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (17, 8) with action `up` toward ---> (17, 7)
cost from (17, 8) to --> (17, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199

Node <(17, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (17, 8) with action `left` toward ---> (16, 8)
cost from (17, 8) to --> (16, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0

Node <(16, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 7)>, Node <(16, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (17, 8) with action `right` toward ---> (18, 8)
cost from (17, 8) to --> (18, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 8) is = 13.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 8) is = 13.0

Node <(18, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 8)>, Node <(17, 7)>, Node <(16, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (17, 8) with action `up left` toward ---> (16, 7)
cost from (17, 8) to --> (16, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908

Node <(16, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(18, 8)>, Node <(17, 7)>, Node <(16, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (17, 8) with action `up right` toward ---> (18, 7)
cost from (17, 8) to --> (18, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298

Node <(18, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 7)>, Node <(18, 7)>, Node <(16, 7)>, Node <(18, 8)>, Node <(16, 8)>}]

||From utils.append() method: we push the Node <(18, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(18, 8)> Node <(8, 4)> Node <(7, 8)> Node <(7, 4)> Node <(5, 6)> Node <(15, 7)> Node <(6, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(16, 7)> Node <(5, 8)> Node <(17, 7)>

||From utils.append() method: we push the Node <(18, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(18, 8)> Node <(8, 4)> Node <(7, 8)> Node <(7, 4)> Node <(5, 6)> Node <(15, 7)> Node <(6, 8)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(16, 7)> Node <(5, 8)> Node <(17, 7)> Node <(18, 7)>


||From utils.pop() method: we pop() Node <(18, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(18, 8)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (18, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (11, 8) (16, 8) (8, 8) (9, 5) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (18, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`right` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (18, 8) are: ['up', 'left', 'up left']
The successors of the (18, 8) are ['up', 'left', 'up left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (18, 8) with action `up` toward ---> (18, 7)
cost from (18, 8) to --> (18, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298

Node <(18, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (18, 8) with action `left` toward ---> (17, 8)
cost from (18, 8) to --> (17, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0

Node <(17, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 8)>, Node <(18, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (18, 8) with action `up left` toward ---> (17, 7)
cost from (18, 8) to --> (17, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199

Node <(17, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 7)>, Node <(17, 8)>, Node <(18, 7)>}]


||From utils.pop() method: we pop() Node <(7, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(7, 8)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (18, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (11, 8) (16, 8) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (7, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (7, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (7, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (7, 8) with action `up` toward ---> (7, 7)
cost from (7, 8) to --> (7, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (7, 8) with action `left` toward ---> (6, 8)
cost from (7, 8) to --> (6, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0

Node <(6, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 7)>, Node <(6, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (7, 8) with action `right` toward ---> (8, 8)
cost from (7, 8) to --> (8, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 8) is = 23.0

Node <(8, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 7)>, Node <(8, 8)>, Node <(6, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (7, 8) with action `up left` toward ---> (6, 7)
cost from (7, 8) to --> (6, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 7)>, Node <(7, 7)>, Node <(8, 8)>, Node <(6, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (7, 8) with action `up right` toward ---> (8, 7)
cost from (7, 8) to --> (8, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 7) is = 23.021728866442675

Node <(8, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 7)>, Node <(6, 7)>, Node <(7, 7)>, Node <(8, 8)>, Node <(6, 8)>}]


||From utils.pop() method: we pop() Node <(8, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(8, 4)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (11, 8) (16, 8) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (8, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
Generated actions to generate the successors of the (8, 4) are: ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']
The successors of the (8, 4) are ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (8, 4) with action `up` toward ---> (8, 3)
cost from (8, 4) to --> (8, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964

Node <(8, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (8, 4) with action `down` toward ---> (8, 5)
cost from (8, 4) to --> (8, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403

Node <(8, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 3)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (8, 4) with action `left` toward ---> (7, 4)
cost from (8, 4) to --> (7, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 4)>, Node <(8, 3)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (8, 4) with action `up left` toward ---> (7, 3)
cost from (8, 4) to --> (7, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525

Node <(7, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 4)>, Node <(8, 3)>, Node <(7, 3)>, Node <(8, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (8, 4) with action `up right` toward ---> (9, 3)
cost from (8, 4) to --> (9, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 3) is = 22.561028345356956


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 3) is = 22.561028345356956

Node <(9, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 3)>, Node <(8, 3)>, Node <(7, 3)>, Node <(8, 5)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (8, 4) with action `down left` toward ---> (7, 5)
cost from (8, 4) to --> (7, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 3)>, Node <(8, 3)>, Node <(7, 3)>, Node <(8, 5)>, Node <(7, 4)>, Node <(7, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (8, 4) with action `down right` toward ---> (9, 5)
cost from (8, 4) to --> (9, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 5) is = 22.20360331117452

Node <(9, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 3)>, Node <(8, 3)>, Node <(7, 3)>, Node <(8, 5)>, Node <(7, 4)>, Node <(7, 5)>, Node <(9, 5)>}]

||From utils.append() method: we push the Node <(8, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 8)> Node <(7, 4)> Node <(15, 7)> Node <(18, 7)> Node <(5, 6)> Node <(16, 7)> Node <(17, 7)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(5, 8)> Node <(8, 3)>

||From utils.append() method: we push the Node <(7, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 8)> Node <(7, 4)> Node <(15, 7)> Node <(18, 7)> Node <(5, 6)> Node <(16, 7)> Node <(17, 7)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(5, 8)> Node <(8, 3)> Node <(7, 3)>

||From utils.append() method: we push the Node <(9, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 8)> Node <(7, 4)> Node <(15, 7)> Node <(18, 7)> Node <(5, 6)> Node <(16, 7)> Node <(17, 7)> Node <(5, 4)> Node <(5, 5)> Node <(5, 7)> Node <(6, 4)> Node <(5, 8)> Node <(8, 3)> Node <(7, 3)> Node <(9, 3)>


||From utils.pop() method: we pop() Node <(6, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(6, 8)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (6, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (6, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (6, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (6, 8) with action `up` toward ---> (6, 7)
cost from (6, 8) to --> (6, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (6, 8) with action `left` toward ---> (5, 8)
cost from (6, 8) to --> (5, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 8) is = 26.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 8) is = 26.0

Node <(5, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 7)>, Node <(5, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (6, 8) with action `right` toward ---> (7, 8)
cost from (6, 8) to --> (7, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 8) is = 24.0

Node <(7, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 8)>, Node <(6, 7)>, Node <(5, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (6, 8) with action `up left` toward ---> (5, 7)
cost from (6, 8) to --> (5, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376

Node <(5, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 8)>, Node <(5, 7)>, Node <(6, 7)>, Node <(5, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (6, 8) with action `up right` toward ---> (7, 7)
cost from (6, 8) to --> (7, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 7) is = 24.020824298928627

Node <(7, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 8)>, Node <(5, 7)>, Node <(5, 8)>, Node <(6, 7)>, Node <(7, 7)>}]


||From utils.pop() method: we pop() Node <(7, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(7, 4)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (7, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (7, 4) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (7, 4) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (7, 4) with action `up` toward ---> (7, 3)
cost from (7, 4) to --> (7, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525

Node <(7, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (7, 4) with action `down` toward ---> (7, 5)
cost from (7, 4) to --> (7, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 5)>, Node <(7, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (7, 4) with action `left` toward ---> (6, 4)
cost from (7, 4) to --> (6, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(7, 5)>, Node <(7, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (7, 4) with action `right` toward ---> (8, 4)
cost from (7, 4) to --> (8, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504

Node <(8, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(7, 5)>, Node <(7, 3)>, Node <(8, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (7, 4) with action `up left` toward ---> (6, 3)
cost from (7, 4) to --> (6, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924

Node <(6, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 5)>, Node <(7, 3)>, Node <(8, 4)>, Node <(6, 3)>, Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (7, 4) with action `up right` toward ---> (8, 3)
cost from (7, 4) to --> (8, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964

Node <(8, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 5)>, Node <(7, 3)>, Node <(8, 4)>, Node <(6, 3)>, Node <(6, 4)>, Node <(8, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (7, 4) with action `down left` toward ---> (6, 5)
cost from (7, 4) to --> (6, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 5)>, Node <(7, 3)>, Node <(8, 4)>, Node <(6, 3)>, Node <(6, 5)>, Node <(6, 4)>, Node <(8, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (7, 4) with action `down right` toward ---> (8, 5)
cost from (7, 4) to --> (8, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 5) is = 23.194827009486403

Node <(8, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 5)>, Node <(7, 5)>, Node <(7, 3)>, Node <(8, 4)>, Node <(6, 3)>, Node <(6, 5)>, Node <(6, 4)>, Node <(8, 3)>}]

||From utils.append() method: we push the Node <(7, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 6)> Node <(18, 7)> Node <(15, 7)> Node <(5, 5)> Node <(6, 4)> Node <(16, 7)> Node <(17, 7)> Node <(5, 4)> Node <(5, 7)> Node <(9, 3)> Node <(5, 8)> Node <(8, 3)> Node <(7, 3)>

||From utils.append() method: we push the Node <(6, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 6)> Node <(18, 7)> Node <(15, 7)> Node <(5, 5)> Node <(6, 4)> Node <(16, 7)> Node <(17, 7)> Node <(5, 4)> Node <(5, 7)> Node <(9, 3)> Node <(5, 8)> Node <(8, 3)> Node <(7, 3)> Node <(6, 3)>


||From utils.pop() method: we pop() Node <(5, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(5, 6)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (5, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (5, 6) are: ['up', 'down', 'right', 'up right', 'down right']
The successors of the (5, 6) are ['up', 'down', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (5, 6) with action `up` toward ---> (5, 5)
cost from (5, 6) to --> (5, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048

Node <(5, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (5, 6) with action `down` toward ---> (5, 7)
cost from (5, 6) to --> (5, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376

Node <(5, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 7)>, Node <(5, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (5, 6) with action `right` toward ---> (6, 6)
cost from (5, 6) to --> (6, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 7)>, Node <(5, 5)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (5, 6) with action `up right` toward ---> (6, 5)
cost from (5, 6) to --> (6, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(5, 7)>, Node <(5, 5)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (5, 6) with action `down right` toward ---> (6, 7)
cost from (5, 6) to --> (6, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 5)>, Node <(6, 5)>, Node <(6, 7)>, Node <(6, 6)>, Node <(5, 7)>}]


||From utils.pop() method: we pop() Node <(15, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(15, 7)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (15, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
Generated actions to generate the successors of the (15, 7) are: ['up', 'down', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (15, 7) are ['up', 'down', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (15, 7) with action `up` toward ---> (15, 6)
cost from (15, 7) to --> (15, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971

Node <(15, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (15, 7) with action `down` toward ---> (15, 8)
cost from (15, 7) to --> (15, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0

Node <(15, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 8)>, Node <(15, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (15, 7) with action `right` toward ---> (16, 7)
cost from (15, 7) to --> (16, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908

Node <(16, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(15, 8)>, Node <(15, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (15, 7) with action `up left` toward ---> (14, 6)
cost from (15, 7) to --> (14, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369

Node <(14, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(14, 6)>, Node <(15, 8)>, Node <(15, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (15, 7) with action `up right` toward ---> (16, 6)
cost from (15, 7) to --> (16, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556

Node <(16, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(14, 6)>, Node <(16, 7)>, Node <(15, 6)>, Node <(15, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (15, 7) with action `down left` toward ---> (14, 8)
cost from (15, 7) to --> (14, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 8) is = 17.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 8) is = 17.0

Node <(14, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(14, 8)>, Node <(14, 6)>, Node <(16, 7)>, Node <(15, 6)>, Node <(15, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (15, 7) with action `down right` toward ---> (16, 8)
cost from (15, 7) to --> (16, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0

Node <(16, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 8)>, Node <(16, 6)>, Node <(14, 8)>, Node <(14, 6)>, Node <(16, 7)>, Node <(15, 6)>, Node <(15, 8)>}]

||From utils.append() method: we push the Node <(15, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 7)> Node <(18, 7)> Node <(17, 7)> Node <(5, 5)> Node <(6, 4)> Node <(8, 3)> Node <(7, 3)> Node <(5, 4)> Node <(5, 7)> Node <(9, 3)> Node <(5, 8)> Node <(6, 3)> Node <(15, 6)>

||From utils.append() method: we push the Node <(14, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 7)> Node <(18, 7)> Node <(17, 7)> Node <(5, 5)> Node <(6, 4)> Node <(8, 3)> Node <(7, 3)> Node <(5, 4)> Node <(5, 7)> Node <(9, 3)> Node <(5, 8)> Node <(6, 3)> Node <(15, 6)> Node <(14, 6)>

||From utils.append() method: we push the Node <(16, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 7)> Node <(18, 7)> Node <(17, 7)> Node <(5, 5)> Node <(6, 4)> Node <(8, 3)> Node <(16, 6)> Node <(5, 4)> Node <(5, 7)> Node <(9, 3)> Node <(5, 8)> Node <(6, 3)> Node <(15, 6)> Node <(14, 6)> Node <(7, 3)>


||From utils.pop() method: we pop() Node <(16, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(16, 7)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (16, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up right` hits the obstacle
Generated actions to generate the successors of the (16, 7) are: ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']
The successors of the (16, 7) are ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (16, 7) with action `up` toward ---> (16, 6)
cost from (16, 7) to --> (16, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556

Node <(16, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (16, 7) with action `down` toward ---> (16, 8)
cost from (16, 7) to --> (16, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0

Node <(16, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(16, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (16, 7) with action `left` toward ---> (15, 7)
cost from (16, 7) to --> (15, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814

Node <(15, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 7)>, Node <(16, 6)>, Node <(16, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (16, 7) with action `right` toward ---> (17, 7)
cost from (16, 7) to --> (17, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199

Node <(17, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 7)>, Node <(16, 6)>, Node <(17, 7)>, Node <(16, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (16, 7) with action `up left` toward ---> (15, 6)
cost from (16, 7) to --> (15, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971

Node <(15, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 8)>, Node <(15, 7)>, Node <(17, 7)>, Node <(16, 6)>, Node <(15, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (16, 7) with action `down left` toward ---> (15, 8)
cost from (16, 7) to --> (15, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 8) is = 16.0

Node <(15, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 8)>, Node <(15, 7)>, Node <(15, 8)>, Node <(17, 7)>, Node <(16, 6)>, Node <(15, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (16, 7) with action `down right` toward ---> (17, 8)
cost from (16, 7) to --> (17, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0

Node <(17, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 8)>, Node <(15, 7)>, Node <(15, 8)>, Node <(17, 7)>, Node <(16, 6)>, Node <(15, 6)>, Node <(17, 8)>}]


||From utils.pop() method: we pop() Node <(17, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(17, 7)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (17, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
Generated actions to generate the successors of the (17, 7) are: ['down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (17, 7) are ['down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (17, 7) with action `down` toward ---> (17, 8)
cost from (17, 7) to --> (17, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0

Node <(17, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (17, 7) with action `left` toward ---> (16, 7)
cost from (17, 7) to --> (16, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908

Node <(16, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 8)>, Node <(16, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (17, 7) with action `right` toward ---> (18, 7)
cost from (17, 7) to --> (18, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298

Node <(18, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 8)>, Node <(16, 7)>, Node <(18, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (17, 7) with action `up left` toward ---> (16, 6)
cost from (17, 7) to --> (16, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556

Node <(16, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(17, 8)>, Node <(16, 7)>, Node <(18, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (17, 7) with action `up right` toward ---> (18, 6)
cost from (17, 7) to --> (18, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905

Node <(18, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(18, 6)>, Node <(17, 8)>, Node <(18, 7)>, Node <(16, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (17, 7) with action `down left` toward ---> (16, 8)
cost from (17, 7) to --> (16, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 8) is = 15.0

Node <(16, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(18, 6)>, Node <(16, 8)>, Node <(17, 8)>, Node <(18, 7)>, Node <(16, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (17, 7) with action `down right` toward ---> (18, 8)
cost from (17, 7) to --> (18, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 8) is = 13.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 8) is = 13.0

Node <(18, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(18, 6)>, Node <(16, 8)>, Node <(17, 8)>, Node <(18, 7)>, Node <(16, 7)>, Node <(18, 8)>}]

||From utils.append() method: we push the Node <(18, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(18, 7)> Node <(6, 4)> Node <(16, 6)> Node <(5, 5)> Node <(9, 3)> Node <(8, 3)> Node <(18, 6)> Node <(5, 4)> Node <(5, 7)> Node <(14, 6)> Node <(5, 8)> Node <(6, 3)> Node <(15, 6)> Node <(7, 3)>


||From utils.pop() method: we pop() Node <(18, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(18, 7)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (18, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`up left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (18, 7) are: ['up', 'down', 'left', 'up right', 'down left']
The successors of the (18, 7) are ['up', 'down', 'left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (18, 7) with action `up` toward ---> (18, 6)
cost from (18, 7) to --> (18, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905

Node <(18, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (18, 7) with action `down` toward ---> (18, 8)
cost from (18, 7) to --> (18, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 8) is = 13.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 8) is = 13.0

Node <(18, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>, Node <(18, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (18, 7) with action `left` toward ---> (17, 7)
cost from (18, 7) to --> (17, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199

Node <(17, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>, Node <(17, 7)>, Node <(18, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (18, 7) with action `up right` toward ---> (19, 6)
cost from (18, 7) to --> (19, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439

Node <(19, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>, Node <(17, 7)>, Node <(18, 8)>, Node <(19, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (18, 7) with action `down left` toward ---> (17, 8)
cost from (18, 7) to --> (17, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 8) is = 14.0

Node <(17, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 7)>, Node <(18, 8)>, Node <(19, 6)>, Node <(18, 6)>, Node <(17, 8)>}]

||From utils.append() method: we push the Node <(19, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 4)> Node <(9, 3)> Node <(16, 6)> Node <(5, 5)> Node <(7, 3)> Node <(8, 3)> Node <(18, 6)> Node <(5, 4)> Node <(5, 7)> Node <(14, 6)> Node <(5, 8)> Node <(6, 3)> Node <(15, 6)> Node <(19, 6)>


||From utils.pop() method: we pop() Node <(6, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(6, 4)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (6, 4) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (6, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (6, 4) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (6, 4) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (6, 4) with action `up` toward ---> (6, 3)
cost from (6, 4) to --> (6, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924

Node <(6, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (6, 4) with action `down` toward ---> (6, 5)
cost from (6, 4) to --> (6, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(6, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (6, 4) with action `left` toward ---> (5, 4)
cost from (6, 4) to --> (5, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181

Node <(5, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(5, 4)>, Node <(6, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (6, 4) with action `right` toward ---> (7, 4)
cost from (6, 4) to --> (7, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 4)>, Node <(6, 5)>, Node <(5, 4)>, Node <(6, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (6, 4) with action `up left` toward ---> (5, 3)
cost from (6, 4) to --> (5, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453

Node <(5, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(5, 3)>, Node <(6, 3)>, Node <(5, 4)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (6, 4) with action `up right` toward ---> (7, 3)
cost from (6, 4) to --> (7, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525

Node <(7, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(5, 3)>, Node <(6, 3)>, Node <(7, 3)>, Node <(5, 4)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (6, 4) with action `down left` toward ---> (5, 5)
cost from (6, 4) to --> (5, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048

Node <(5, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(5, 3)>, Node <(6, 3)>, Node <(7, 3)>, Node <(5, 4)>, Node <(7, 4)>, Node <(5, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (6, 4) with action `down right` toward ---> (7, 5)
cost from (6, 4) to --> (7, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 5) is = 24.186773244895647

Node <(7, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(5, 3)>, Node <(6, 3)>, Node <(7, 3)>, Node <(5, 4)>, Node <(7, 5)>, Node <(7, 4)>, Node <(5, 5)>}]

||From utils.append() method: we push the Node <(6, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(9, 3)> Node <(5, 5)> Node <(16, 6)> Node <(5, 7)> Node <(7, 3)> Node <(8, 3)> Node <(18, 6)> Node <(5, 4)> Node <(19, 6)> Node <(14, 6)> Node <(5, 8)> Node <(15, 6)> Node <(6, 3)>

||From utils.append() method: we push the Node <(5, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(9, 3)> Node <(5, 5)> Node <(16, 6)> Node <(5, 7)> Node <(7, 3)> Node <(8, 3)> Node <(18, 6)> Node <(5, 4)> Node <(19, 6)> Node <(14, 6)> Node <(5, 8)> Node <(15, 6)> Node <(6, 3)> Node <(5, 3)>


||From utils.pop() method: we pop() Node <(9, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(9, 3)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (7, 6) (8, 6) (9, 7) (6, 4) (9, 3) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (9, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`right` hits the obstacle
`up left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (9, 3) are: ['left', 'up right', 'down left']
The successors of the (9, 3) are ['left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (9, 3) with action `left` toward ---> (8, 3)
cost from (9, 3) to --> (8, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964

Node <(8, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (9, 3) with action `up right` toward ---> (10, 2)
cost from (9, 3) to --> (10, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555

Node <(10, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 2)>, Node <(8, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (9, 3) with action `down left` toward ---> (8, 4)
cost from (9, 3) to --> (8, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504

Node <(8, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 4)>, Node <(10, 2)>, Node <(8, 3)>}]

||From utils.append() method: we push the Node <(10, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 5)> Node <(5, 7)> Node <(16, 6)> Node <(19, 6)> Node <(7, 3)> Node <(8, 3)> Node <(18, 6)> Node <(5, 4)> Node <(5, 3)> Node <(14, 6)> Node <(5, 8)> Node <(15, 6)> Node <(6, 3)> Node <(10, 2)>


||From utils.pop() method: we pop() Node <(5, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(5, 5)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (9, 3) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (5, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (5, 5) are: ['up', 'down', 'right', 'up right', 'down right']
The successors of the (5, 5) are ['up', 'down', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (5, 5) with action `up` toward ---> (5, 4)
cost from (5, 5) to --> (5, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181

Node <(5, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (5, 5) with action `down` toward ---> (5, 6)
cost from (5, 5) to --> (5, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597

Node <(5, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 6)>, Node <(5, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (5, 5) with action `right` toward ---> (6, 5)
cost from (5, 5) to --> (6, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 6)>, Node <(5, 4)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (5, 5) with action `up right` toward ---> (6, 4)
cost from (5, 5) to --> (6, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 6)>, Node <(6, 4)>, Node <(5, 4)>, Node <(6, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (5, 5) with action `down right` toward ---> (6, 6)
cost from (5, 5) to --> (6, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 5)>, Node <(6, 6)>, Node <(6, 4)>, Node <(5, 4)>, Node <(5, 6)>}]


||From utils.pop() method: we pop() Node <(5, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(5, 7)>

CLOSED List in traditional has these nodes: (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (9, 3) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (5, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (5, 7) are: ['up', 'down', 'right', 'up right', 'down right']
The successors of the (5, 7) are ['up', 'down', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (5, 7) with action `up` toward ---> (5, 6)
cost from (5, 7) to --> (5, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 6) is = 26.076809620810597

Node <(5, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (5, 7) with action `down` toward ---> (5, 8)
cost from (5, 7) to --> (5, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 8) is = 26.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 8) is = 26.0

Node <(5, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 8)>, Node <(5, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (5, 7) with action `right` toward ---> (6, 7)
cost from (5, 7) to --> (6, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 8)>, Node <(6, 7)>, Node <(5, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (5, 7) with action `up right` toward ---> (6, 6)
cost from (5, 7) to --> (6, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 6) is = 25.079872407968907

Node <(6, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 8)>, Node <(6, 7)>, Node <(5, 6)>, Node <(6, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (5, 7) with action `down right` toward ---> (6, 8)
cost from (5, 7) to --> (6, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0

Node <(6, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 8)>, Node <(5, 6)>, Node <(6, 7)>, Node <(5, 8)>, Node <(6, 6)>}]


||From utils.pop() method: we pop() Node <(16, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(16, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (9, 3) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (16, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`right` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (16, 6) are: ['down', 'left', 'down left', 'down right']
The successors of the (16, 6) are ['down', 'left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (16, 6) with action `down` toward ---> (16, 7)
cost from (16, 6) to --> (16, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908

Node <(16, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (16, 6) with action `left` toward ---> (15, 6)
cost from (16, 6) to --> (15, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971

Node <(15, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(15, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (16, 6) with action `down left` toward ---> (15, 7)
cost from (16, 6) to --> (15, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814

Node <(15, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(15, 6)>, Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (16, 6) with action `down right` toward ---> (17, 7)
cost from (16, 6) to --> (17, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199

Node <(17, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 7)>, Node <(17, 7)>, Node <(15, 6)>, Node <(15, 7)>}]


||From utils.pop() method: we pop() Node <(8, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(8, 3)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (9, 3) (7, 5) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (8, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (8, 3) are: ['down', 'left', 'right', 'down left']
The successors of the (8, 3) are ['down', 'left', 'right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (8, 3) with action `down` toward ---> (8, 4)
cost from (8, 3) to --> (8, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504

Node <(8, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (8, 3) with action `left` toward ---> (7, 3)
cost from (8, 3) to --> (7, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525

Node <(7, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 4)>, Node <(7, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (8, 3) with action `right` toward ---> (9, 3)
cost from (8, 3) to --> (9, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 3) is = 22.561028345356956


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 3) is = 22.561028345356956

Node <(9, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 3)>, Node <(8, 4)>, Node <(7, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (8, 3) with action `down left` toward ---> (7, 4)
cost from (8, 3) to --> (7, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 3)>, Node <(8, 4)>, Node <(7, 3)>, Node <(7, 4)>}]


||From utils.pop() method: we pop() Node <(18, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(18, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (18, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (18, 6) are: ['up', 'down', 'right', 'up right', 'down left']
The successors of the (18, 6) are ['up', 'down', 'right', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (18, 6) with action `up` toward ---> (18, 5)
cost from (18, 6) to --> (18, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 5) is = 13.341664064126334


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 5) is = 13.341664064126334

Node <(18, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (18, 6) with action `down` toward ---> (18, 7)
cost from (18, 6) to --> (18, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298

Node <(18, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 5)>, Node <(18, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (18, 6) with action `right` toward ---> (19, 6)
cost from (18, 6) to --> (19, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439

Node <(19, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 5)>, Node <(19, 6)>, Node <(18, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (18, 6) with action `up right` toward ---> (19, 5)
cost from (18, 6) to --> (19, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298

Node <(19, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 5)>, Node <(19, 6)>, Node <(19, 5)>, Node <(18, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (18, 6) with action `down left` toward ---> (17, 7)
cost from (18, 6) to --> (17, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 7) is = 14.035668847618199

Node <(17, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 7)>, Node <(18, 5)>, Node <(17, 7)>, Node <(19, 6)>, Node <(19, 5)>}]

||From utils.append() method: we push the Node <(18, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(19, 6)> Node <(7, 3)> Node <(15, 6)> Node <(10, 2)> Node <(18, 5)> Node <(5, 8)> Node <(6, 3)> Node <(5, 4)> Node <(5, 3)> Node <(14, 6)>

||From utils.append() method: we push the Node <(19, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(19, 6)> Node <(7, 3)> Node <(15, 6)> Node <(10, 2)> Node <(19, 5)> Node <(5, 8)> Node <(6, 3)> Node <(5, 4)> Node <(5, 3)> Node <(14, 6)> Node <(18, 5)>


||From utils.pop() method: we pop() Node <(19, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(19, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (8, 8) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (19, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
Generated actions to generate the successors of the (19, 6) are: ['up', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (19, 6) are ['up', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (19, 6) with action `up` toward ---> (19, 5)
cost from (19, 6) to --> (19, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298

Node <(19, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (19, 6) with action `left` toward ---> (18, 6)
cost from (19, 6) to --> (18, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905

Node <(18, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>, Node <(19, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (19, 6) with action `right` toward ---> (20, 6)
cost from (19, 6) to --> (20, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949

Node <(20, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(18, 6)>, Node <(19, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (19, 6) with action `up left` toward ---> (18, 5)
cost from (19, 6) to --> (18, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 5) is = 13.341664064126334


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 5) is = 13.341664064126334

Node <(18, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(18, 6)>, Node <(19, 5)>, Node <(18, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (19, 6) with action `up right` toward ---> (20, 5)
cost from (19, 6) to --> (20, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 5) is = 11.40175425099138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 5) is = 11.40175425099138

Node <(20, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(18, 6)>, Node <(18, 5)>, Node <(19, 5)>, Node <(20, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (19, 6) with action `down left` toward ---> (18, 7)
cost from (19, 6) to --> (18, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 7) is = 13.038404810405298

Node <(18, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(18, 6)>, Node <(18, 5)>, Node <(18, 7)>, Node <(19, 5)>, Node <(20, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (19, 6) with action `down right` toward ---> (20, 7)
cost from (19, 6) to --> (20, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261

Node <(20, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(18, 6)>, Node <(18, 5)>, Node <(18, 7)>, Node <(20, 7)>, Node <(19, 5)>, Node <(20, 5)>}]

||From utils.append() method: we push the Node <(20, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(20, 6)> Node <(7, 3)> Node <(15, 6)> Node <(5, 4)> Node <(10, 2)> Node <(5, 8)> Node <(6, 3)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)>

||From utils.append() method: we push the Node <(20, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(20, 6)> Node <(7, 3)> Node <(15, 6)> Node <(5, 4)> Node <(10, 2)> Node <(5, 8)> Node <(6, 3)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)> Node <(20, 5)>

||From utils.append() method: we push the Node <(20, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(20, 6)> Node <(7, 3)> Node <(15, 6)> Node <(5, 4)> Node <(10, 2)> Node <(20, 7)> Node <(6, 3)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)> Node <(20, 5)> Node <(5, 8)>


||From utils.pop() method: we pop() Node <(20, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(20, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (8, 8) (20, 6) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (20, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (20, 6) are: ['up', 'down', 'left', 'up left', 'down right']
The successors of the (20, 6) are ['up', 'down', 'left', 'up left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (20, 6) with action `up` toward ---> (20, 5)
cost from (20, 6) to --> (20, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 5) is = 11.40175425099138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 5) is = 11.40175425099138

Node <(20, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (20, 6) with action `down` toward ---> (20, 7)
cost from (20, 6) to --> (20, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261

Node <(20, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 7)>, Node <(20, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (20, 6) with action `left` toward ---> (19, 6)
cost from (20, 6) to --> (19, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439

Node <(19, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 7)>, Node <(20, 5)>, Node <(19, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (20, 6) with action `up left` toward ---> (19, 5)
cost from (20, 6) to --> (19, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298

Node <(19, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 5)>, Node <(20, 7)>, Node <(20, 5)>, Node <(19, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (20, 6) with action `down right` toward ---> (21, 7)
cost from (20, 6) to --> (21, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089

Node <(21, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 7)>, Node <(19, 6)>, Node <(19, 5)>, Node <(21, 7)>, Node <(20, 5)>}]

||From utils.append() method: we push the Node <(21, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(7, 3)> Node <(10, 2)> Node <(15, 6)> Node <(5, 4)> Node <(5, 8)> Node <(20, 7)> Node <(6, 3)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)> Node <(20, 5)> Node <(21, 7)>


||From utils.pop() method: we pop() Node <(7, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(7, 3)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (8, 8) (20, 6) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (7, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (7, 3) are: ['down', 'left', 'right', 'down left', 'down right']
The successors of the (7, 3) are ['down', 'left', 'right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (7, 3) with action `down` toward ---> (7, 4)
cost from (7, 3) to --> (7, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (7, 3) with action `left` toward ---> (6, 3)
cost from (7, 3) to --> (6, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924

Node <(6, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 3)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (7, 3) with action `right` toward ---> (8, 3)
cost from (7, 3) to --> (8, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 3) is = 23.53720459187964

Node <(8, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 3)>, Node <(6, 3)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (7, 3) with action `down left` toward ---> (6, 4)
cost from (7, 3) to --> (6, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(8, 3)>, Node <(6, 3)>, Node <(7, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (7, 3) with action `down right` toward ---> (8, 4)
cost from (7, 3) to --> (8, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 4) is = 23.345235059857504

Node <(8, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 4)>, Node <(6, 3)>, Node <(6, 4)>, Node <(8, 4)>, Node <(8, 3)>}]


||From utils.pop() method: we pop() Node <(15, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(15, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (15, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (15, 6) are: ['down', 'left', 'right', 'up left', 'down right']
The successors of the (15, 6) are ['down', 'left', 'right', 'up left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (15, 6) with action `down` toward ---> (15, 7)
cost from (15, 6) to --> (15, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814

Node <(15, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (15, 6) with action `left` toward ---> (14, 6)
cost from (15, 6) to --> (14, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369

Node <(14, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 6)>, Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (15, 6) with action `right` toward ---> (16, 6)
cost from (15, 6) to --> (16, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 6) is = 15.132745950421556

Node <(16, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 6)>, Node <(16, 6)>, Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (15, 6) with action `up left` toward ---> (14, 5)
cost from (15, 6) to --> (14, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207

Node <(14, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 5)>, Node <(14, 6)>, Node <(16, 6)>, Node <(15, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (15, 6) with action `down right` toward ---> (16, 7)
cost from (15, 6) to --> (16, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 7) is = 15.033296378372908

Node <(16, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 6)>, Node <(14, 5)>, Node <(15, 7)>, Node <(16, 7)>, Node <(14, 6)>}]

||From utils.append() method: we push the Node <(14, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(6, 3)> Node <(10, 2)> Node <(20, 7)> Node <(5, 4)> Node <(5, 8)> Node <(20, 5)> Node <(21, 7)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)> Node <(14, 5)>


||From utils.pop() method: we pop() Node <(6, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(6, 3)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (6, 3) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (6, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (6, 3) are: ['down', 'left', 'right', 'up left', 'down left', 'down right']
The successors of the (6, 3) are ['down', 'left', 'right', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (6, 3) with action `down` toward ---> (6, 4)
cost from (6, 3) to --> (6, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (6, 3) with action `left` toward ---> (5, 3)
cost from (6, 3) to --> (5, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453

Node <(5, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>, Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (6, 3) with action `right` toward ---> (7, 3)
cost from (6, 3) to --> (7, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 3) is = 24.515301344262525

Node <(7, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 3)>, Node <(5, 3)>, Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (6, 3) with action `up left` toward ---> (5, 2)
cost from (6, 3) to --> (5, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 2) is = 26.68332812825267


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 2) is = 26.68332812825267

Node <(5, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(7, 3)>, Node <(5, 2)>, Node <(5, 3)>, Node <(6, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (6, 3) with action `down left` toward ---> (5, 4)
cost from (6, 3) to --> (5, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181

Node <(5, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 4)>, Node <(5, 2)>, Node <(6, 4)>, Node <(7, 3)>, Node <(5, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (6, 3) with action `down right` toward ---> (7, 4)
cost from (6, 3) to --> (7, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (7, 4) is = 24.331050121192877

Node <(7, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 4)>, Node <(5, 2)>, Node <(6, 4)>, Node <(7, 3)>, Node <(7, 4)>, Node <(5, 3)>}]

||From utils.append() method: we push the Node <(5, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(20, 7)> Node <(10, 2)> Node <(21, 7)> Node <(5, 4)> Node <(5, 8)> Node <(20, 5)> Node <(14, 5)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)> Node <(5, 2)>


||From utils.pop() method: we pop() Node <(20, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(20, 7)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (6, 3) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (20, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (20, 7) are: ['up', 'down', 'right', 'up left', 'down right']
The successors of the (20, 7) are ['up', 'down', 'right', 'up left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (20, 7) with action `up` toward ---> (20, 6)
cost from (20, 7) to --> (20, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949

Node <(20, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (20, 7) with action `down` toward ---> (20, 8)
cost from (20, 7) to --> (20, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 8) is = 11.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 8) is = 11.0

Node <(20, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(20, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (20, 7) with action `right` toward ---> (21, 7)
cost from (20, 7) to --> (21, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089

Node <(21, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(20, 8)>, Node <(21, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (20, 7) with action `up left` toward ---> (19, 6)
cost from (20, 7) to --> (19, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439

Node <(19, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(20, 8)>, Node <(21, 7)>, Node <(19, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (20, 7) with action `down right` toward ---> (21, 8)
cost from (20, 7) to --> (21, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0

Node <(21, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>, Node <(19, 6)>, Node <(20, 8)>, Node <(21, 7)>, Node <(21, 8)>}]

||From utils.append() method: we push the Node <(20, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(21, 7)> Node <(10, 2)> Node <(20, 5)> Node <(5, 4)> Node <(5, 8)> Node <(20, 8)> Node <(14, 5)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)> Node <(5, 2)>

||From utils.append() method: we push the Node <(21, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(21, 7)> Node <(10, 2)> Node <(20, 5)> Node <(5, 4)> Node <(5, 8)> Node <(21, 8)> Node <(14, 5)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(19, 5)> Node <(5, 2)> Node <(20, 8)>


||From utils.pop() method: we pop() Node <(21, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(21, 7)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (6, 3) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (21, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
Generated actions to generate the successors of the (21, 7) are: ['down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (21, 7) are ['down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (21, 7) with action `down` toward ---> (21, 8)
cost from (21, 7) to --> (21, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0

Node <(21, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (21, 7) with action `left` toward ---> (20, 7)
cost from (21, 7) to --> (20, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261

Node <(20, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 7)>, Node <(21, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (21, 7) with action `right` toward ---> (22, 7)
cost from (21, 7) to --> (22, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417

Node <(22, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>, Node <(20, 7)>, Node <(21, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (21, 7) with action `up left` toward ---> (20, 6)
cost from (21, 7) to --> (20, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949

Node <(20, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>, Node <(20, 7)>, Node <(21, 8)>, Node <(20, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (21, 7) with action `up right` toward ---> (22, 6)
cost from (21, 7) to --> (22, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887

Node <(22, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 6)>, Node <(22, 7)>, Node <(21, 8)>, Node <(20, 7)>, Node <(20, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (21, 7) with action `down left` toward ---> (20, 8)
cost from (21, 7) to --> (20, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 8) is = 11.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 8) is = 11.0

Node <(20, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 6)>, Node <(22, 7)>, Node <(21, 8)>, Node <(20, 7)>, Node <(20, 8)>, Node <(20, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (21, 7) with action `down right` toward ---> (22, 8)
cost from (21, 7) to --> (22, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0

Node <(22, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 6)>, Node <(22, 7)>, Node <(21, 8)>, Node <(22, 8)>, Node <(20, 7)>, Node <(20, 8)>, Node <(20, 6)>}]

||From utils.append() method: we push the Node <(22, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 7)> Node <(5, 8)> Node <(10, 2)> Node <(5, 4)> Node <(19, 5)> Node <(20, 5)> Node <(14, 5)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(21, 8)>

||From utils.append() method: we push the Node <(22, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 7)> Node <(5, 8)> Node <(10, 2)> Node <(5, 4)> Node <(19, 5)> Node <(20, 5)> Node <(22, 6)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(21, 8)> Node <(14, 5)>

||From utils.append() method: we push the Node <(22, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 7)> Node <(5, 8)> Node <(10, 2)> Node <(5, 4)> Node <(19, 5)> Node <(20, 5)> Node <(22, 8)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(21, 8)> Node <(14, 5)> Node <(22, 6)>


||From utils.pop() method: we pop() Node <(22, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(22, 7)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (22, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up left` hits the obstacle
Generated actions to generate the successors of the (22, 7) are: ['up', 'down', 'left', 'right', 'up right', 'down left', 'down right']
The successors of the (22, 7) are ['up', 'down', 'left', 'right', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (22, 7) with action `up` toward ---> (22, 6)
cost from (22, 7) to --> (22, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887

Node <(22, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (22, 7) with action `down` toward ---> (22, 8)
cost from (22, 7) to --> (22, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0

Node <(22, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 8)>, Node <(22, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (22, 7) with action `left` toward ---> (21, 7)
cost from (22, 7) to --> (21, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089

Node <(21, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 8)>, Node <(21, 7)>, Node <(22, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (22, 7) with action `right` toward ---> (23, 7)
cost from (22, 7) to --> (23, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855

Node <(23, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 8)>, Node <(21, 7)>, Node <(22, 6)>, Node <(23, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (22, 7) with action `up right` toward ---> (23, 6)
cost from (22, 7) to --> (23, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321

Node <(23, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(22, 8)>, Node <(23, 6)>, Node <(23, 7)>, Node <(22, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (22, 7) with action `down left` toward ---> (21, 8)
cost from (22, 7) to --> (21, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0

Node <(21, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(21, 8)>, Node <(22, 8)>, Node <(23, 6)>, Node <(23, 7)>, Node <(22, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (22, 7) with action `down right` toward ---> (23, 8)
cost from (22, 7) to --> (23, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0

Node <(23, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(21, 8)>, Node <(22, 8)>, Node <(23, 6)>, Node <(23, 7)>, Node <(22, 6)>, Node <(23, 8)>}]

||From utils.append() method: we push the Node <(23, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 7)> Node <(5, 8)> Node <(10, 2)> Node <(5, 4)> Node <(19, 5)> Node <(21, 8)> Node <(20, 5)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(22, 8)>

||From utils.append() method: we push the Node <(23, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 7)> Node <(5, 8)> Node <(10, 2)> Node <(5, 4)> Node <(19, 5)> Node <(21, 8)> Node <(20, 5)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(22, 8)> Node <(23, 6)>

||From utils.append() method: we push the Node <(23, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 7)> Node <(5, 8)> Node <(10, 2)> Node <(5, 4)> Node <(19, 5)> Node <(21, 8)> Node <(20, 5)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(22, 8)> Node <(23, 6)> Node <(23, 8)>


||From utils.pop() method: we pop() Node <(23, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(23, 7)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (23, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (23, 7) are: ['up', 'down', 'left', 'up left', 'down left', 'down right']
The successors of the (23, 7) are ['up', 'down', 'left', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (23, 7) with action `up` toward ---> (23, 6)
cost from (23, 7) to --> (23, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321

Node <(23, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (23, 7) with action `down` toward ---> (23, 8)
cost from (23, 7) to --> (23, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0

Node <(23, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 8)>, Node <(23, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (23, 7) with action `left` toward ---> (22, 7)
cost from (23, 7) to --> (22, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417

Node <(22, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>, Node <(23, 8)>, Node <(23, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (23, 7) with action `up left` toward ---> (22, 6)
cost from (23, 7) to --> (22, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887

Node <(22, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>, Node <(22, 6)>, Node <(23, 8)>, Node <(23, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (23, 7) with action `down left` toward ---> (22, 8)
cost from (23, 7) to --> (22, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0

Node <(22, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>, Node <(23, 6)>, Node <(22, 6)>, Node <(23, 8)>, Node <(22, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (23, 7) with action `down right` toward ---> (24, 8)
cost from (23, 7) to --> (24, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0

Node <(24, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>, Node <(23, 6)>, Node <(22, 6)>, Node <(24, 8)>, Node <(23, 8)>, Node <(22, 8)>}]

||From utils.append() method: we push the Node <(24, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(10, 2)> Node <(5, 8)> Node <(20, 5)> Node <(5, 4)> Node <(19, 5)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(24, 8)>


||From utils.pop() method: we pop() Node <(10, 2)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(10, 2)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (10, 2)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`left` hits the obstacle
Generated actions to generate the successors of the (10, 2) are: ['up', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (10, 2) are ['up', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (10, 2) with action `up` toward ---> (10, 1)
cost from (10, 2) to --> (10, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654

Node <(10, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (10, 2) with action `right` toward ---> (11, 2)
cost from (10, 2) to --> (11, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211

Node <(11, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 1)>, Node <(11, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (10, 2) with action `up left` toward ---> (9, 1)
cost from (10, 2) to --> (9, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 1) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 1) is = 23.08679276123039

Node <(9, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(9, 1)>, Node <(10, 1)>, Node <(11, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (10, 2) with action `up right` toward ---> (11, 1)
cost from (10, 2) to --> (11, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709

Node <(11, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(9, 1)>, Node <(10, 1)>, Node <(11, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (10, 2) with action `down left` toward ---> (9, 3)
cost from (10, 2) to --> (9, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 3) is = 22.561028345356956


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 3) is = 22.561028345356956

Node <(9, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(9, 3)>, Node <(9, 1)>, Node <(11, 2)>, Node <(10, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (10, 2) with action `down right` toward ---> (11, 3)
cost from (10, 2) to --> (11, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304

Node <(11, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(11, 3)>, Node <(9, 3)>, Node <(9, 1)>, Node <(11, 2)>, Node <(10, 1)>}]

||From utils.append() method: we push the Node <(10, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 8)> Node <(19, 5)> Node <(20, 5)> Node <(5, 4)> Node <(24, 8)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(5, 3)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)>

||From utils.append() method: we push the Node <(11, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(11, 2)> Node <(5, 8)> Node <(20, 5)> Node <(19, 5)> Node <(24, 8)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(5, 4)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)> Node <(5, 3)>

||From utils.append() method: we push the Node <(9, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(11, 2)> Node <(5, 8)> Node <(20, 5)> Node <(19, 5)> Node <(24, 8)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(5, 4)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)>

||From utils.append() method: we push the Node <(11, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(11, 2)> Node <(5, 8)> Node <(20, 5)> Node <(19, 5)> Node <(24, 8)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(5, 4)> Node <(11, 1)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)>

||From utils.append() method: we push the Node <(11, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(11, 2)> Node <(5, 8)> Node <(20, 5)> Node <(19, 5)> Node <(11, 3)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(5, 4)> Node <(24, 8)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(11, 1)>


||From utils.pop() method: we pop() Node <(11, 2)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(11, 2)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (10, 8) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (11, 2)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down left` hits the obstacle
Generated actions to generate the successors of the (11, 2) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down right']
The successors of the (11, 2) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (11, 2) with action `up` toward ---> (11, 1)
cost from (11, 2) to --> (11, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709

Node <(11, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (11, 2) with action `down` toward ---> (11, 3)
cost from (11, 2) to --> (11, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304

Node <(11, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(11, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (11, 2) with action `left` toward ---> (10, 2)
cost from (11, 2) to --> (10, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555

Node <(10, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(10, 2)>, Node <(11, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (11, 2) with action `right` toward ---> (12, 2)
cost from (11, 2) to --> (12, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(10, 2)>, Node <(12, 2)>, Node <(11, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (11, 2) with action `up left` toward ---> (10, 1)
cost from (11, 2) to --> (10, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654

Node <(10, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 2)>, Node <(11, 1)>, Node <(10, 2)>, Node <(10, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (11, 2) with action `up right` toward ---> (12, 1)
cost from (11, 2) to --> (12, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587

Node <(12, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 2)>, Node <(12, 1)>, Node <(11, 1)>, Node <(10, 2)>, Node <(10, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (11, 2) with action `down right` toward ---> (12, 3)
cost from (11, 2) to --> (12, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885

Node <(12, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 2)>, Node <(12, 1)>, Node <(11, 1)>, Node <(10, 2)>, Node <(12, 3)>, Node <(10, 1)>}]

||From utils.append() method: we push the Node <(12, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 8)> Node <(12, 2)> Node <(20, 5)> Node <(5, 4)> Node <(19, 5)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(11, 1)> Node <(11, 3)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(24, 8)>

||From utils.append() method: we push the Node <(12, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 8)> Node <(12, 2)> Node <(20, 5)> Node <(5, 4)> Node <(19, 5)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(11, 1)> Node <(11, 3)> Node <(20, 8)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(24, 8)> Node <(12, 1)>

||From utils.append() method: we push the Node <(12, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 8)> Node <(12, 2)> Node <(20, 5)> Node <(5, 4)> Node <(19, 5)> Node <(21, 8)> Node <(22, 8)> Node <(18, 5)> Node <(11, 1)> Node <(11, 3)> Node <(12, 3)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(23, 6)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(24, 8)> Node <(12, 1)> Node <(20, 8)>


||From utils.pop() method: we pop() Node <(5, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(5, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (5, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (5, 8) are: ['up', 'right', 'up right']
The successors of the (5, 8) are ['up', 'right', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (5, 8) with action `up` toward ---> (5, 7)
cost from (5, 8) to --> (5, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 7) is = 26.019223662515376

Node <(5, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (5, 8) with action `right` toward ---> (6, 8)
cost from (5, 8) to --> (6, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 8) is = 25.0

Node <(6, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 8)>, Node <(5, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (5, 8) with action `up right` toward ---> (6, 7)
cost from (5, 8) to --> (6, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 7) is = 25.019992006393608

Node <(6, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 8)>, Node <(5, 7)>, Node <(6, 7)>}]


||From utils.pop() method: we pop() Node <(12, 2)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(12, 2)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (12, 2)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (12, 2) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (12, 2) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (12, 2) with action `up` toward ---> (12, 1)
cost from (12, 2) to --> (12, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587

Node <(12, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (12, 2) with action `down` toward ---> (12, 3)
cost from (12, 2) to --> (12, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885

Node <(12, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (12, 2) with action `left` toward ---> (11, 2)
cost from (12, 2) to --> (11, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211

Node <(11, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(11, 2)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (12, 2) with action `right` toward ---> (13, 2)
cost from (12, 2) to --> (13, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276

Node <(13, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(11, 2)>, Node <(13, 2)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (12, 2) with action `up left` toward ---> (11, 1)
cost from (12, 2) to --> (11, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709

Node <(11, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(11, 1)>, Node <(11, 2)>, Node <(13, 2)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (12, 2) with action `up right` toward ---> (13, 1)
cost from (12, 2) to --> (13, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 1) is = 19.313207915827967


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 1) is = 19.313207915827967

Node <(13, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(11, 1)>, Node <(13, 1)>, Node <(11, 2)>, Node <(13, 2)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (12, 2) with action `down left` toward ---> (11, 3)
cost from (12, 2) to --> (11, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304

Node <(11, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 3)>, Node <(11, 1)>, Node <(13, 1)>, Node <(11, 2)>, Node <(13, 2)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (12, 2) with action `down right` toward ---> (13, 3)
cost from (12, 2) to --> (13, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406

Node <(13, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 3)>, Node <(11, 1)>, Node <(13, 1)>, Node <(13, 3)>, Node <(11, 2)>, Node <(13, 2)>, Node <(12, 1)>}]

||From utils.append() method: we push the Node <(13, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(13, 2)> Node <(19, 5)> Node <(20, 5)> Node <(18, 5)> Node <(5, 4)> Node <(21, 8)> Node <(22, 8)> Node <(23, 6)> Node <(11, 1)> Node <(24, 8)> Node <(11, 3)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(12, 1)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(20, 8)> Node <(12, 3)>

||From utils.append() method: we push the Node <(13, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(13, 2)> Node <(19, 5)> Node <(20, 5)> Node <(18, 5)> Node <(5, 4)> Node <(21, 8)> Node <(22, 8)> Node <(23, 6)> Node <(11, 1)> Node <(24, 8)> Node <(11, 3)> Node <(5, 2)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(12, 1)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(20, 8)> Node <(12, 3)> Node <(13, 1)>

||From utils.append() method: we push the Node <(13, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(13, 2)> Node <(19, 5)> Node <(20, 5)> Node <(18, 5)> Node <(5, 4)> Node <(13, 3)> Node <(22, 8)> Node <(23, 6)> Node <(11, 1)> Node <(24, 8)> Node <(11, 3)> Node <(21, 8)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(12, 1)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(20, 8)> Node <(12, 3)> Node <(13, 1)> Node <(5, 2)>


||From utils.pop() method: we pop() Node <(13, 2)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(13, 2)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (13, 2)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (13, 2) are: ['up', 'down', 'left', 'up left', 'down left', 'down right']
The successors of the (13, 2) are ['up', 'down', 'left', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (13, 2) with action `up` toward ---> (13, 1)
cost from (13, 2) to --> (13, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 1) is = 19.313207915827967


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 1) is = 19.313207915827967

Node <(13, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (13, 2) with action `down` toward ---> (13, 3)
cost from (13, 2) to --> (13, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406

Node <(13, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(13, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (13, 2) with action `left` toward ---> (12, 2)
cost from (13, 2) to --> (12, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 2)>, Node <(13, 3)>, Node <(13, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (13, 2) with action `up left` toward ---> (12, 1)
cost from (13, 2) to --> (12, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587

Node <(12, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 2)>, Node <(13, 3)>, Node <(12, 1)>, Node <(13, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (13, 2) with action `down left` toward ---> (12, 3)
cost from (13, 2) to --> (12, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885

Node <(12, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(12, 3)>, Node <(12, 2)>, Node <(13, 1)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (13, 2) with action `down right` toward ---> (14, 3)
cost from (13, 2) to --> (14, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935

Node <(14, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(12, 3)>, Node <(12, 2)>, Node <(13, 1)>, Node <(12, 1)>, Node <(14, 3)>}]

||From utils.append() method: we push the Node <(14, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(19, 5)> Node <(5, 4)> Node <(20, 5)> Node <(18, 5)> Node <(11, 3)> Node <(13, 3)> Node <(22, 8)> Node <(23, 6)> Node <(11, 1)> Node <(24, 8)> Node <(12, 3)> Node <(21, 8)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(12, 1)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(20, 8)> Node <(5, 2)> Node <(13, 1)> Node <(14, 3)>


||From utils.pop() method: we pop() Node <(19, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(19, 5)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (19, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (19, 5) are: ['down', 'left', 'right', 'down left', 'down right']
The successors of the (19, 5) are ['down', 'left', 'right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (19, 5) with action `down` toward ---> (19, 6)
cost from (19, 5) to --> (19, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439

Node <(19, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (19, 5) with action `left` toward ---> (18, 5)
cost from (19, 5) to --> (18, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 5) is = 13.341664064126334


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 5) is = 13.341664064126334

Node <(18, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 6)>, Node <(18, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (19, 5) with action `right` toward ---> (20, 5)
cost from (19, 5) to --> (20, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 5) is = 11.40175425099138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 5) is = 11.40175425099138

Node <(20, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 6)>, Node <(20, 5)>, Node <(18, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (19, 5) with action `down left` toward ---> (18, 6)
cost from (19, 5) to --> (18, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905

Node <(18, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 6)>, Node <(20, 5)>, Node <(18, 5)>, Node <(18, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (19, 5) with action `down right` toward ---> (20, 6)
cost from (19, 5) to --> (20, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949

Node <(20, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 6)>, Node <(20, 5)>, Node <(18, 6)>, Node <(20, 6)>, Node <(18, 5)>}]


||From utils.pop() method: we pop() Node <(20, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(20, 5)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (20, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`right` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (20, 5) are: ['down', 'left', 'down left']
The successors of the (20, 5) are ['down', 'left', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (20, 5) with action `down` toward ---> (20, 6)
cost from (20, 5) to --> (20, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 6) is = 11.180339887498949

Node <(20, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (20, 5) with action `left` toward ---> (19, 5)
cost from (20, 5) to --> (19, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298

Node <(19, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 5)>, Node <(20, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (20, 5) with action `down left` toward ---> (19, 6)
cost from (20, 5) to --> (19, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439

Node <(19, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 5)>, Node <(19, 6)>, Node <(20, 6)>}]


||From utils.pop() method: we pop() Node <(5, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(5, 4)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (5, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (5, 4) are: ['up', 'down', 'right', 'up right', 'down right']
The successors of the (5, 4) are ['up', 'down', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (5, 4) with action `up` toward ---> (5, 3)
cost from (5, 4) to --> (5, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453

Node <(5, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (5, 4) with action `down` toward ---> (5, 5)
cost from (5, 4) to --> (5, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 5) is = 26.1725046566048

Node <(5, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>, Node <(5, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (5, 4) with action `right` toward ---> (6, 4)
cost from (5, 4) to --> (6, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>, Node <(6, 4)>, Node <(5, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (5, 4) with action `up right` toward ---> (6, 3)
cost from (5, 4) to --> (6, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924

Node <(6, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>, Node <(6, 4)>, Node <(6, 3)>, Node <(5, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (5, 4) with action `down right` toward ---> (6, 5)
cost from (5, 4) to --> (6, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 5) is = 25.179356624028344

Node <(6, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(6, 4)>, Node <(5, 3)>, Node <(5, 5)>, Node <(6, 3)>, Node <(6, 5)>}]


||From utils.pop() method: we pop() Node <(11, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(11, 3)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (11, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (11, 3) are: ['up', 'right', 'up left', 'up right', 'down right']
The successors of the (11, 3) are ['up', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (11, 3) with action `up` toward ---> (11, 2)
cost from (11, 3) to --> (11, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211

Node <(11, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (11, 3) with action `right` toward ---> (12, 3)
cost from (11, 3) to --> (12, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885

Node <(12, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(11, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (11, 3) with action `up left` toward ---> (10, 2)
cost from (11, 3) to --> (10, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555

Node <(10, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(11, 2)>, Node <(10, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (11, 3) with action `up right` toward ---> (12, 2)
cost from (11, 3) to --> (12, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(12, 2)>, Node <(11, 2)>, Node <(10, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (11, 3) with action `down right` toward ---> (12, 4)
cost from (11, 3) to --> (12, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476

Node <(12, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 2)>, Node <(12, 4)>, Node <(11, 2)>, Node <(12, 3)>, Node <(10, 2)>}]

||From utils.append() method: we push the Node <(12, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(18, 5)> Node <(12, 3)> Node <(13, 3)> Node <(23, 6)> Node <(24, 8)> Node <(21, 8)> Node <(22, 8)> Node <(12, 1)> Node <(11, 1)> Node <(20, 8)> Node <(13, 1)> Node <(14, 3)> Node <(22, 6)> Node <(14, 5)> Node <(23, 8)> Node <(5, 2)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 6)> Node <(12, 4)>


||From utils.pop() method: we pop() Node <(18, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(18, 5)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (18, 5) (6, 3) (22, 7) (8, 6) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (18, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`left` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (18, 5) are: ['down', 'right', 'down right']
The successors of the (18, 5) are ['down', 'right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (18, 5) with action `down` toward ---> (18, 6)
cost from (18, 5) to --> (18, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 6) is = 13.152946437965905

Node <(18, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (18, 5) with action `right` toward ---> (19, 5)
cost from (18, 5) to --> (19, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 5) is = 12.36931687685298

Node <(19, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>, Node <(19, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (18, 5) with action `down right` toward ---> (19, 6)
cost from (18, 5) to --> (19, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 6) is = 12.165525060596439

Node <(19, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 6)>, Node <(19, 5)>, Node <(19, 6)>}]


||From utils.pop() method: we pop() Node <(12, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(12, 3)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (7, 6) (10, 2) (18, 5) (6, 3) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (12, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down left` hits the obstacle
Generated actions to generate the successors of the (12, 3) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down right']
The successors of the (12, 3) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (12, 3) with action `up` toward ---> (12, 2)
cost from (12, 3) to --> (12, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (12, 3) with action `down` toward ---> (12, 4)
cost from (12, 3) to --> (12, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476

Node <(12, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>, Node <(12, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (12, 3) with action `left` toward ---> (11, 3)
cost from (12, 3) to --> (11, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304

Node <(11, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>, Node <(11, 3)>, Node <(12, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (12, 3) with action `right` toward ---> (13, 3)
cost from (12, 3) to --> (13, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406

Node <(13, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(12, 4)>, Node <(11, 3)>, Node <(12, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (12, 3) with action `up left` toward ---> (11, 2)
cost from (12, 3) to --> (11, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211

Node <(11, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(11, 2)>, Node <(12, 4)>, Node <(12, 2)>, Node <(11, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (12, 3) with action `up right` toward ---> (13, 2)
cost from (12, 3) to --> (13, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276

Node <(13, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(11, 2)>, Node <(12, 4)>, Node <(12, 2)>, Node <(13, 2)>, Node <(11, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (12, 3) with action `down right` toward ---> (13, 4)
cost from (12, 3) to --> (13, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(13, 4)>, Node <(11, 2)>, Node <(12, 4)>, Node <(12, 2)>, Node <(13, 2)>, Node <(11, 3)>}]

||From utils.append() method: we push the Node <(13, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(13, 3)> Node <(24, 8)> Node <(22, 8)> Node <(23, 6)> Node <(20, 8)> Node <(21, 8)> Node <(23, 8)> Node <(12, 1)> Node <(11, 1)> Node <(12, 4)> Node <(13, 1)> Node <(14, 3)> Node <(22, 6)> Node <(14, 5)> Node <(14, 6)> Node <(5, 2)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(13, 4)>


||From utils.pop() method: we pop() Node <(13, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(13, 3)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (6, 3) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (13, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up right` hits the obstacle
Generated actions to generate the successors of the (13, 3) are: ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']
The successors of the (13, 3) are ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (13, 3) with action `up` toward ---> (13, 2)
cost from (13, 3) to --> (13, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276

Node <(13, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (13, 3) with action `down` toward ---> (13, 4)
cost from (13, 3) to --> (13, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 4)>, Node <(13, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (13, 3) with action `left` toward ---> (12, 3)
cost from (13, 3) to --> (12, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885

Node <(12, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 4)>, Node <(13, 2)>, Node <(12, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (13, 3) with action `right` toward ---> (14, 3)
cost from (13, 3) to --> (14, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935

Node <(14, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 4)>, Node <(13, 2)>, Node <(12, 3)>, Node <(14, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (13, 3) with action `up left` toward ---> (12, 2)
cost from (13, 3) to --> (12, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(12, 2)>, Node <(14, 3)>, Node <(13, 4)>, Node <(13, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (13, 3) with action `down left` toward ---> (12, 4)
cost from (13, 3) to --> (12, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476

Node <(12, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(12, 2)>, Node <(14, 3)>, Node <(13, 4)>, Node <(12, 4)>, Node <(13, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (13, 3) with action `down right` toward ---> (14, 4)
cost from (13, 3) to --> (14, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298

Node <(14, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(12, 2)>, Node <(14, 3)>, Node <(13, 4)>, Node <(12, 4)>, Node <(13, 2)>, Node <(14, 4)>}]

||From utils.append() method: we push the Node <(14, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 8)> Node <(24, 8)> Node <(23, 8)> Node <(23, 6)> Node <(20, 8)> Node <(21, 8)> Node <(13, 4)> Node <(12, 1)> Node <(11, 1)> Node <(12, 4)> Node <(13, 1)> Node <(14, 3)> Node <(22, 6)> Node <(14, 5)> Node <(14, 6)> Node <(5, 2)> Node <(10, 1)> Node <(5, 3)> Node <(9, 1)> Node <(14, 4)>


||From utils.pop() method: we pop() Node <(22, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(22, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (6, 3) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (22, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (22, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (22, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (22, 8) with action `up` toward ---> (22, 7)
cost from (22, 8) to --> (22, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417

Node <(22, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (22, 8) with action `left` toward ---> (21, 8)
cost from (22, 8) to --> (21, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0

Node <(21, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 8)>, Node <(22, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (22, 8) with action `right` toward ---> (23, 8)
cost from (22, 8) to --> (23, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0

Node <(23, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 8)>, Node <(22, 7)>, Node <(23, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (22, 8) with action `up left` toward ---> (21, 7)
cost from (22, 8) to --> (21, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089

Node <(21, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(21, 8)>, Node <(22, 7)>, Node <(23, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (22, 8) with action `up right` toward ---> (23, 7)
cost from (22, 8) to --> (23, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855

Node <(23, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(21, 8)>, Node <(22, 7)>, Node <(23, 7)>, Node <(23, 8)>}]


||From utils.pop() method: we pop() Node <(23, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(23, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (6, 3) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (23, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (23, 8) are: ['up', 'left', 'right', 'up left']
The successors of the (23, 8) are ['up', 'left', 'right', 'up left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (23, 8) with action `up` toward ---> (23, 7)
cost from (23, 8) to --> (23, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855

Node <(23, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (23, 8) with action `left` toward ---> (22, 8)
cost from (23, 8) to --> (22, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0

Node <(22, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 8)>, Node <(23, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (23, 8) with action `right` toward ---> (24, 8)
cost from (23, 8) to --> (24, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0

Node <(24, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 8)>, Node <(24, 8)>, Node <(23, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (23, 8) with action `up left` toward ---> (22, 7)
cost from (23, 8) to --> (22, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417

Node <(22, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 7)>, Node <(22, 8)>, Node <(24, 8)>, Node <(23, 7)>}]


||From utils.pop() method: we pop() Node <(24, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(24, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (6, 3) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (24, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (24, 8) are: ['left', 'right', 'up left', 'up right']
The successors of the (24, 8) are ['left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (24, 8) with action `left` toward ---> (23, 8)
cost from (24, 8) to --> (23, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 8) is = 8.0

Node <(23, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (24, 8) with action `right` toward ---> (25, 8)
cost from (24, 8) to --> (25, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0

Node <(25, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 8)>, Node <(25, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (24, 8) with action `up left` toward ---> (23, 7)
cost from (24, 8) to --> (23, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855

Node <(23, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 8)>, Node <(23, 7)>, Node <(25, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (24, 8) with action `up right` toward ---> (25, 7)
cost from (24, 8) to --> (25, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219

Node <(25, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 8)>, Node <(23, 7)>, Node <(25, 7)>, Node <(25, 8)>}]

||From utils.append() method: we push the Node <(25, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(25, 8)> Node <(21, 8)> Node <(14, 3)> Node <(23, 6)> Node <(20, 8)> Node <(22, 6)> Node <(13, 4)> Node <(12, 1)> Node <(11, 1)> Node <(12, 4)> Node <(13, 1)> Node <(14, 4)> Node <(9, 1)> Node <(14, 5)> Node <(14, 6)> Node <(5, 2)> Node <(10, 1)> Node <(5, 3)>

||From utils.append() method: we push the Node <(25, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(25, 8)> Node <(21, 8)> Node <(14, 3)> Node <(23, 6)> Node <(20, 8)> Node <(22, 6)> Node <(13, 4)> Node <(12, 1)> Node <(11, 1)> Node <(12, 4)> Node <(13, 1)> Node <(14, 4)> Node <(9, 1)> Node <(14, 5)> Node <(14, 6)> Node <(5, 2)> Node <(10, 1)> Node <(5, 3)> Node <(25, 7)>


||From utils.pop() method: we pop() Node <(25, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(25, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (25, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (6, 3) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (25, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (25, 8) are: ['up', 'left', 'right', 'up right']
The successors of the (25, 8) are ['up', 'left', 'right', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (25, 8) with action `up` toward ---> (25, 7)
cost from (25, 8) to --> (25, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219

Node <(25, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (25, 8) with action `left` toward ---> (24, 8)
cost from (25, 8) to --> (24, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0

Node <(24, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 7)>, Node <(24, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (25, 8) with action `right` toward ---> (26, 8)
cost from (25, 8) to --> (26, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 8) is = 5.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 8) is = 5.0

Node <(26, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 7)>, Node <(24, 8)>, Node <(26, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (25, 8) with action `up right` toward ---> (26, 7)
cost from (25, 8) to --> (26, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845

Node <(26, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 7)>, Node <(24, 8)>, Node <(26, 8)>, Node <(26, 7)>}]

||From utils.append() method: we push the Node <(26, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 8)> Node <(21, 8)> Node <(14, 3)> Node <(23, 6)> Node <(20, 8)> Node <(22, 6)> Node <(13, 4)> Node <(12, 1)> Node <(11, 1)> Node <(12, 4)> Node <(13, 1)> Node <(14, 4)> Node <(9, 1)> Node <(14, 5)> Node <(14, 6)> Node <(5, 2)> Node <(10, 1)> Node <(5, 3)> Node <(25, 7)>

||From utils.append() method: we push the Node <(26, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 8)> Node <(21, 8)> Node <(14, 3)> Node <(23, 6)> Node <(20, 8)> Node <(22, 6)> Node <(13, 4)> Node <(12, 1)> Node <(11, 1)> Node <(12, 4)> Node <(13, 1)> Node <(14, 4)> Node <(9, 1)> Node <(14, 5)> Node <(14, 6)> Node <(5, 2)> Node <(10, 1)> Node <(5, 3)> Node <(25, 7)> Node <(26, 7)>


||From utils.pop() method: we pop() Node <(26, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(26, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (25, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (6, 3) (26, 8) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (26, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`right` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (26, 8) are: ['up', 'left', 'up left']
The successors of the (26, 8) are ['up', 'left', 'up left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (26, 8) with action `up` toward ---> (26, 7)
cost from (26, 8) to --> (26, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845

Node <(26, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (26, 8) with action `left` toward ---> (25, 8)
cost from (26, 8) to --> (25, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0

Node <(25, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 8)>, Node <(26, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (26, 8) with action `up left` toward ---> (25, 7)
cost from (26, 8) to --> (25, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219

Node <(25, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 8)>, Node <(25, 7)>, Node <(26, 7)>}]


||From utils.pop() method: we pop() Node <(21, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(21, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (25, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (21, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (21, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (21, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (21, 8) with action `up` toward ---> (21, 7)
cost from (21, 8) to --> (21, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089

Node <(21, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (21, 8) with action `left` toward ---> (20, 8)
cost from (21, 8) to --> (20, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 8) is = 11.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 8) is = 11.0

Node <(20, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(20, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (21, 8) with action `right` toward ---> (22, 8)
cost from (21, 8) to --> (22, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 8) is = 9.0

Node <(22, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(20, 8)>, Node <(22, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (21, 8) with action `up left` toward ---> (20, 7)
cost from (21, 8) to --> (20, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261

Node <(20, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 7)>, Node <(21, 7)>, Node <(20, 8)>, Node <(22, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (21, 8) with action `up right` toward ---> (22, 7)
cost from (21, 8) to --> (22, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417

Node <(22, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 7)>, Node <(21, 7)>, Node <(22, 7)>, Node <(20, 8)>, Node <(22, 8)>}]


||From utils.pop() method: we pop() Node <(14, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(14, 3)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (18, 8) (25, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (14, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`right` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (14, 3) are: ['down', 'left', 'up left', 'down left', 'down right']
The successors of the (14, 3) are ['down', 'left', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (14, 3) with action `down` toward ---> (14, 4)
cost from (14, 3) to --> (14, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298

Node <(14, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (14, 3) with action `left` toward ---> (13, 3)
cost from (14, 3) to --> (13, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406

Node <(13, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(13, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (14, 3) with action `up left` toward ---> (13, 2)
cost from (14, 3) to --> (13, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276

Node <(13, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(13, 3)>, Node <(13, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (14, 3) with action `down left` toward ---> (13, 4)
cost from (14, 3) to --> (13, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(13, 3)>, Node <(13, 4)>, Node <(13, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (14, 3) with action `down right` toward ---> (15, 4)
cost from (14, 3) to --> (15, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642

Node <(15, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 2)>, Node <(15, 4)>, Node <(13, 4)>, Node <(14, 4)>, Node <(13, 3)>}]

||From utils.append() method: we push the Node <(15, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 6)> Node <(23, 6)> Node <(13, 4)> Node <(11, 1)> Node <(20, 8)> Node <(14, 4)> Node <(14, 6)> Node <(12, 1)> Node <(15, 4)> Node <(12, 4)> Node <(13, 1)> Node <(26, 7)> Node <(9, 1)> Node <(14, 5)> Node <(5, 3)> Node <(5, 2)> Node <(10, 1)> Node <(25, 7)>


||From utils.pop() method: we pop() Node <(22, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(22, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (22, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
Generated actions to generate the successors of the (22, 6) are: ['up', 'down', 'right', 'up right', 'down left', 'down right']
The successors of the (22, 6) are ['up', 'down', 'right', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (22, 6) with action `up` toward ---> (22, 5)
cost from (22, 6) to --> (22, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138

Node <(22, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (22, 6) with action `down` toward ---> (22, 7)
cost from (22, 6) to --> (22, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417

Node <(22, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 5)>, Node <(22, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (22, 6) with action `right` toward ---> (23, 6)
cost from (22, 6) to --> (23, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321

Node <(23, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 5)>, Node <(23, 6)>, Node <(22, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (22, 6) with action `up right` toward ---> (23, 5)
cost from (22, 6) to --> (23, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753

Node <(23, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(22, 5)>, Node <(23, 6)>, Node <(22, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (22, 6) with action `down left` toward ---> (21, 7)
cost from (22, 6) to --> (21, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089

Node <(21, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(22, 5)>, Node <(21, 7)>, Node <(22, 7)>, Node <(23, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (22, 6) with action `down right` toward ---> (23, 7)
cost from (22, 6) to --> (23, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855

Node <(23, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(22, 5)>, Node <(21, 7)>, Node <(22, 7)>, Node <(23, 7)>, Node <(23, 6)>}]

||From utils.append() method: we push the Node <(22, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 6)> Node <(20, 8)> Node <(13, 4)> Node <(11, 1)> Node <(12, 4)> Node <(14, 4)> Node <(14, 6)> Node <(12, 1)> Node <(15, 4)> Node <(25, 7)> Node <(13, 1)> Node <(26, 7)> Node <(9, 1)> Node <(14, 5)> Node <(5, 3)> Node <(5, 2)> Node <(10, 1)> Node <(22, 5)>

||From utils.append() method: we push the Node <(23, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 6)> Node <(20, 8)> Node <(13, 4)> Node <(11, 1)> Node <(12, 4)> Node <(14, 4)> Node <(14, 6)> Node <(12, 1)> Node <(15, 4)> Node <(25, 7)> Node <(13, 1)> Node <(26, 7)> Node <(9, 1)> Node <(14, 5)> Node <(5, 3)> Node <(5, 2)> Node <(10, 1)> Node <(22, 5)> Node <(23, 5)>


||From utils.pop() method: we pop() Node <(23, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(23, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (23, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (23, 6) are: ['up', 'down', 'left', 'up left', 'up right', 'down left']
The successors of the (23, 6) are ['up', 'down', 'left', 'up left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (23, 6) with action `up` toward ---> (23, 5)
cost from (23, 6) to --> (23, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753

Node <(23, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (23, 6) with action `down` toward ---> (23, 7)
cost from (23, 6) to --> (23, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 7) is = 8.06225774829855

Node <(23, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 7)>, Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (23, 6) with action `left` toward ---> (22, 6)
cost from (23, 6) to --> (22, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887

Node <(22, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 7)>, Node <(22, 6)>, Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (23, 6) with action `up left` toward ---> (22, 5)
cost from (23, 6) to --> (22, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138

Node <(22, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 5)>, Node <(23, 7)>, Node <(22, 6)>, Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (23, 6) with action `up right` toward ---> (24, 5)
cost from (23, 6) to --> (24, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909

Node <(24, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 7)>, Node <(22, 6)>, Node <(22, 5)>, Node <(23, 5)>, Node <(24, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (23, 6) with action `down left` toward ---> (22, 7)
cost from (23, 6) to --> (22, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 7) is = 9.055385138137417

Node <(22, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 7)>, Node <(22, 6)>, Node <(22, 7)>, Node <(22, 5)>, Node <(23, 5)>, Node <(24, 5)>}]

||From utils.append() method: we push the Node <(24, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(20, 8)> Node <(12, 4)> Node <(13, 4)> Node <(11, 1)> Node <(13, 1)> Node <(14, 4)> Node <(14, 6)> Node <(12, 1)> Node <(15, 4)> Node <(25, 7)> Node <(23, 5)> Node <(26, 7)> Node <(9, 1)> Node <(14, 5)> Node <(5, 3)> Node <(5, 2)> Node <(10, 1)> Node <(22, 5)> Node <(24, 5)>


||From utils.pop() method: we pop() Node <(20, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(20, 8)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (20, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (20, 8) are: ['up', 'right', 'up right']
The successors of the (20, 8) are ['up', 'right', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (20, 8) with action `up` toward ---> (20, 7)
cost from (20, 8) to --> (20, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 7) is = 11.045361017187261

Node <(20, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (20, 8) with action `right` toward ---> (21, 8)
cost from (20, 8) to --> (21, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 8) is = 10.0

Node <(21, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 8)>, Node <(20, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (20, 8) with action `up right` toward ---> (21, 7)
cost from (20, 8) to --> (21, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 7) is = 10.04987562112089

Node <(21, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 7)>, Node <(21, 8)>, Node <(20, 7)>}]


||From utils.pop() method: we pop() Node <(12, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(12, 4)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (12, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (12, 4) are: ['up', 'down', 'right', 'up left', 'up right', 'down right']
The successors of the (12, 4) are ['up', 'down', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (12, 4) with action `up` toward ---> (12, 3)
cost from (12, 4) to --> (12, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885

Node <(12, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (12, 4) with action `down` toward ---> (12, 5)
cost from (12, 4) to --> (12, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343

Node <(12, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(12, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (12, 4) with action `right` toward ---> (13, 4)
cost from (12, 4) to --> (13, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 3)>, Node <(12, 5)>, Node <(13, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (12, 4) with action `up left` toward ---> (11, 3)
cost from (12, 4) to --> (11, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 3) is = 20.615528128088304

Node <(11, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 3)>, Node <(12, 5)>, Node <(13, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (12, 4) with action `up right` toward ---> (13, 3)
cost from (12, 4) to --> (13, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406

Node <(13, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 5)>, Node <(13, 3)>, Node <(13, 4)>, Node <(12, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (12, 4) with action `down right` toward ---> (13, 5)
cost from (12, 4) to --> (13, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 3)>, Node <(12, 5)>, Node <(13, 5)>, Node <(13, 3)>, Node <(13, 4)>, Node <(12, 3)>}]

||From utils.append() method: we push the Node <(12, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(13, 4)> Node <(11, 1)> Node <(14, 4)> Node <(15, 4)> Node <(13, 1)> Node <(26, 7)> Node <(14, 6)> Node <(12, 1)> Node <(12, 5)> Node <(25, 7)> Node <(23, 5)> Node <(22, 5)> Node <(9, 1)> Node <(14, 5)> Node <(5, 3)> Node <(5, 2)> Node <(10, 1)> Node <(24, 5)>

||From utils.append() method: we push the Node <(13, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(13, 4)> Node <(11, 1)> Node <(14, 4)> Node <(15, 4)> Node <(13, 1)> Node <(26, 7)> Node <(14, 6)> Node <(12, 1)> Node <(13, 5)> Node <(25, 7)> Node <(23, 5)> Node <(22, 5)> Node <(9, 1)> Node <(14, 5)> Node <(5, 3)> Node <(5, 2)> Node <(10, 1)> Node <(24, 5)> Node <(12, 5)>


||From utils.pop() method: we pop() Node <(13, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(13, 4)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (13, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (13, 4) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (13, 4) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (13, 4) with action `up` toward ---> (13, 3)
cost from (13, 4) to --> (13, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406

Node <(13, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (13, 4) with action `down` toward ---> (13, 5)
cost from (13, 4) to --> (13, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 5)>, Node <(13, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (13, 4) with action `left` toward ---> (12, 4)
cost from (13, 4) to --> (12, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476

Node <(12, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>, Node <(13, 5)>, Node <(13, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (13, 4) with action `right` toward ---> (14, 4)
cost from (13, 4) to --> (14, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298

Node <(14, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>, Node <(14, 4)>, Node <(13, 5)>, Node <(13, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (13, 4) with action `up left` toward ---> (12, 3)
cost from (13, 4) to --> (12, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 3) is = 19.6468827043885

Node <(12, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(12, 4)>, Node <(13, 5)>, Node <(13, 3)>, Node <(12, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (13, 4) with action `up right` toward ---> (14, 3)
cost from (13, 4) to --> (14, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935

Node <(14, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(12, 4)>, Node <(13, 5)>, Node <(13, 3)>, Node <(14, 3)>, Node <(12, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (13, 4) with action `down left` toward ---> (12, 5)
cost from (13, 4) to --> (12, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343

Node <(12, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(12, 4)>, Node <(13, 5)>, Node <(13, 3)>, Node <(14, 3)>, Node <(12, 3)>, Node <(12, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (13, 4) with action `down right` toward ---> (14, 5)
cost from (13, 4) to --> (14, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207

Node <(14, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 5)>, Node <(14, 4)>, Node <(12, 4)>, Node <(13, 5)>, Node <(13, 3)>, Node <(14, 3)>, Node <(12, 3)>, Node <(12, 5)>}]

||From utils.append() method: we push the Node <(14, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(14, 4)> Node <(11, 1)> Node <(14, 6)> Node <(15, 4)> Node <(13, 1)> Node <(26, 7)> Node <(5, 3)> Node <(12, 1)> Node <(13, 5)> Node <(25, 7)> Node <(23, 5)> Node <(22, 5)> Node <(9, 1)> Node <(12, 5)> Node <(5, 2)> Node <(10, 1)> Node <(24, 5)> Node <(14, 5)>


||From utils.pop() method: we pop() Node <(14, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(14, 4)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (22, 7) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (14, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (14, 4) are: ['up', 'down', 'left', 'right', 'up left', 'down left']
The successors of the (14, 4) are ['up', 'down', 'left', 'right', 'up left', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (14, 4) with action `up` toward ---> (14, 3)
cost from (14, 4) to --> (14, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935

Node <(14, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (14, 4) with action `down` toward ---> (14, 5)
cost from (14, 4) to --> (14, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207

Node <(14, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 3)>, Node <(14, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (14, 4) with action `left` toward ---> (13, 4)
cost from (14, 4) to --> (13, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 4)>, Node <(14, 3)>, Node <(14, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (14, 4) with action `right` toward ---> (15, 4)
cost from (14, 4) to --> (15, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642

Node <(15, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 4)>, Node <(14, 3)>, Node <(15, 4)>, Node <(14, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (14, 4) with action `up left` toward ---> (13, 3)
cost from (14, 4) to --> (13, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 3) is = 18.681541692269406

Node <(13, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 3)>, Node <(14, 5)>, Node <(13, 4)>, Node <(14, 3)>, Node <(15, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (14, 4) with action `down left` toward ---> (13, 5)
cost from (14, 4) to --> (13, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 5)>, Node <(13, 3)>, Node <(14, 5)>, Node <(13, 4)>, Node <(14, 3)>, Node <(15, 4)>}]


||From utils.pop() method: we pop() Node <(11, 1)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(11, 1)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (11, 1)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (11, 1) are: ['down', 'left', 'right', 'down left', 'down right']
The successors of the (11, 1) are ['down', 'left', 'right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (11, 1) with action `down` toward ---> (11, 2)
cost from (11, 1) to --> (11, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211

Node <(11, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (11, 1) with action `left` toward ---> (10, 1)
cost from (11, 1) to --> (10, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654

Node <(10, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 1)>, Node <(11, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (11, 1) with action `right` toward ---> (12, 1)
cost from (11, 1) to --> (12, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587

Node <(12, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 1)>, Node <(11, 2)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (11, 1) with action `down left` toward ---> (10, 2)
cost from (11, 1) to --> (10, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555

Node <(10, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 1)>, Node <(11, 2)>, Node <(12, 1)>, Node <(10, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (11, 1) with action `down right` toward ---> (12, 2)
cost from (11, 1) to --> (12, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 2)>, Node <(10, 1)>, Node <(11, 2)>, Node <(10, 2)>, Node <(12, 1)>}]


||From utils.pop() method: we pop() Node <(15, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(15, 4)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (15, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (15, 4) are: ['left', 'right', 'up left', 'up right', 'down left']
The successors of the (15, 4) are ['left', 'right', 'up left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (15, 4) with action `left` toward ---> (14, 4)
cost from (15, 4) to --> (14, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298

Node <(14, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (15, 4) with action `right` toward ---> (16, 4)
cost from (15, 4) to --> (16, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 4) is = 15.524174696260024


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 4) is = 15.524174696260024

Node <(16, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 4)>, Node <(14, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (15, 4) with action `up left` toward ---> (14, 3)
cost from (15, 4) to --> (14, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 3) is = 17.72004514666935

Node <(14, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 3)>, Node <(16, 4)>, Node <(14, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (15, 4) with action `up right` toward ---> (16, 3)
cost from (15, 4) to --> (16, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 3) is = 15.811388300841896


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 3) is = 15.811388300841896

Node <(16, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 3)>, Node <(16, 4)>, Node <(16, 3)>, Node <(14, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (15, 4) with action `down left` toward ---> (14, 5)
cost from (15, 4) to --> (14, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207

Node <(14, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(14, 3)>, Node <(16, 4)>, Node <(16, 3)>, Node <(14, 5)>}]

||From utils.append() method: we push the Node <(16, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 4)> Node <(12, 1)> Node <(14, 6)> Node <(13, 1)> Node <(25, 7)> Node <(26, 7)> Node <(5, 3)> Node <(10, 1)> Node <(13, 5)> Node <(24, 5)> Node <(23, 5)> Node <(22, 5)> Node <(9, 1)> Node <(12, 5)> Node <(5, 2)> Node <(14, 5)>

||From utils.append() method: we push the Node <(16, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 4)> Node <(12, 1)> Node <(14, 6)> Node <(13, 1)> Node <(25, 7)> Node <(26, 7)> Node <(5, 3)> Node <(10, 1)> Node <(13, 5)> Node <(24, 5)> Node <(23, 5)> Node <(22, 5)> Node <(9, 1)> Node <(12, 5)> Node <(5, 2)> Node <(14, 5)> Node <(16, 3)>


||From utils.pop() method: we pop() Node <(16, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(16, 4)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (16, 4) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (16, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`right` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (16, 4) are: ['up', 'left', 'up right']
The successors of the (16, 4) are ['up', 'left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (16, 4) with action `up` toward ---> (16, 3)
cost from (16, 4) to --> (16, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 3) is = 15.811388300841896


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 3) is = 15.811388300841896

Node <(16, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (16, 4) with action `left` toward ---> (15, 4)
cost from (16, 4) to --> (15, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642

Node <(15, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 4)>, Node <(16, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (16, 4) with action `up right` toward ---> (17, 3)
cost from (16, 4) to --> (17, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 3) is = 14.866068747318506


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 3) is = 14.866068747318506

Node <(17, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 3)>, Node <(15, 4)>, Node <(16, 3)>}]

||From utils.append() method: we push the Node <(17, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(12, 1)> Node <(13, 1)> Node <(14, 6)> Node <(10, 1)> Node <(25, 7)> Node <(26, 7)> Node <(5, 3)> Node <(14, 5)> Node <(13, 5)> Node <(24, 5)> Node <(23, 5)> Node <(22, 5)> Node <(9, 1)> Node <(12, 5)> Node <(5, 2)> Node <(16, 3)> Node <(17, 3)>


||From utils.pop() method: we pop() Node <(12, 1)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(12, 1)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (12, 1) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (16, 4) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (12, 1)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (12, 1) are: ['down', 'left', 'right', 'down left', 'down right']
The successors of the (12, 1) are ['down', 'left', 'right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (12, 1) with action `down` toward ---> (12, 2)
cost from (12, 1) to --> (12, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (12, 1) with action `left` toward ---> (11, 1)
cost from (12, 1) to --> (11, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709

Node <(11, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(12, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (12, 1) with action `right` toward ---> (13, 1)
cost from (12, 1) to --> (13, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 1) is = 19.313207915827967


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 1) is = 19.313207915827967

Node <(13, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(12, 2)>, Node <(13, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (12, 1) with action `down left` toward ---> (11, 2)
cost from (12, 1) to --> (11, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211

Node <(11, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 2)>, Node <(11, 1)>, Node <(12, 2)>, Node <(13, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (12, 1) with action `down right` toward ---> (13, 2)
cost from (12, 1) to --> (13, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276

Node <(13, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 2)>, Node <(13, 1)>, Node <(11, 1)>, Node <(12, 2)>, Node <(13, 2)>}]


||From utils.pop() method: we pop() Node <(13, 1)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(13, 1)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (12, 1) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (16, 4) (9, 3) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (13, 1) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (13, 1)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`right` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (13, 1) are: ['down', 'left', 'down left']
The successors of the (13, 1) are ['down', 'left', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (13, 1) with action `down` toward ---> (13, 2)
cost from (13, 1) to --> (13, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 2) is = 18.973665961010276

Node <(13, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (13, 1) with action `left` toward ---> (12, 1)
cost from (13, 1) to --> (12, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 1) is = 20.248456731316587

Node <(12, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 2)>, Node <(12, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (13, 1) with action `down left` toward ---> (12, 2)
cost from (13, 1) to --> (12, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 2) is = 19.924858845171276

Node <(12, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 2)>, Node <(13, 2)>, Node <(12, 1)>}]


||From utils.pop() method: we pop() Node <(14, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(14, 6)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (12, 1) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (16, 4) (9, 3) (14, 6) (7, 5) (18, 6) (15, 7) (8, 7) (20, 5) (9, 6) (6, 5) (13, 1) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (14, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (14, 6) are: ['up', 'left', 'right', 'up left', 'down right']
The successors of the (14, 6) are ['up', 'left', 'right', 'up left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (14, 6) with action `up` toward ---> (14, 5)
cost from (14, 6) to --> (14, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207

Node <(14, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (14, 6) with action `left` toward ---> (13, 6)
cost from (14, 6) to --> (13, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835

Node <(13, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 5)>, Node <(13, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (14, 6) with action `right` toward ---> (15, 6)
cost from (14, 6) to --> (15, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971

Node <(15, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 5)>, Node <(15, 6)>, Node <(13, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (14, 6) with action `up left` toward ---> (13, 5)
cost from (14, 6) to --> (13, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 5)>, Node <(13, 5)>, Node <(15, 6)>, Node <(13, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (14, 6) with action `down right` toward ---> (15, 7)
cost from (14, 6) to --> (15, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 7) is = 16.0312195418814

Node <(15, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 7)>, Node <(14, 5)>, Node <(15, 6)>, Node <(13, 5)>, Node <(13, 6)>}]

||From utils.append() method: we push the Node <(13, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(10, 1)> Node <(25, 7)> Node <(26, 7)> Node <(13, 5)> Node <(23, 5)> Node <(22, 5)> Node <(5, 3)> Node <(14, 5)> Node <(17, 3)> Node <(24, 5)> Node <(5, 2)> Node <(16, 3)> Node <(9, 1)> Node <(12, 5)> Node <(13, 6)>


||From utils.pop() method: we pop() Node <(10, 1)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(10, 1)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (12, 1) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (16, 4) (9, 3) (14, 6) (7, 5) (18, 6) (15, 7) (8, 7) (10, 1) (20, 5) (9, 6) (6, 5) (13, 1) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (10, 1)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (10, 1) are: ['down', 'left', 'right', 'down right']
The successors of the (10, 1) are ['down', 'left', 'right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (10, 1) with action `down` toward ---> (10, 2)
cost from (10, 1) to --> (10, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555

Node <(10, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (10, 1) with action `left` toward ---> (9, 1)
cost from (10, 1) to --> (9, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 1) is = 23.08679276123039


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (9, 1) is = 23.08679276123039

Node <(9, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(10, 2)>, Node <(9, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (10, 1) with action `right` toward ---> (11, 1)
cost from (10, 1) to --> (11, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 1) is = 21.18962010041709

Node <(11, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(10, 2)>, Node <(9, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (10, 1) with action `down right` toward ---> (11, 2)
cost from (10, 1) to --> (11, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (11, 2) is = 20.8806130178211

Node <(11, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(11, 1)>, Node <(10, 2)>, Node <(9, 1)>, Node <(11, 2)>}]


||From utils.pop() method: we pop() Node <(25, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(25, 7)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (12, 1) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (16, 4) (9, 3) (14, 6) (25, 7) (7, 5) (18, 6) (15, 7) (8, 7) (10, 1) (20, 5) (9, 6) (6, 5) (13, 1) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (25, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
Generated actions to generate the successors of the (25, 7) are: ['up', 'down', 'right', 'up right', 'down left', 'down right']
The successors of the (25, 7) are ['up', 'down', 'right', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (25, 7) with action `up` toward ---> (25, 6)
cost from (25, 7) to --> (25, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (25, 7) with action `down` toward ---> (25, 8)
cost from (25, 7) to --> (25, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0

Node <(25, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 8)>, Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (25, 7) with action `right` toward ---> (26, 7)
cost from (25, 7) to --> (26, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845

Node <(26, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 7)>, Node <(25, 8)>, Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (25, 7) with action `up right` toward ---> (26, 6)
cost from (25, 7) to --> (26, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 7)>, Node <(25, 8)>, Node <(26, 6)>, Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (25, 7) with action `down left` toward ---> (24, 8)
cost from (25, 7) to --> (24, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 8) is = 7.0

Node <(24, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>, Node <(26, 7)>, Node <(25, 6)>, Node <(24, 8)>, Node <(25, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (25, 7) with action `down right` toward ---> (26, 8)
cost from (25, 7) to --> (26, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 8) is = 5.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 8) is = 5.0

Node <(26, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>, Node <(26, 7)>, Node <(25, 6)>, Node <(26, 8)>, Node <(24, 8)>, Node <(25, 8)>}]

||From utils.append() method: we push the Node <(25, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 7)> Node <(13, 5)> Node <(5, 3)> Node <(14, 5)> Node <(23, 5)> Node <(22, 5)> Node <(12, 5)> Node <(13, 6)> Node <(17, 3)> Node <(24, 5)> Node <(5, 2)> Node <(16, 3)> Node <(9, 1)> Node <(25, 6)>

||From utils.append() method: we push the Node <(26, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 7)> Node <(13, 5)> Node <(5, 3)> Node <(14, 5)> Node <(23, 5)> Node <(22, 5)> Node <(12, 5)> Node <(13, 6)> Node <(17, 3)> Node <(24, 5)> Node <(5, 2)> Node <(16, 3)> Node <(9, 1)> Node <(25, 6)> Node <(26, 6)>


||From utils.pop() method: we pop() Node <(26, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(26, 7)>

CLOSED List in traditional has these nodes: (16, 6) (17, 8) (7, 3) (24, 8) (12, 1) (6, 6) (5, 6) (17, 7) (9, 8) (10, 6) (11, 2) (7, 7) (23, 8) (13, 4) (14, 4) (20, 7) (15, 8) (13, 8) (8, 4) (22, 6) (18, 8) (25, 8) (20, 8) (8, 5) (23, 7) (16, 7) (5, 8) (10, 8) (12, 2) (6, 7) (5, 5) (13, 3) (7, 6) (10, 2) (18, 5) (21, 8) (6, 3) (26, 8) (11, 1) (22, 7) (15, 4) (8, 6) (23, 6) (26, 7) (12, 3) (9, 7) (6, 4) (5, 4) (13, 2) (19, 6) (16, 4) (9, 3) (14, 6) (25, 7) (7, 5) (18, 6) (15, 7) (8, 7) (10, 1) (20, 5) (9, 6) (6, 5) (13, 1) (10, 5) (8, 3) (6, 8) (11, 8) (16, 8) (5, 7) (11, 3) (19, 5) (7, 4) (18, 7) (15, 6) (8, 8) (12, 4) (20, 6) (22, 8) (14, 3) (9, 5) (21, 7) (7, 8) (14, 8) (12, 8)
In the expand () method of the model now, we have this state: (26, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (26, 7) are: ['up', 'down', 'left', 'up left', 'down left']
The successors of the (26, 7) are ['up', 'down', 'left', 'up left', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (26, 7) with action `up` toward ---> (26, 6)
cost from (26, 7) to --> (26, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (26, 7) with action `down` toward ---> (26, 8)
cost from (26, 7) to --> (26, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 8) is = 5.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 8) is = 5.0

Node <(26, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 8)>, Node <(26, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (26, 7) with action `left` toward ---> (25, 7)
cost from (26, 7) to --> (25, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219

Node <(25, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 8)>, Node <(25, 7)>, Node <(26, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (26, 7) with action `up left` toward ---> (25, 6)
cost from (26, 7) to --> (25, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(26, 8)>, Node <(25, 7)>, Node <(26, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (26, 7) with action `down left` toward ---> (25, 8)
cost from (26, 7) to --> (25, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 8) is = 6.0

Node <(25, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>, Node <(25, 6)>, Node <(25, 8)>, Node <(25, 7)>, Node <(26, 8)>}]


||From utils.pop() method: we pop() Node <(13, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(13, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (16, 7) (12, 2) (13, 3) (18, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (13, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (13, 5) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (13, 5) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (13, 5) with action `up` toward ---> (13, 4)
cost from (13, 5) to --> (13, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (13, 5) with action `down` toward ---> (13, 6)
cost from (13, 5) to --> (13, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835

Node <(13, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 6)>, Node <(13, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (13, 5) with action `left` toward ---> (12, 5)
cost from (13, 5) to --> (12, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343

Node <(12, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 6)>, Node <(12, 5)>, Node <(13, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (13, 5) with action `right` toward ---> (14, 5)
cost from (13, 5) to --> (14, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207

Node <(14, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 6)>, Node <(12, 5)>, Node <(13, 4)>, Node <(14, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (13, 5) with action `up left` toward ---> (12, 4)
cost from (13, 5) to --> (12, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476

Node <(12, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 6)>, Node <(12, 5)>, Node <(13, 4)>, Node <(12, 4)>, Node <(14, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (13, 5) with action `up right` toward ---> (14, 4)
cost from (13, 5) to --> (14, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298

Node <(14, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 6)>, Node <(12, 5)>, Node <(13, 4)>, Node <(12, 4)>, Node <(14, 4)>, Node <(14, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (13, 5) with action `down left` toward ---> (12, 6)
cost from (13, 5) to --> (12, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 6) is = 19.1049731745428


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 6) is = 19.1049731745428

Node <(12, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 6)>, Node <(12, 5)>, Node <(13, 4)>, Node <(12, 4)>, Node <(14, 4)>, Node <(14, 5)>, Node <(12, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (13, 5) with action `down right` toward ---> (14, 6)
cost from (13, 5) to --> (14, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369

Node <(14, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 6)>, Node <(12, 5)>, Node <(13, 4)>, Node <(12, 4)>, Node <(14, 4)>, Node <(14, 6)>, Node <(14, 5)>, Node <(12, 6)>}]

||From utils.append() method: we push the Node <(13, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(14, 5)> Node <(23, 5)> Node <(5, 3)> Node <(17, 3)> Node <(24, 5)> Node <(22, 5)> Node <(12, 5)> Node <(26, 6)> Node <(25, 6)> Node <(5, 2)> Node <(16, 3)> Node <(9, 1)> Node <(13, 6)>

||From utils.append() method: we push the Node <(12, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(14, 5)> Node <(23, 5)> Node <(5, 3)> Node <(17, 3)> Node <(24, 5)> Node <(22, 5)> Node <(12, 5)> Node <(26, 6)> Node <(25, 6)> Node <(5, 2)> Node <(16, 3)> Node <(9, 1)> Node <(13, 6)> Node <(12, 6)>


||From utils.pop() method: we pop() Node <(14, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(14, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (14, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
Generated actions to generate the successors of the (14, 5) are: ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']
The successors of the (14, 5) are ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (14, 5) with action `up` toward ---> (14, 4)
cost from (14, 5) to --> (14, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 4) is = 17.46424919657298

Node <(14, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (14, 5) with action `down` toward ---> (14, 6)
cost from (14, 5) to --> (14, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369

Node <(14, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(14, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (14, 5) with action `left` toward ---> (13, 5)
cost from (14, 5) to --> (13, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(13, 5)>, Node <(14, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (14, 5) with action `up left` toward ---> (13, 4)
cost from (14, 5) to --> (13, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 4)>, Node <(13, 5)>, Node <(14, 6)>, Node <(13, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (14, 5) with action `up right` toward ---> (15, 4)
cost from (14, 5) to --> (15, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642

Node <(15, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 6)>, Node <(13, 4)>, Node <(14, 4)>, Node <(13, 5)>, Node <(15, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (14, 5) with action `down left` toward ---> (13, 6)
cost from (14, 5) to --> (13, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835

Node <(13, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 6)>, Node <(13, 4)>, Node <(13, 6)>, Node <(14, 4)>, Node <(13, 5)>, Node <(15, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (14, 5) with action `down right` toward ---> (15, 6)
cost from (14, 5) to --> (15, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 6) is = 16.1245154965971

Node <(15, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 6)>, Node <(13, 4)>, Node <(13, 6)>, Node <(14, 4)>, Node <(15, 6)>, Node <(13, 5)>, Node <(15, 4)>}]


||From utils.pop() method: we pop() Node <(5, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(5, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (5, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (5, 3) are: ['up', 'down', 'right', 'down right']
The successors of the (5, 3) are ['up', 'down', 'right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (5, 3) with action `up` toward ---> (5, 2)
cost from (5, 3) to --> (5, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 2) is = 26.68332812825267


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 2) is = 26.68332812825267

Node <(5, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (5, 3) with action `down` toward ---> (5, 4)
cost from (5, 3) to --> (5, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 4) is = 26.30589287593181

Node <(5, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 2)>, Node <(5, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (5, 3) with action `right` toward ---> (6, 3)
cost from (5, 3) to --> (6, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924

Node <(6, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 2)>, Node <(5, 4)>, Node <(6, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (5, 3) with action `down right` toward ---> (6, 4)
cost from (5, 3) to --> (6, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 4) is = 25.317977802344327

Node <(6, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 2)>, Node <(5, 4)>, Node <(6, 4)>, Node <(6, 3)>}]


||From utils.pop() method: we pop() Node <(12, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(12, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (12, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (12, 5) are: ['up', 'down', 'right', 'up right', 'down right']
The successors of the (12, 5) are ['up', 'down', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (12, 5) with action `up` toward ---> (12, 4)
cost from (12, 5) to --> (12, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 4) is = 19.4164878389476

Node <(12, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (12, 5) with action `down` toward ---> (12, 6)
cost from (12, 5) to --> (12, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 6) is = 19.1049731745428


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 6) is = 19.1049731745428

Node <(12, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>, Node <(12, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (12, 5) with action `right` toward ---> (13, 5)
cost from (12, 5) to --> (13, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>, Node <(13, 5)>, Node <(12, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (12, 5) with action `up right` toward ---> (13, 4)
cost from (12, 5) to --> (13, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 4) is = 18.439088914585774

Node <(13, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 4)>, Node <(13, 5)>, Node <(13, 4)>, Node <(12, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (12, 5) with action `down right` toward ---> (13, 6)
cost from (12, 5) to --> (13, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835

Node <(13, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 4)>, Node <(13, 5)>, Node <(12, 6)>, Node <(12, 4)>, Node <(13, 6)>}]

||From utils.append() method: we push the Node <(12, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 5)> Node <(24, 5)> Node <(22, 5)> Node <(17, 3)> Node <(16, 3)> Node <(13, 6)> Node <(26, 6)> Node <(25, 6)> Node <(5, 2)> Node <(9, 1)> Node <(12, 6)>


||From utils.pop() method: we pop() Node <(23, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(23, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (23, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (23, 5) are: ['up', 'down', 'left', 'right', 'up left', 'down left']
The successors of the (23, 5) are ['up', 'down', 'left', 'right', 'up left', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (23, 5) with action `up` toward ---> (23, 4)
cost from (23, 5) to --> (23, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916

Node <(23, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (23, 5) with action `down` toward ---> (23, 6)
cost from (23, 5) to --> (23, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321

Node <(23, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 6)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (23, 5) with action `left` toward ---> (22, 5)
cost from (23, 5) to --> (22, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138

Node <(22, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 6)>, Node <(22, 5)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (23, 5) with action `right` toward ---> (24, 5)
cost from (23, 5) to --> (24, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909

Node <(24, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 6)>, Node <(22, 5)>, Node <(24, 5)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (23, 5) with action `up left` toward ---> (22, 4)
cost from (23, 5) to --> (22, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104

Node <(22, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 6)>, Node <(23, 4)>, Node <(24, 5)>, Node <(22, 5)>, Node <(22, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (23, 5) with action `down left` toward ---> (22, 6)
cost from (23, 5) to --> (22, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887

Node <(22, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 6)>, Node <(23, 6)>, Node <(23, 4)>, Node <(24, 5)>, Node <(22, 5)>, Node <(22, 4)>}]

||From utils.append() method: we push the Node <(23, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(24, 5)> Node <(16, 3)> Node <(22, 5)> Node <(17, 3)> Node <(12, 6)> Node <(13, 6)> Node <(26, 6)> Node <(25, 6)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)>

||From utils.append() method: we push the Node <(22, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(24, 5)> Node <(16, 3)> Node <(22, 5)> Node <(17, 3)> Node <(12, 6)> Node <(13, 6)> Node <(26, 6)> Node <(25, 6)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(22, 4)>


||From utils.pop() method: we pop() Node <(24, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(24, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (24, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (24, 5) are: ['left', 'right', 'up left', 'down left', 'down right']
The successors of the (24, 5) are ['left', 'right', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (24, 5) with action `left` toward ---> (23, 5)
cost from (24, 5) to --> (23, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753

Node <(23, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (24, 5) with action `right` toward ---> (25, 5)
cost from (24, 5) to --> (25, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369

Node <(25, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 5)>, Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (24, 5) with action `up left` toward ---> (23, 4)
cost from (24, 5) to --> (23, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916

Node <(23, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 5)>, Node <(23, 5)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (24, 5) with action `down left` toward ---> (23, 6)
cost from (24, 5) to --> (23, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321

Node <(23, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 5)>, Node <(23, 5)>, Node <(23, 6)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (24, 5) with action `down right` toward ---> (25, 6)
cost from (24, 5) to --> (25, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(25, 5)>, Node <(23, 5)>, Node <(23, 6)>, Node <(23, 4)>}]

||From utils.append() method: we push the Node <(25, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(25, 5)> Node <(16, 3)> Node <(22, 5)> Node <(17, 3)> Node <(12, 6)> Node <(26, 6)> Node <(22, 4)> Node <(25, 6)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(13, 6)>

||From utils.append() method: we push the Node <(25, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(25, 5)> Node <(16, 3)> Node <(22, 5)> Node <(17, 3)> Node <(12, 6)> Node <(25, 6)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(13, 6)> Node <(26, 6)>


||From utils.pop() method: we pop() Node <(25, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(25, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (25, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (25, 5) are: ['down', 'left', 'right', 'down right']
The successors of the (25, 5) are ['down', 'left', 'right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (25, 5) with action `down` toward ---> (25, 6)
cost from (25, 5) to --> (25, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (25, 5) with action `left` toward ---> (24, 5)
cost from (25, 5) to --> (24, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909

Node <(24, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 5)>, Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (25, 5) with action `right` toward ---> (26, 5)
cost from (25, 5) to --> (26, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301

Node <(26, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 5)>, Node <(26, 5)>, Node <(25, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (25, 5) with action `down right` toward ---> (26, 6)
cost from (25, 5) to --> (26, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 5)>, Node <(26, 5)>, Node <(25, 6)>, Node <(26, 6)>}]

||From utils.append() method: we push the Node <(26, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 5)> Node <(16, 3)> Node <(26, 5)> Node <(17, 3)> Node <(12, 6)> Node <(25, 6)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(13, 6)> Node <(26, 6)>


||From utils.pop() method: we pop() Node <(22, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(22, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (22, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (22, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (22, 5) are: ['up', 'down', 'right', 'up right', 'down right']
The successors of the (22, 5) are ['up', 'down', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (22, 5) with action `up` toward ---> (22, 4)
cost from (22, 5) to --> (22, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104

Node <(22, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (22, 5) with action `down` toward ---> (22, 6)
cost from (22, 5) to --> (22, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 6) is = 9.219544457292887

Node <(22, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 4)>, Node <(22, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (22, 5) with action `right` toward ---> (23, 5)
cost from (22, 5) to --> (23, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753

Node <(23, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 4)>, Node <(22, 6)>, Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (22, 5) with action `up right` toward ---> (23, 4)
cost from (22, 5) to --> (23, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916

Node <(23, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 4)>, Node <(22, 4)>, Node <(22, 6)>, Node <(23, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (22, 5) with action `down right` toward ---> (23, 6)
cost from (22, 5) to --> (23, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 6) is = 8.246211251235321

Node <(23, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 6)>, Node <(23, 4)>, Node <(22, 4)>, Node <(23, 6)>, Node <(23, 5)>}]

||From utils.append() method: we push the Node <(22, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(16, 3)> Node <(17, 3)> Node <(26, 5)> Node <(26, 6)> Node <(12, 6)> Node <(25, 6)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(13, 6)> Node <(22, 4)>


||From utils.pop() method: we pop() Node <(16, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(16, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (22, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (16, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`left` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (16, 3) are: ['down', 'right', 'down left']
The successors of the (16, 3) are ['down', 'right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (16, 3) with action `down` toward ---> (16, 4)
cost from (16, 3) to --> (16, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 4) is = 15.524174696260024


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 4) is = 15.524174696260024

Node <(16, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (16, 3) with action `right` toward ---> (17, 3)
cost from (16, 3) to --> (17, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 3) is = 14.866068747318506


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 3) is = 14.866068747318506

Node <(17, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 4)>, Node <(17, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (16, 3) with action `down left` toward ---> (15, 4)
cost from (16, 3) to --> (15, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (15, 4) is = 16.492422502470642

Node <(15, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(15, 4)>, Node <(16, 4)>, Node <(17, 3)>}]


||From utils.pop() method: we pop() Node <(26, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(26, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (26, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (26, 5) are: ['down', 'left', 'right', 'down left']
The successors of the (26, 5) are ['down', 'left', 'right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (26, 5) with action `down` toward ---> (26, 6)
cost from (26, 5) to --> (26, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (26, 5) with action `left` toward ---> (25, 5)
cost from (26, 5) to --> (25, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369

Node <(25, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>, Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (26, 5) with action `right` toward ---> (27, 5)
cost from (26, 5) to --> (27, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(27, 5)>, Node <(26, 6)>, Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (26, 5) with action `down left` toward ---> (25, 6)
cost from (26, 5) to --> (25, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(27, 5)>, Node <(26, 6)>, Node <(25, 6)>, Node <(25, 5)>}]

||From utils.append() method: we push the Node <(27, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(17, 3)> Node <(27, 5)> Node <(25, 6)> Node <(13, 6)> Node <(26, 6)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(12, 6)>


||From utils.pop() method: we pop() Node <(17, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(17, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (17, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (17, 3) are: ['left', 'right', 'down left']
The successors of the (17, 3) are ['left', 'right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (17, 3) with action `left` toward ---> (16, 3)
cost from (17, 3) to --> (16, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 3) is = 15.811388300841896


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 3) is = 15.811388300841896

Node <(16, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (17, 3) with action `right` toward ---> (18, 3)
cost from (17, 3) to --> (18, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 3) is = 13.92838827718412


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 3) is = 13.92838827718412

Node <(18, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 3)>, Node <(18, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (17, 3) with action `down left` toward ---> (16, 4)
cost from (17, 3) to --> (16, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 4) is = 15.524174696260024


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (16, 4) is = 15.524174696260024

Node <(16, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(16, 3)>, Node <(16, 4)>, Node <(18, 3)>}]

||From utils.append() method: we push the Node <(18, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(18, 3)> Node <(27, 5)> Node <(25, 6)> Node <(13, 6)> Node <(26, 6)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(12, 6)>


||From utils.pop() method: we pop() Node <(18, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(18, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (18, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (18, 3) are: ['left', 'right']
The successors of the (18, 3) are ['left', 'right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (18, 3) with action `left` toward ---> (17, 3)
cost from (18, 3) to --> (17, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 3) is = 14.866068747318506


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (17, 3) is = 14.866068747318506

Node <(17, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (18, 3) with action `right` toward ---> (19, 3)
cost from (18, 3) to --> (19, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 3) is = 13.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 3) is = 13.0

Node <(19, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(17, 3)>, Node <(19, 3)>}]

||From utils.append() method: we push the Node <(19, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(27, 5)> Node <(19, 3)> Node <(25, 6)> Node <(13, 6)> Node <(26, 6)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(12, 6)>


||From utils.pop() method: we pop() Node <(27, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(27, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (27, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
Generated actions to generate the successors of the (27, 5) are: ['left', 'right', 'down left', 'down right']
The successors of the (27, 5) are ['left', 'right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (27, 5) with action `left` toward ---> (26, 5)
cost from (27, 5) to --> (26, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301

Node <(26, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (27, 5) with action `right` toward ---> (28, 5)
cost from (27, 5) to --> (28, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285

Node <(28, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (27, 5) with action `down left` toward ---> (26, 6)
cost from (27, 5) to --> (26, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(26, 6)>, Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (27, 5) with action `down right` toward ---> (28, 6)
cost from (27, 5) to --> (28, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(26, 6)>, Node <(26, 5)>, Node <(28, 6)>}]

||From utils.append() method: we push the Node <(28, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(19, 3)> Node <(26, 6)> Node <(25, 6)> Node <(13, 6)> Node <(28, 5)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(12, 6)>

||From utils.append() method: we push the Node <(28, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(19, 3)> Node <(26, 6)> Node <(25, 6)> Node <(13, 6)> Node <(28, 5)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(12, 6)> Node <(28, 6)>


||From utils.pop() method: we pop() Node <(19, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(19, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (19, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (19, 3) are: ['left', 'right']
The successors of the (19, 3) are ['left', 'right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (19, 3) with action `left` toward ---> (18, 3)
cost from (19, 3) to --> (18, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 3) is = 13.92838827718412


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (18, 3) is = 13.92838827718412

Node <(18, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(18, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (19, 3) with action `right` toward ---> (20, 3)
cost from (19, 3) to --> (20, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 3) is = 12.083045973594572


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 3) is = 12.083045973594572

Node <(20, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 3)>, Node <(18, 3)>}]

||From utils.append() method: we push the Node <(20, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(25, 6)> Node <(20, 3)> Node <(28, 6)> Node <(13, 6)> Node <(26, 6)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(12, 6)> Node <(28, 5)>


||From utils.pop() method: we pop() Node <(25, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(25, 6)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (25, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (25, 6) are: ['up', 'down', 'right', 'up left', 'up right', 'down right']
The successors of the (25, 6) are ['up', 'down', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (25, 6) with action `up` toward ---> (25, 5)
cost from (25, 6) to --> (25, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369

Node <(25, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (25, 6) with action `down` toward ---> (25, 7)
cost from (25, 6) to --> (25, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219

Node <(25, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 7)>, Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (25, 6) with action `right` toward ---> (26, 6)
cost from (25, 6) to --> (26, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 6) is = 5.385164807134504

Node <(26, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 6)>, Node <(25, 7)>, Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (25, 6) with action `up left` toward ---> (24, 5)
cost from (25, 6) to --> (24, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909

Node <(24, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 5)>, Node <(26, 6)>, Node <(25, 7)>, Node <(25, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (25, 6) with action `up right` toward ---> (26, 5)
cost from (25, 6) to --> (26, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301

Node <(26, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>, Node <(25, 5)>, Node <(24, 5)>, Node <(26, 6)>, Node <(25, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (25, 6) with action `down right` toward ---> (26, 7)
cost from (25, 6) to --> (26, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845

Node <(26, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>, Node <(25, 5)>, Node <(24, 5)>, Node <(26, 6)>, Node <(26, 7)>, Node <(25, 7)>}]


||From utils.pop() method: we pop() Node <(20, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(20, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (20, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (20, 3) are: ['left', 'right']
The successors of the (20, 3) are ['left', 'right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (20, 3) with action `left` toward ---> (19, 3)
cost from (20, 3) to --> (19, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 3) is = 13.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (19, 3) is = 13.0

Node <(19, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (20, 3) with action `right` toward ---> (21, 3)
cost from (20, 3) to --> (21, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 3) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 3) is = 11.180339887498949

Node <(21, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(19, 3)>, Node <(21, 3)>}]

||From utils.append() method: we push the Node <(21, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 6)> Node <(13, 6)> Node <(28, 6)> Node <(12, 6)> Node <(21, 3)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(23, 4)> Node <(28, 5)>


||From utils.pop() method: we pop() Node <(26, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(26, 6)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (26, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (26, 6) are: ['up', 'down', 'left', 'up left', 'up right', 'down left']
The successors of the (26, 6) are ['up', 'down', 'left', 'up left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (26, 6) with action `up` toward ---> (26, 5)
cost from (26, 6) to --> (26, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 5) is = 5.830951894845301

Node <(26, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (26, 6) with action `down` toward ---> (26, 7)
cost from (26, 6) to --> (26, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 7) is = 5.0990195135927845

Node <(26, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 5)>, Node <(26, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (26, 6) with action `left` toward ---> (25, 6)
cost from (26, 6) to --> (25, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 6) is = 6.324555320336759

Node <(25, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(26, 5)>, Node <(26, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (26, 6) with action `up left` toward ---> (25, 5)
cost from (26, 6) to --> (25, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 5) is = 6.708203932499369

Node <(25, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(26, 5)>, Node <(25, 5)>, Node <(26, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (26, 6) with action `up right` toward ---> (27, 5)
cost from (26, 6) to --> (27, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(27, 5)>, Node <(26, 5)>, Node <(25, 5)>, Node <(26, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (26, 6) with action `down left` toward ---> (25, 7)
cost from (26, 6) to --> (25, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 7) is = 6.082762530298219

Node <(25, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 6)>, Node <(27, 5)>, Node <(25, 7)>, Node <(26, 5)>, Node <(25, 5)>, Node <(26, 7)>}]


||From utils.pop() method: we pop() Node <(13, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(13, 6)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (13, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (13, 6) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (13, 6) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (13, 6) with action `up` toward ---> (13, 5)
cost from (13, 6) to --> (13, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (13, 6) with action `left` toward ---> (12, 6)
cost from (13, 6) to --> (12, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 6) is = 19.1049731745428


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 6) is = 19.1049731745428

Node <(12, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 5)>, Node <(12, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (13, 6) with action `right` toward ---> (14, 6)
cost from (13, 6) to --> (14, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 6) is = 17.11724276862369

Node <(14, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(13, 5)>, Node <(12, 6)>, Node <(14, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (13, 6) with action `up left` toward ---> (12, 5)
cost from (13, 6) to --> (12, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343

Node <(12, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 5)>, Node <(13, 5)>, Node <(12, 6)>, Node <(14, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (13, 6) with action `up right` toward ---> (14, 5)
cost from (13, 6) to --> (14, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (14, 5) is = 17.26267650163207

Node <(14, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(14, 6)>, Node <(12, 5)>, Node <(13, 5)>, Node <(14, 5)>, Node <(12, 6)>}]


||From utils.pop() method: we pop() Node <(21, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(21, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (21, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (21, 3) are: ['left', 'right', 'up right', 'down right']
The successors of the (21, 3) are ['left', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (21, 3) with action `left` toward ---> (20, 3)
cost from (21, 3) to --> (20, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 3) is = 12.083045973594572


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (20, 3) is = 12.083045973594572

Node <(20, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (21, 3) with action `right` toward ---> (22, 3)
cost from (21, 3) to --> (22, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987

Node <(22, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 3)>, Node <(22, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (21, 3) with action `up right` toward ---> (22, 2)
cost from (21, 3) to --> (22, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 2) is = 10.816653826391969


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 2) is = 10.816653826391969

Node <(22, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 3)>, Node <(22, 2)>, Node <(22, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (21, 3) with action `down right` toward ---> (22, 4)
cost from (21, 3) to --> (22, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104

Node <(22, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(20, 3)>, Node <(22, 2)>, Node <(22, 3)>, Node <(22, 4)>}]

||From utils.append() method: we push the Node <(22, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 5)> Node <(22, 3)> Node <(28, 6)> Node <(12, 6)> Node <(23, 4)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)>

||From utils.append() method: we push the Node <(22, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 5)> Node <(22, 3)> Node <(28, 6)> Node <(12, 6)> Node <(23, 4)> Node <(22, 4)> Node <(5, 2)> Node <(9, 1)> Node <(22, 2)>

||From utils.append() method: we push the Node <(22, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 5)> Node <(22, 3)> Node <(28, 6)> Node <(12, 6)> Node <(23, 4)> Node <(5, 2)> Node <(9, 1)> Node <(22, 2)> Node <(22, 4)>


||From utils.pop() method: we pop() Node <(28, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(28, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (28, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (28, 5) are: ['down', 'left', 'right', 'down right']
The successors of the (28, 5) are ['down', 'left', 'right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (28, 5) with action `down` toward ---> (28, 6)
cost from (28, 5) to --> (28, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (28, 5) with action `left` toward ---> (27, 5)
cost from (28, 5) to --> (27, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 6)>, Node <(27, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (28, 5) with action `right` toward ---> (29, 5)
cost from (28, 5) to --> (29, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989

Node <(29, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>, Node <(28, 6)>, Node <(27, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (28, 5) with action `down right` toward ---> (29, 6)
cost from (28, 5) to --> (29, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(29, 5)>, Node <(28, 6)>, Node <(27, 5)>}]

||From utils.append() method: we push the Node <(29, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 3)> Node <(12, 6)> Node <(28, 6)> Node <(22, 4)> Node <(23, 4)> Node <(5, 2)> Node <(9, 1)> Node <(22, 2)> Node <(29, 5)>

||From utils.append() method: we push the Node <(29, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 3)> Node <(12, 6)> Node <(28, 6)> Node <(22, 4)> Node <(29, 6)> Node <(5, 2)> Node <(9, 1)> Node <(22, 2)> Node <(29, 5)> Node <(23, 4)>


||From utils.pop() method: we pop() Node <(22, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(22, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (22, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (22, 3) are: ['up', 'down', 'left', 'right', 'up right', 'down right']
The successors of the (22, 3) are ['up', 'down', 'left', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (22, 3) with action `up` toward ---> (22, 2)
cost from (22, 3) to --> (22, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 2) is = 10.816653826391969


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 2) is = 10.816653826391969

Node <(22, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (22, 3) with action `down` toward ---> (22, 4)
cost from (22, 3) to --> (22, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104

Node <(22, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 4)>, Node <(22, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (22, 3) with action `left` toward ---> (21, 3)
cost from (22, 3) to --> (21, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 3) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 3) is = 11.180339887498949

Node <(21, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 4)>, Node <(21, 3)>, Node <(22, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (22, 3) with action `right` toward ---> (23, 3)
cost from (22, 3) to --> (23, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603

Node <(23, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 3)>, Node <(22, 4)>, Node <(21, 3)>, Node <(22, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (22, 3) with action `up right` toward ---> (23, 2)
cost from (22, 3) to --> (23, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 2) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 2) is = 10.0

Node <(23, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 4)>, Node <(23, 3)>, Node <(21, 3)>, Node <(22, 2)>, Node <(23, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (22, 3) with action `down right` toward ---> (23, 4)
cost from (22, 3) to --> (23, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916

Node <(23, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 4)>, Node <(22, 4)>, Node <(23, 3)>, Node <(21, 3)>, Node <(22, 2)>, Node <(23, 2)>}]

||From utils.append() method: we push the Node <(23, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 6)> Node <(12, 6)> Node <(5, 2)> Node <(22, 4)> Node <(23, 3)> Node <(23, 4)> Node <(9, 1)> Node <(22, 2)> Node <(29, 5)> Node <(29, 6)>

||From utils.append() method: we push the Node <(23, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 6)> Node <(12, 6)> Node <(5, 2)> Node <(22, 4)> Node <(23, 3)> Node <(23, 4)> Node <(9, 1)> Node <(22, 2)> Node <(29, 5)> Node <(29, 6)> Node <(23, 2)>

||From utils.append() method: we push the Node <(23, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 6)> Node <(12, 6)> Node <(5, 2)> Node <(22, 4)> Node <(23, 3)> Node <(9, 1)> Node <(22, 2)> Node <(29, 5)> Node <(29, 6)> Node <(23, 2)> Node <(23, 4)>


||From utils.pop() method: we pop() Node <(28, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(28, 6)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (28, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (28, 6) are: ['up', 'down', 'right', 'up left', 'up right', 'down right']
The successors of the (28, 6) are ['up', 'down', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (28, 6) with action `up` toward ---> (28, 5)
cost from (28, 6) to --> (28, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285

Node <(28, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (28, 6) with action `down` toward ---> (28, 7)
cost from (28, 6) to --> (28, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 3.1622776601683795

Node <(28, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(28, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (28, 6) with action `right` toward ---> (29, 6)
cost from (28, 6) to --> (29, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(29, 6)>, Node <(28, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (28, 6) with action `up left` toward ---> (27, 5)
cost from (28, 6) to --> (27, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 5) is = 5.0

Node <(27, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(29, 6)>, Node <(28, 7)>, Node <(27, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (28, 6) with action `up right` toward ---> (29, 5)
cost from (28, 6) to --> (29, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989

Node <(29, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>, Node <(28, 5)>, Node <(27, 5)>, Node <(29, 6)>, Node <(28, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (28, 6) with action `down right` toward ---> (29, 7)
cost from (28, 6) to --> (29, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979

Node <(29, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(29, 5)>, Node <(28, 5)>, Node <(27, 5)>, Node <(29, 6)>, Node <(28, 7)>}]

||From utils.append() method: we push the Node <(28, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(12, 6)> Node <(23, 3)> Node <(5, 2)> Node <(22, 4)> Node <(23, 4)> Node <(9, 1)> Node <(22, 2)> Node <(29, 5)> Node <(29, 6)> Node <(23, 2)> Node <(28, 7)>

||From utils.append() method: we push the Node <(29, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(12, 6)> Node <(23, 3)> Node <(5, 2)> Node <(22, 4)> Node <(23, 4)> Node <(29, 7)> Node <(22, 2)> Node <(29, 5)> Node <(29, 6)> Node <(23, 2)> Node <(28, 7)> Node <(9, 1)>


||From utils.pop() method: we pop() Node <(12, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(12, 6)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (12, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (12, 6) are: ['up', 'right', 'up right']
The successors of the (12, 6) are ['up', 'right', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (12, 6) with action `up` toward ---> (12, 5)
cost from (12, 6) to --> (12, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (12, 5) is = 19.235384061671343

Node <(12, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (12, 6) with action `right` toward ---> (13, 6)
cost from (12, 6) to --> (13, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 6) is = 18.110770276274835

Node <(13, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 5)>, Node <(13, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (12, 6) with action `up right` toward ---> (13, 5)
cost from (12, 6) to --> (13, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (13, 5) is = 18.24828759089466

Node <(13, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(12, 5)>, Node <(13, 5)>, Node <(13, 6)>}]


||From utils.pop() method: we pop() Node <(23, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(23, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (10, 2)
In the expand () method of the model now, we have this state: (23, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down right` hits the obstacle
Generated actions to generate the successors of the (23, 3) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left']
The successors of the (23, 3) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (23, 3) with action `up` toward ---> (23, 2)
cost from (23, 3) to --> (23, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 2) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 2) is = 10.0

Node <(23, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (23, 3) with action `down` toward ---> (23, 4)
cost from (23, 3) to --> (23, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916

Node <(23, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (23, 3) with action `left` toward ---> (22, 3)
cost from (23, 3) to --> (22, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987

Node <(22, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(23, 4)>, Node <(22, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (23, 3) with action `right` toward ---> (24, 3)
cost from (23, 3) to --> (24, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 3) is = 8.602325267042627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 3) is = 8.602325267042627

Node <(24, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(24, 3)>, Node <(23, 4)>, Node <(22, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (23, 3) with action `up left` toward ---> (22, 2)
cost from (23, 3) to --> (22, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 2) is = 10.816653826391969


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 2) is = 10.816653826391969

Node <(22, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(24, 3)>, Node <(23, 4)>, Node <(22, 3)>, Node <(22, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (23, 3) with action `up right` toward ---> (24, 2)
cost from (23, 3) to --> (24, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 2) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 2) is = 9.219544457292887

Node <(24, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(24, 3)>, Node <(23, 4)>, Node <(24, 2)>, Node <(22, 3)>, Node <(22, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (23, 3) with action `down left` toward ---> (22, 4)
cost from (23, 3) to --> (22, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104

Node <(22, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(24, 3)>, Node <(23, 4)>, Node <(24, 2)>, Node <(22, 4)>, Node <(22, 3)>, Node <(22, 2)>}]

||From utils.append() method: we push the Node <(24, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 2)> Node <(22, 4)> Node <(29, 7)> Node <(29, 6)> Node <(24, 3)> Node <(28, 7)> Node <(22, 2)> Node <(29, 5)> Node <(9, 1)> Node <(23, 2)> Node <(23, 4)>

||From utils.append() method: we push the Node <(24, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(5, 2)> Node <(22, 4)> Node <(29, 7)> Node <(29, 6)> Node <(24, 3)> Node <(28, 7)> Node <(22, 2)> Node <(29, 5)> Node <(9, 1)> Node <(23, 2)> Node <(23, 4)> Node <(24, 2)>


||From utils.pop() method: we pop() Node <(5, 2)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(5, 2)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (10, 2)
In the expand () method of the model now, we have this state: (5, 2)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`right` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (5, 2) are: ['up', 'down', 'up right', 'down right']
The successors of the (5, 2) are ['up', 'down', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (5, 2) with action `up` toward ---> (5, 1)
cost from (5, 2) to --> (5, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 1) is = 26.92582403567252


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 1) is = 26.92582403567252

Node <(5, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (5, 2) with action `down` toward ---> (5, 3)
cost from (5, 2) to --> (5, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (5, 3) is = 26.476404589747453

Node <(5, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>, Node <(5, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (5, 2) with action `up right` toward ---> (6, 1)
cost from (5, 2) to --> (6, 1) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 1) is = 25.96150997149434


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 1) is = 25.96150997149434

Node <(6, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>, Node <(6, 1)>, Node <(5, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (5, 2) with action `down right` toward ---> (6, 3)
cost from (5, 2) to --> (6, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (6, 3) is = 25.495097567963924

Node <(6, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(5, 3)>, Node <(6, 3)>, Node <(6, 1)>, Node <(5, 1)>}]

||From utils.append() method: we push the Node <(5, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 4)> Node <(29, 6)> Node <(29, 7)> Node <(29, 5)> Node <(24, 3)> Node <(28, 7)> Node <(22, 2)> Node <(24, 2)> Node <(9, 1)> Node <(23, 2)> Node <(23, 4)> Node <(5, 1)>

||From utils.append() method: we push the Node <(6, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(22, 4)> Node <(29, 6)> Node <(29, 7)> Node <(29, 5)> Node <(24, 3)> Node <(28, 7)> Node <(22, 2)> Node <(24, 2)> Node <(9, 1)> Node <(23, 2)> Node <(23, 4)> Node <(5, 1)> Node <(6, 1)>


||From utils.pop() method: we pop() Node <(22, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(22, 4)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (10, 2)
In the expand () method of the model now, we have this state: (22, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (22, 4) are: ['up', 'down', 'right', 'up left', 'up right', 'down right']
The successors of the (22, 4) are ['up', 'down', 'right', 'up left', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (22, 4) with action `up` toward ---> (22, 3)
cost from (22, 4) to --> (22, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987

Node <(22, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (22, 4) with action `down` toward ---> (22, 5)
cost from (22, 4) to --> (22, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138

Node <(22, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 3)>, Node <(22, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (22, 4) with action `right` toward ---> (23, 4)
cost from (22, 4) to --> (23, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916

Node <(23, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(22, 3)>, Node <(22, 5)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (22, 4) with action `up left` toward ---> (21, 3)
cost from (22, 4) to --> (21, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 3) is = 11.180339887498949


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (21, 3) is = 11.180339887498949

Node <(21, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 3)>, Node <(22, 3)>, Node <(22, 5)>, Node <(23, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (22, 4) with action `up right` toward ---> (23, 3)
cost from (22, 4) to --> (23, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603

Node <(23, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 3)>, Node <(23, 4)>, Node <(23, 3)>, Node <(22, 3)>, Node <(22, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (22, 4) with action `down right` toward ---> (23, 5)
cost from (22, 4) to --> (23, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753

Node <(23, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(21, 3)>, Node <(23, 4)>, Node <(23, 3)>, Node <(22, 3)>, Node <(22, 5)>, Node <(23, 5)>}]


||From utils.pop() method: we pop() Node <(29, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(29, 6)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (10, 2)
In the expand () method of the model now, we have this state: (29, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (29, 6) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (29, 6) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (29, 6) with action `up` toward ---> (29, 5)
cost from (29, 6) to --> (29, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989

Node <(29, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (29, 6) with action `down` toward ---> (29, 7)
cost from (29, 6) to --> (29, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979

Node <(29, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>, Node <(29, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (29, 6) with action `left` toward ---> (28, 6)
cost from (29, 6) to --> (28, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>, Node <(29, 7)>, Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (29, 6) with action `right` toward ---> (30, 6)
cost from (29, 6) to --> (30, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979

Node <(30, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 6)>, Node <(29, 5)>, Node <(29, 7)>, Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (29, 6) with action `up left` toward ---> (28, 5)
cost from (29, 6) to --> (28, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285

Node <(28, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 6)>, Node <(29, 5)>, Node <(29, 7)>, Node <(28, 6)>, Node <(28, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (29, 6) with action `up right` toward ---> (30, 5)
cost from (29, 6) to --> (30, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 5) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 5) is = 3.1622776601683795

Node <(30, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 6)>, Node <(29, 5)>, Node <(29, 7)>, Node <(28, 6)>, Node <(30, 5)>, Node <(28, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (29, 6) with action `down left` toward ---> (28, 7)
cost from (29, 6) to --> (28, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 3.1622776601683795

Node <(28, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 6)>, Node <(29, 5)>, Node <(29, 7)>, Node <(28, 6)>, Node <(28, 7)>, Node <(30, 5)>, Node <(28, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (29, 6) with action `down right` toward ---> (30, 7)
cost from (29, 6) to --> (30, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951

Node <(30, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 6)>, Node <(30, 7)>, Node <(29, 5)>, Node <(29, 7)>, Node <(28, 6)>, Node <(28, 7)>, Node <(30, 5)>, Node <(28, 5)>}]

||From utils.append() method: we push the Node <(30, 6)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(24, 3)> Node <(29, 5)> Node <(29, 7)> Node <(9, 1)> Node <(23, 4)> Node <(28, 7)> Node <(22, 2)> Node <(24, 2)> Node <(5, 1)> Node <(23, 2)> Node <(6, 1)> Node <(30, 6)>

||From utils.append() method: we push the Node <(30, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(24, 3)> Node <(29, 5)> Node <(29, 7)> Node <(9, 1)> Node <(23, 4)> Node <(28, 7)> Node <(22, 2)> Node <(24, 2)> Node <(5, 1)> Node <(23, 2)> Node <(6, 1)> Node <(30, 6)> Node <(30, 5)>

||From utils.append() method: we push the Node <(30, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(24, 3)> Node <(29, 5)> Node <(29, 7)> Node <(9, 1)> Node <(23, 4)> Node <(28, 7)> Node <(30, 7)> Node <(24, 2)> Node <(5, 1)> Node <(23, 2)> Node <(6, 1)> Node <(30, 6)> Node <(30, 5)> Node <(22, 2)>


||From utils.pop() method: we pop() Node <(24, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(24, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (10, 2)
In the expand () method of the model now, we have this state: (24, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (24, 3) are: ['up', 'left', 'right', 'up left', 'up right', 'down left']
The successors of the (24, 3) are ['up', 'left', 'right', 'up left', 'up right', 'down left']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (24, 3) with action `up` toward ---> (24, 2)
cost from (24, 3) to --> (24, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 2) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 2) is = 9.219544457292887

Node <(24, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (24, 3) with action `left` toward ---> (23, 3)
cost from (24, 3) to --> (23, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603

Node <(23, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 2)>, Node <(23, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (24, 3) with action `right` toward ---> (25, 3)
cost from (24, 3) to --> (25, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 3) is = 7.810249675906654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 3) is = 7.810249675906654

Node <(25, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 3)>, Node <(24, 2)>, Node <(23, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (24, 3) with action `up left` toward ---> (23, 2)
cost from (24, 3) to --> (23, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 2) is = 10.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 2) is = 10.0

Node <(23, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 3)>, Node <(23, 2)>, Node <(24, 2)>, Node <(23, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (24, 3) with action `up right` toward ---> (25, 2)
cost from (24, 3) to --> (25, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 2) is = 8.48528137423857


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 2) is = 8.48528137423857

Node <(25, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(25, 2)>, Node <(24, 2)>, Node <(23, 3)>, Node <(25, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (24, 3) with action `down left` toward ---> (23, 4)
cost from (24, 3) to --> (23, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 4) is = 8.94427190999916

Node <(23, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 2)>, Node <(23, 4)>, Node <(25, 2)>, Node <(24, 2)>, Node <(23, 3)>, Node <(25, 3)>}]

||From utils.append() method: we push the Node <(25, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(29, 5)> Node <(23, 4)> Node <(29, 7)> Node <(9, 1)> Node <(6, 1)> Node <(28, 7)> Node <(25, 3)> Node <(24, 2)> Node <(5, 1)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(30, 5)> Node <(30, 7)>

||From utils.append() method: we push the Node <(25, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(29, 5)> Node <(23, 4)> Node <(29, 7)> Node <(9, 1)> Node <(6, 1)> Node <(28, 7)> Node <(25, 3)> Node <(24, 2)> Node <(5, 1)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(30, 5)> Node <(30, 7)> Node <(25, 2)>


||From utils.pop() method: we pop() Node <(29, 5)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(29, 5)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (29, 5)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`up left` hits the obstacle
Generated actions to generate the successors of the (29, 5) are: ['down', 'left', 'right', 'up right', 'down left', 'down right']
The successors of the (29, 5) are ['down', 'left', 'right', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (29, 5) with action `down` toward ---> (29, 6)
cost from (29, 5) to --> (29, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (29, 5) with action `left` toward ---> (28, 5)
cost from (29, 5) to --> (28, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 5) is = 4.242640687119285

Node <(28, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 5)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (29, 5) with action `right` toward ---> (30, 5)
cost from (29, 5) to --> (30, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 5) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 5) is = 3.1622776601683795

Node <(30, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>, Node <(28, 5)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (29, 5) with action `up right` toward ---> (30, 4)
cost from (29, 5) to --> (30, 4) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 4) is = 4.123105625617661


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 4) is = 4.123105625617661

Node <(30, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>, Node <(28, 5)>, Node <(30, 4)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (29, 5) with action `down left` toward ---> (28, 6)
cost from (29, 5) to --> (28, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(28, 5)>, Node <(28, 6)>, Node <(30, 4)>, Node <(30, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (29, 5) with action `down right` toward ---> (30, 6)
cost from (29, 5) to --> (30, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979

Node <(30, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(30, 6)>, Node <(28, 5)>, Node <(28, 6)>, Node <(30, 4)>, Node <(30, 5)>}]

||From utils.append() method: we push the Node <(30, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(29, 7)> Node <(23, 4)> Node <(25, 3)> Node <(9, 1)> Node <(6, 1)> Node <(28, 7)> Node <(30, 7)> Node <(24, 2)> Node <(5, 1)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(25, 2)> Node <(30, 5)>

||From utils.append() method: we push the Node <(30, 4)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(29, 7)> Node <(23, 4)> Node <(25, 3)> Node <(9, 1)> Node <(6, 1)> Node <(28, 7)> Node <(30, 7)> Node <(24, 2)> Node <(5, 1)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(25, 2)> Node <(30, 5)> Node <(30, 4)>


||From utils.pop() method: we pop() Node <(29, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(29, 7)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (29, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
Generated actions to generate the successors of the (29, 7) are: ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']
The successors of the (29, 7) are ['up', 'down', 'left', 'right', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (29, 7) with action `up` toward ---> (29, 6)
cost from (29, 7) to --> (29, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (29, 7) with action `down` toward ---> (29, 8)
cost from (29, 7) to --> (29, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0

Node <(29, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(29, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (29, 7) with action `left` toward ---> (28, 7)
cost from (29, 7) to --> (28, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 7) is = 3.1622776601683795

Node <(28, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(28, 7)>, Node <(29, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (29, 7) with action `right` toward ---> (30, 7)
cost from (29, 7) to --> (30, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951

Node <(30, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 6)>, Node <(28, 7)>, Node <(29, 8)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (29, 7) with action `up left` toward ---> (28, 6)
cost from (29, 7) to --> (28, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(29, 6)>, Node <(28, 7)>, Node <(28, 6)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (29, 7) with action `up right` toward ---> (30, 6)
cost from (29, 7) to --> (30, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979

Node <(30, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(29, 6)>, Node <(28, 7)>, Node <(28, 6)>, Node <(30, 6)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (29, 7) with action `down left` toward ---> (28, 8)
cost from (29, 7) to --> (28, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 8) is = 3.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 8) is = 3.0

Node <(28, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(29, 6)>, Node <(28, 7)>, Node <(28, 6)>, Node <(28, 8)>, Node <(30, 6)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (29, 7) with action `down right` toward ---> (30, 8)
cost from (29, 7) to --> (30, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 8) is = 1.0

Node <(30, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(29, 6)>, Node <(28, 7)>, Node <(28, 6)>, Node <(28, 8)>, Node <(30, 6)>, Node <(30, 8)>, Node <(30, 7)>}]

||From utils.append() method: we push the Node <(29, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 4)> Node <(9, 1)> Node <(25, 3)> Node <(5, 1)> Node <(6, 1)> Node <(28, 7)> Node <(30, 7)> Node <(24, 2)> Node <(30, 4)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(25, 2)> Node <(30, 5)> Node <(29, 8)>

||From utils.append() method: we push the Node <(28, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 4)> Node <(9, 1)> Node <(25, 3)> Node <(5, 1)> Node <(6, 1)> Node <(28, 7)> Node <(30, 7)> Node <(24, 2)> Node <(30, 4)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(25, 2)> Node <(30, 5)> Node <(29, 8)> Node <(28, 8)>

||From utils.append() method: we push the Node <(30, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(23, 4)> Node <(9, 1)> Node <(25, 3)> Node <(30, 8)> Node <(6, 1)> Node <(28, 7)> Node <(30, 7)> Node <(5, 1)> Node <(30, 4)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(25, 2)> Node <(30, 5)> Node <(29, 8)> Node <(28, 8)> Node <(24, 2)>


||From utils.pop() method: we pop() Node <(23, 4)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(23, 4)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (23, 4)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
Generated actions to generate the successors of the (23, 4) are: ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']
The successors of the (23, 4) are ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (23, 4) with action `up` toward ---> (23, 3)
cost from (23, 4) to --> (23, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 3) is = 9.433981132056603

Node <(23, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (23, 4) with action `down` toward ---> (23, 5)
cost from (23, 4) to --> (23, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (23, 5) is = 8.54400374531753

Node <(23, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(23, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (23, 4) with action `left` toward ---> (22, 4)
cost from (23, 4) to --> (22, 4) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 4) is = 9.848857801796104

Node <(22, 4)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(23, 3)>, Node <(22, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (23, 4) with action `up left` toward ---> (22, 3)
cost from (23, 4) to --> (22, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 3) is = 10.295630140987

Node <(22, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(23, 3)>, Node <(22, 3)>, Node <(22, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (23, 4) with action `up right` toward ---> (24, 3)
cost from (23, 4) to --> (24, 3) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 3) is = 8.602325267042627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 3) is = 8.602325267042627

Node <(24, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(23, 3)>, Node <(22, 3)>, Node <(24, 3)>, Node <(22, 4)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (23, 4) with action `down left` toward ---> (22, 5)
cost from (23, 4) to --> (22, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (22, 5) is = 9.486832980505138

Node <(22, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(23, 3)>, Node <(22, 3)>, Node <(24, 3)>, Node <(22, 4)>, Node <(22, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (23, 4) with action `down right` toward ---> (24, 5)
cost from (23, 4) to --> (24, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 5) is = 7.615773105863909

Node <(24, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(23, 5)>, Node <(24, 5)>, Node <(23, 3)>, Node <(22, 3)>, Node <(24, 3)>, Node <(22, 4)>, Node <(22, 5)>}]


||From utils.pop() method: we pop() Node <(9, 1)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(9, 1)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (9, 1) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (9, 1)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up` hits the obstacle
`down` hits the obstacle
`up left` hits the obstacle
`up right` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (9, 1) are: ['left', 'right', 'down right']
The successors of the (9, 1) are ['left', 'right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (9, 1) with action `left` toward ---> (8, 1)
cost from (9, 1) to --> (8, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 1) is = 24.041630560342615


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (8, 1) is = 24.041630560342615

Node <(8, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (9, 1) with action `right` toward ---> (10, 1)
cost from (9, 1) to --> (10, 1) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 1) is = 22.135943621178654

Node <(10, 1)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 1)>, Node <(10, 1)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (9, 1) with action `down right` toward ---> (10, 2)
cost from (9, 1) to --> (10, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (10, 2) is = 21.840329667841555

Node <(10, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(8, 1)>, Node <(10, 2)>, Node <(10, 1)>}]

||From utils.append() method: we push the Node <(8, 1)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(25, 3)> Node <(30, 8)> Node <(30, 7)> Node <(5, 1)> Node <(6, 1)> Node <(28, 7)> Node <(30, 5)> Node <(24, 2)> Node <(30, 4)> Node <(23, 2)> Node <(22, 2)> Node <(30, 6)> Node <(25, 2)> Node <(28, 8)> Node <(29, 8)> Node <(8, 1)>


||From utils.pop() method: we pop() Node <(25, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(25, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (25, 3) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (9, 1) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (25, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (25, 3) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (25, 3) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (25, 3) with action `up` toward ---> (25, 2)
cost from (25, 3) to --> (25, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 2) is = 8.48528137423857


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 2) is = 8.48528137423857

Node <(25, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (25, 3) with action `left` toward ---> (24, 3)
cost from (25, 3) to --> (24, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 3) is = 8.602325267042627


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 3) is = 8.602325267042627

Node <(24, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 3)>, Node <(25, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (25, 3) with action `right` toward ---> (26, 3)
cost from (25, 3) to --> (26, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 3) is = 7.0710678118654755


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 3) is = 7.0710678118654755

Node <(26, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 3)>, Node <(26, 3)>, Node <(25, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (25, 3) with action `up left` toward ---> (24, 2)
cost from (25, 3) to --> (24, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 2) is = 9.219544457292887


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (24, 2) is = 9.219544457292887

Node <(24, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(24, 3)>, Node <(26, 3)>, Node <(24, 2)>, Node <(25, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (25, 3) with action `up right` toward ---> (26, 2)
cost from (25, 3) to --> (26, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 2) is = 7.810249675906654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 2) is = 7.810249675906654

Node <(26, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 2)>, Node <(24, 3)>, Node <(24, 2)>, Node <(26, 3)>, Node <(26, 2)>}]

||From utils.append() method: we push the Node <(26, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(30, 7)> Node <(26, 3)> Node <(28, 7)> Node <(30, 8)> Node <(6, 1)> Node <(30, 6)> Node <(30, 5)> Node <(5, 1)> Node <(30, 4)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(25, 2)> Node <(28, 8)> Node <(29, 8)> Node <(24, 2)>

||From utils.append() method: we push the Node <(26, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(30, 7)> Node <(26, 3)> Node <(28, 7)> Node <(30, 8)> Node <(6, 1)> Node <(30, 6)> Node <(30, 5)> Node <(5, 1)> Node <(30, 4)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(25, 2)> Node <(28, 8)> Node <(29, 8)> Node <(24, 2)> Node <(26, 2)>


||From utils.pop() method: we pop() Node <(30, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(30, 7)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (30, 7) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (25, 3) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (9, 1) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (30, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`up right` hits the obstacle
Generated actions to generate the successors of the (30, 7) are: ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']
The successors of the (30, 7) are ['up', 'down', 'left', 'right', 'up left', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (30, 7) with action `up` toward ---> (30, 6)
cost from (30, 7) to --> (30, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 6) is = 2.23606797749979

Node <(30, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (30, 7) with action `down` toward ---> (30, 8)
cost from (30, 7) to --> (30, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 8) is = 1.0

Node <(30, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 6)>, Node <(30, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (30, 7) with action `left` toward ---> (29, 7)
cost from (30, 7) to --> (29, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979

Node <(29, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(30, 6)>, Node <(30, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (30, 7) with action `right` toward ---> (31, 7)
cost from (30, 7) to --> (31, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 7) is = 1.0

Node <(31, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(31, 7)>, Node <(29, 7)>, Node <(30, 6)>, Node <(30, 8)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (30, 7) with action `up left` toward ---> (29, 6)
cost from (30, 7) to --> (29, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(31, 7)>, Node <(30, 6)>, Node <(30, 8)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (30, 7) with action `down left` toward ---> (29, 8)
cost from (30, 7) to --> (29, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0

Node <(29, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(31, 7)>, Node <(29, 8)>, Node <(30, 6)>, Node <(30, 8)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (30, 7) with action `down right` toward ---> (31, 8)
cost from (30, 7) to --> (31, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 8) is = 0.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 8) is = 0.0

Node <(31, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(31, 7)>, Node <(29, 8)>, Node <(30, 6)>, Node <(30, 8)>, Node <(31, 8)>, Node <(29, 6)>}]

||From utils.append() method: we push the Node <(31, 7)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 7)> Node <(26, 3)> Node <(30, 6)> Node <(30, 8)> Node <(6, 1)> Node <(25, 2)> Node <(30, 5)> Node <(31, 7)> Node <(30, 4)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(26, 2)> Node <(28, 8)> Node <(29, 8)> Node <(24, 2)> Node <(5, 1)>

||From utils.append() method: we push the Node <(31, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(28, 7)> Node <(26, 3)> Node <(30, 6)> Node <(30, 8)> Node <(6, 1)> Node <(25, 2)> Node <(30, 5)> Node <(31, 7)> Node <(31, 8)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(26, 2)> Node <(28, 8)> Node <(29, 8)> Node <(24, 2)> Node <(5, 1)> Node <(30, 4)>


||From utils.pop() method: we pop() Node <(28, 7)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(28, 7)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (30, 7) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (25, 3) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (28, 7) (9, 6) (6, 5) (5, 3) (29, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (9, 1) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (28, 7)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`left` hits the obstacle
`up left` hits the obstacle
`down left` hits the obstacle
Generated actions to generate the successors of the (28, 7) are: ['up', 'down', 'right', 'up right', 'down right']
The successors of the (28, 7) are ['up', 'down', 'right', 'up right', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (28, 7) with action `up` toward ---> (28, 6)
cost from (28, 7) to --> (28, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 6) is = 3.605551275463989

Node <(28, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (28, 7) with action `down` toward ---> (28, 8)
cost from (28, 7) to --> (28, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 8) is = 3.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (28, 8) is = 3.0

Node <(28, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(28, 8)>, Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (28, 7) with action `right` toward ---> (29, 7)
cost from (28, 7) to --> (29, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979

Node <(29, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(28, 8)>, Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (28, 7) with action `up right` toward ---> (29, 6)
cost from (28, 7) to --> (29, 6) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(28, 8)>, Node <(29, 6)>, Node <(28, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (28, 7) with action `down right` toward ---> (29, 8)
cost from (28, 7) to --> (29, 8) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0

Node <(29, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 7)>, Node <(28, 8)>, Node <(29, 6)>, Node <(28, 6)>, Node <(29, 8)>}]

||From utils.append() method: we push the Node <(28, 8)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(30, 6)> Node <(26, 3)> Node <(30, 5)> Node <(30, 8)> Node <(6, 1)> Node <(25, 2)> Node <(29, 8)> Node <(31, 7)> Node <(31, 8)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(26, 2)> Node <(30, 4)> Node <(24, 2)> Node <(5, 1)> Node <(28, 8)>


||From utils.pop() method: we pop() Node <(30, 6)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(30, 6)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (30, 7) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (25, 3) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (28, 7) (9, 6) (6, 5) (5, 3) (29, 6) (30, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (9, 1) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (30, 6)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`right` hits the obstacle
Generated actions to generate the successors of the (30, 6) are: ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']
The successors of the (30, 6) are ['up', 'down', 'left', 'up left', 'up right', 'down left', 'down right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (30, 6) with action `up` toward ---> (30, 5)
cost from (30, 6) to --> (30, 5) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 5) is = 3.1622776601683795


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 5) is = 3.1622776601683795

Node <(30, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down` action:||
=======================================================================
From (30, 6) with action `down` toward ---> (30, 7)
cost from (30, 6) to --> (30, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951

Node <(30, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (30, 6) with action `left` toward ---> (29, 6)
cost from (30, 6) to --> (29, 6) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 6) is = 2.8284271247461903

Node <(29, 6)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>, Node <(30, 7)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (30, 6) with action `up left` toward ---> (29, 5)
cost from (30, 6) to --> (29, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 5) is = 3.605551275463989

Node <(29, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 5)>, Node <(30, 5)>, Node <(30, 7)>, Node <(29, 6)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (30, 6) with action `up right` toward ---> (31, 5)
cost from (30, 6) to --> (31, 5) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 5) is = 3.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 5) is = 3.0

Node <(31, 5)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>, Node <(30, 7)>, Node <(29, 5)>, Node <(29, 6)>, Node <(31, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down left` action:||
=======================================================================
From (30, 6) with action `down left` toward ---> (29, 7)
cost from (30, 6) to --> (29, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979

Node <(29, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>, Node <(30, 7)>, Node <(29, 5)>, Node <(29, 7)>, Node <(29, 6)>, Node <(31, 5)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `down right` action:||
=======================================================================
From (30, 6) with action `down right` toward ---> (31, 7)
cost from (30, 6) to --> (31, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 7) is = 1.0

Node <(31, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 5)>, Node <(30, 7)>, Node <(29, 5)>, Node <(29, 7)>, Node <(31, 7)>, Node <(29, 6)>, Node <(31, 5)>}]

||From utils.append() method: we push the Node <(31, 5)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(26, 3)> Node <(30, 8)> Node <(30, 5)> Node <(31, 8)> Node <(6, 1)> Node <(25, 2)> Node <(29, 8)> Node <(31, 7)> Node <(28, 8)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(26, 2)> Node <(30, 4)> Node <(24, 2)> Node <(5, 1)> Node <(31, 5)>


||From utils.pop() method: we pop() Node <(26, 3)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(26, 3)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (30, 7) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (25, 3) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (26, 3) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (28, 7) (9, 6) (6, 5) (5, 3) (29, 6) (30, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (9, 1) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (26, 3)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (26, 3) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (26, 3) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (26, 3) with action `up` toward ---> (26, 2)
cost from (26, 3) to --> (26, 2) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 2) is = 7.810249675906654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (26, 2) is = 7.810249675906654

Node <(26, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(26, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (26, 3) with action `left` toward ---> (25, 3)
cost from (26, 3) to --> (25, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 3) is = 7.810249675906654


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 3) is = 7.810249675906654

Node <(25, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 3)>, Node <(26, 2)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (26, 3) with action `right` toward ---> (27, 3)
cost from (26, 3) to --> (27, 3) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 3) is = 6.4031242374328485


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 3) is = 6.4031242374328485

Node <(27, 3)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 3)>, Node <(26, 2)>, Node <(27, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (26, 3) with action `up left` toward ---> (25, 2)
cost from (26, 3) to --> (25, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 2) is = 8.48528137423857


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (25, 2) is = 8.48528137423857

Node <(25, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 3)>, Node <(26, 2)>, Node <(25, 2)>, Node <(27, 3)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (26, 3) with action `up right` toward ---> (27, 2)
cost from (26, 3) to --> (27, 2) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 2) is = 7.211102550927978


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (27, 2) is = 7.211102550927978

Node <(27, 2)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(25, 3)>, Node <(27, 3)>, Node <(26, 2)>, Node <(27, 2)>, Node <(25, 2)>}]

||From utils.append() method: we push the Node <(27, 3)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(30, 8)> Node <(31, 8)> Node <(30, 5)> Node <(31, 7)> Node <(6, 1)> Node <(25, 2)> Node <(29, 8)> Node <(27, 3)> Node <(28, 8)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(26, 2)> Node <(30, 4)> Node <(24, 2)> Node <(31, 5)> Node <(5, 1)>

||From utils.append() method: we push the Node <(27, 2)> to OPEN list in the queue now||

This is the OPEN list in the utils:
Node <(30, 8)> Node <(31, 8)> Node <(30, 5)> Node <(31, 7)> Node <(6, 1)> Node <(25, 2)> Node <(29, 8)> Node <(27, 3)> Node <(28, 8)> Node <(23, 2)> Node <(22, 2)> Node <(8, 1)> Node <(26, 2)> Node <(30, 4)> Node <(24, 2)> Node <(31, 5)> Node <(5, 1)> Node <(27, 2)>


||From utils.pop() method: we pop() Node <(30, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(30, 8)>

CLOSED List in traditional has these nodes: (16, 6) (7, 3) (12, 1) (17, 7) (14, 4) (13, 4) (20, 7) (22, 6) (26, 6) (8, 5) (23, 7) (5, 8) (28, 5) (10, 8) (6, 7) (5, 5) (7, 6) (16, 3) (30, 7) (12, 6) (19, 3) (15, 4) (22, 3) (9, 3) (7, 5) (7, 8) (14, 8) (12, 8) (17, 8) (24, 8) (20, 3) (25, 5) (23, 3) (16, 7) (12, 2) (14, 5) (13, 3) (18, 5) (24, 5) (21, 8) (26, 8) (22, 7) (27, 5) (26, 7) (8, 6) (23, 6) (28, 6) (9, 7) (6, 4) (5, 4) (29, 7) (16, 4) (14, 6) (13, 6) (18, 6) (15, 7) (20, 5) (25, 3) (8, 3) (23, 5) (5, 7) (11, 3) (7, 4) (12, 4) (14, 3) (9, 8) (23, 8) (30, 8) (26, 3) (12, 3) (13, 2) (19, 6) (25, 7) (22, 4) (8, 7) (28, 7) (9, 6) (6, 5) (5, 3) (29, 6) (30, 6) (10, 5) (6, 8) (11, 8) (16, 8) (13, 5) (19, 5) (18, 7) (15, 6) (24, 3) (20, 6) (21, 7) (8, 4) (23, 4) (9, 1) (6, 6) (5, 6) (11, 2) (10, 6) (7, 7) (12, 5) (17, 3) (15, 8) (13, 8) (20, 8) (18, 8) (25, 8) (6, 3) (11, 1) (10, 1) (13, 1) (18, 3) (25, 6) (22, 5) (21, 3) (26, 5) (8, 8) (22, 8) (9, 5) (5, 2) (29, 5) (10, 2)
In the expand () method of the model now, we have this state: (30, 8)

||I am in the main file in the action() method||
============valid and invalid moves======================================
`down` hits the obstacle
`down left` hits the obstacle
`down right` hits the obstacle
Generated actions to generate the successors of the (30, 8) are: ['up', 'left', 'right', 'up left', 'up right']
The successors of the (30, 8) are ['up', 'left', 'right', 'up left', 'up right']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up` action:||
=======================================================================
From (30, 8) with action `up` toward ---> (30, 7)
cost from (30, 8) to --> (30, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (30, 7) is = 1.4142135623730951

Node <(30, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `left` action:||
=======================================================================
From (30, 8) with action `left` toward ---> (29, 8)
cost from (30, 8) to --> (29, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 8) is = 2.0

Node <(29, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `right` action:||
=======================================================================
From (30, 8) with action `right` toward ---> (31, 8)
cost from (30, 8) to --> (31, 8) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 8) is = 0.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 8) is = 0.0

Node <(31, 8)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(31, 8)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up left` action:||
=======================================================================
From (30, 8) with action `up left` toward ---> (29, 7)
cost from (30, 8) to --> (29, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (29, 7) is = 2.23606797749979

Node <(29, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(31, 8)>, Node <(29, 7)>, Node <(30, 7)>}]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
||print from models, the expand() method for the `up right` action:||
=======================================================================
From (30, 8) with action `up right` toward ---> (31, 7)
cost from (30, 8) to --> (31, 7) is = 1.7


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 7) is = 1.0


I am in SearchNode class of the models now
I am in the SearchNodeHeuristicOrdered of the models
==============================================================
Heuristic for (31, 7) is = 1.0

Node <(31, 7)>
||print from models, the expand() method||
===========================================
Adding new successor to the list: [{Node <(29, 8)>, Node <(31, 7)>, Node <(30, 7)>, Node <(29, 7)>, Node <(31, 8)>}]


||From utils.pop() method: we pop() Node <(31, 8)> from the queue now. Returns the node to traditional.||

||print from the traditional in the _search class, fringe loop||
The node to save in the CLOSED list is Node <(31, 8)>


    ##############################
    #         #              #   #
    # ####    ########        #  #
    #    #    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #    o·     #
    #      #     #   #  #  #·  ###
    #     #####    #    #  # x   #
    #              #       #     #
    ##############################
    

    ##############################
    #         #              #   #
    # ####    ########        #  #
    #     #    #             #   #
    #    ###     #####  ######   #
    #      #   ###   #  [32m*[0m[32m*[0m[32m*[0m[32m*[0m[32m*[0m    #
    # a[32m*[0m[32m*[0m  #     # [32m*[0m[32m*[0m# [32m*[0m#  # [32m*[0m ###
    #    [32m*[0m#####   [32m*[0m# [32m*[0m[32m*[0m #  #  [32m*[0m  #
    #     [32m*[0m[32m*[0m[32m*[0m[32m*[0m[32m*[0m[32m*[0m[32m*[0m[32m*[0m #       #   b #
    ##############################
    
