from collections import defaultdict
import random

def make_matrix(rows, cols): # creates adjacency matrix in 2d grid
    n = rows*cols
    M = [[0 for x in range(n)] for y in range(n)] 
    for r in range(rows):
        for c in range(cols):
            i = r*cols + c
            # Two inner diagonals
            if c > 0: M[i-1][i] = M[i][i-1] = 1
            # Two outer diagonals
            if r > 0: M[i-cols][i] = M[i][i-cols] = 1
    return M

def convert(a): # converts from adjacency matrix to adjacency list
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
                       if a[i][j]== 1:
                           adjList[i].append(j)
    return adjList

def random_list(n):
    lst = []
    while len(lst) < n:
        rnd = random.randint(0,15)
        if rnd not in lst:
            lst.append(rnd)
    return lst


def get_all_elements_in_list_of_lists(lst):
    count = 0
    for element in lst:
        count += len(element)
    return count

def bfs(graph, data):
    n = 0
    mem = 0
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([data[0]])
    while queue:
        if get_all_elements_in_list_of_lists(queue) > mem:
            mem = get_all_elements_in_list_of_lists(queue)
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == data[1] and all(item in path for item in data[5:8]):
            path.append(mem)
            path.append(n)
            return path
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            n = n + 1
            if adjacent not in data[2:5]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

field_size = 4 # size of adjacency matrix
a = make_matrix(field_size,field_size) # adjacency matrix
##print("Adjacency Matrix:")
##for i in a: print(i)
AdjList = convert(a) # adjacency list
##
##print("Adjacency List:")
##for i in AdjList: # print the adjacency list
##    print(i, end ="")
##    for j in AdjList[i]:
##        print(" -> {}".format(j), end ="")
##    print()
nodes_data = random_list(8)
start = nodes_data[0]
end = nodes_data[1]
blocks = nodes_data[2:5]
goals = nodes_data[5:8]
bfs_result = bfs(dict(AdjList), nodes_data)
count = bfs_result.pop(-1)
memo = bfs_result.pop(-1)
trace1 = [[0 for x in range(field_size)] for y in range(field_size)]
trace2 = [[0 for x in range(field_size)] for y in range(field_size)]
x = 0
for i in range(field_size):
    for j in range(field_size):
        trace1[i][j] = x
        x += 1
print('Field: ')
for i in trace1: print(i)
x = 0
for i in range(field_size):
    for j in range(field_size):
        trace1[i][j] = '    '
        if x == blocks[0] or x == blocks[1] or x == blocks[2]:
            trace1[i][j] = ' || '
        if x == start:
            trace1[i][j] = ' ++ '
        if x == end:
            trace1[i][j] = ' -- '
        if x in goals:
            trace1[i][j] = ' ## '
        x += 1
x = 0
for i in range(field_size):
    for j in range(field_size):
        trace2[i][j] = '    '
        for k in bfs_result:
            if k == x:
                trace2[i][j] = ' OO '
        x += 1
print('Visualisation')
for i in range(field_size): print(trace1[i], '    ', trace2[i])
print('Path(oo): ',bfs_result)
print('Start(++): ', start)
print('End(--): ', end)
print('Blocks(||): ', blocks)
print('Goals(##): ', goals)
print('Maximum nodes memorized at once: ', memo)
print('Nodes opened: ', count)
