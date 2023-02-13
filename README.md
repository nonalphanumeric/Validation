# Validation

## Abdulaziz Al Zahrani, Guillian Billard, Rozenn Jézégou

### Description

Our project during the third year at ENSTA Bretagne in the CSN program aimed to build a simulator for constraint programming. To achieve this goal, we carried out the following steps:

Model & Graph: Our initial objective was to create a model of a graph. To do this, we developed the DicGraph class whi is a basic implementation of a directed graph.

Next, we sought to traverse the graph using the TransitionRelation method. This was achieved by using a breadth-first search (bfs) to visit each node and mark its position in the graph.

Examples: We used two examples, nbits and hanoi, to demonstrate how the graph can be used to model different problems. In the nbits example, we modeled all binary words of a given length by only changing one bit at a time. In the hanoi example, we attempted to solve the tower of hanoi problem with varying numbers of discs and towers. The graph was used to model the transitions between configurations, with the constraint that a disk cannot be placed above a smaller disk.

Trace: The trace feature allows us to visualize transitions from one configuration to another in the command line.

Semantic: Alice & Bob: To implement transitions with conditions, we used a lambda function to represent a guard that returns a boolean value, and another lambda function to represent an action that modifies the Configuration variables. This was implemented in the semantic section.
Hanoi and NBits were also implemented in the semantic section.

Finally, we modeled the Alice & Bob example to demonstrate mutual access to a critical resource in AandB. To resolve the deadlock issue, where both Alice and Bob attempt to access the critical resource at the same time, we added a rule in the AandB_deadlock version allowing Bob to change his mind and return to his initial state.

