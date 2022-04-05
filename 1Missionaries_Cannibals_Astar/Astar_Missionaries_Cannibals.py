#Solution to generalised missionaries and cannibals problem using A* algorithm
#Implemented with a priority queue
import heapq


#Setting parameters
number_of_missionaries = 3
number_of_cannibals = 3
boat_size = 2
expected_h = (number_of_missionaries + number_of_cannibals) / boat_size

#Calculate available actions based on boat size and append them to actions
actions = []
for n in range(boat_size):
    actions.append((n+1, 0))
    actions.append((0, n+1))
    for a in range(n):
        actions.append((n+1-(a+1)%(n+1), (a+1)))
print('Available actions:')
print(actions)

#Stack to check and checked nodes
stack = []
checked = []

#Initialise first node
missionaries = number_of_missionaries
cannibals = number_of_cannibals
boat = 'L'
parent = -1
action = -1
g = 0
h = (missionaries + cannibals)/boat_size
f = g + h

#Add the first node to the stack
heapq.heappush(stack, (f, (missionaries, cannibals, boat, parent, action, g, h)))

z = 0
#Unfold the folded node with lowest f (cost to the end)
while any(stack):
    z = z + 1
    item = heapq.heappop(stack)[1]
    #Checking ending conditions (all cannibals and missionaries tarnsported)
    if item[2] == 'R' and item[0] + item[1] == 0:
        checked.append(item)
        print('Ended after checking {0} nodes'.format(z))
        break
    #Checking if the task is solvable using the heuristic function
    if expected_h * 4 < item[5]:
        checked.append(checked[0])
        print('Ended after checking {0} nodes'.format(z))
        break
    parent = len(checked)
    checked.append(item)
    g = item[5] + 1
    boat = 'R' if item[2] == 'L' else 'L'
    for i, a in enumerate(actions):
        action = i
        #Calculating amount of missionaries and cannibals on both sides
        if boat == 'R':
            missionaries = item[0] - a[0]
            cannibals = item[1] - a[1]
            R_M = number_of_missionaries - item[0] + a[0]
            R_C = number_of_cannibals - item[1] + a[1]
        if boat == 'L':
            missionaries = item[0] + a[0]
            cannibals = item[1] + a[1]
            R_M = number_of_missionaries - item[0] - a[0]
            R_C = number_of_cannibals - item[1] - a[1]
        #Defining illegal moves
        if missionaries > number_of_missionaries:
            pass
        elif cannibals > number_of_cannibals:
            pass
        elif R_M > number_of_missionaries:
            pass
        elif R_C > number_of_cannibals:
            pass
        elif cannibals > missionaries and missionaries > 0:
            pass
        elif R_C > R_M and R_M > 0:
            pass
        #If the move is legal it is pushed into the heap (priority queue)
        else:
            h = (missionaries + cannibals)/boat_size
            f = g + h
            heapq.heappush(stack, (f,(missionaries, cannibals, boat, parent, action, g, h)))


path = []
node = checked[-1]
parent = node[3]
path.append(node)
if parent == -1:
    print('Unsolvable')
else:
    print('Recreating instructions from nodes')
    while parent != -1:
        node = checked[parent]
        parent = node[3]
        #Not including parent node since it carries no instructions
        if node[4] != -1:
            path.append(node)
            
    #Reversing the path to start from the top of the tree
    path = path[::-1]
    print('Path from nodes')
    print(path)
    
    #Printing out instructions
    print('Instructions')
    for i, node in enumerate(path):
        direction = 'right' if node[2] == 'R' else 'left'
        action = actions[node[4]]
        message = 'Move {0}: Bring {1} missionaries and {2} cannibals to the {3}'.format(
            i+1, action[0], action[1], direction)
        print(message)