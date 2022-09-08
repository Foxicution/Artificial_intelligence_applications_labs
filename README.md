# Artificial_intelligence_applications_labs
A repository containing the practical works for the subject "artificial intelligence applications".

## Practical work no. 1: Solve the missionaries and cannibals problem using the A* algorithm.
For this I chose to generalise the problem by allowing any number of cannibals, missionaries and any size of the boat. I defined a simple heuristic function *h = (M + C)/ B* where M is the number of missionaries, C is the number of cannibals (on the left shore) and B is the boat size. Because the boat size is variable I defined a funtion to give back all the possible actions based on the boat size. This implementation is using a priority queue (priority queues are used often when implementing the A* algorithm) by using a built in Python library heapq. I chose to do a dumbed down tree construction and rely on my heuristic function to determine if the problem is solvable with the provided initial conditions. The solution can be found in the file [Astar_Missionaries_Cannibals.py](1Missionaries_Cannibals_Astar/Astar_Missionaries_Cannibals.py) and the excel workbook for constructing the algorithm can be found in the file [M_C.xlsx](1Missionaries_Cannibals_Astar/M_C.xlsx)

## Practical work no. 2: Resolution derivation rule for propositional logic sentences.
The problem is as follows: Given. The external memory (file) contains a set of propositional logic sentences - knowledge base. Sentences are written in the disjunctive form. The number of propositional logic characters, the number of sentences, and the number of disjunctions in sentences can generally vary. Write a program that, with the help of resolution rule, would derive from this knowledge base all the other sentences that can be derived. Print newly derived sentences to a file. Problem file can be found []
