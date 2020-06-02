'''
Given a 2D array of black and white entries representing a maze with designated entry
and exit points, find a path from the entrance to the exit if once exists.

Notes:
* Use DFS
* what went right
    * implemented DFS correctly including accounting visited nodes
* what went wrong
    * initializing a 2D array using [[0] * num_columns] * num_rows is a trap!! it creates copies of a references to the rows instead
      of allocating new rows. instead use [[0] * num_columns for i in range(num_rows)]
'''
from queue import Queue

def maze_search(maze, start, end):
    num_rows = len(maze)
    num_columns = len(maze[0])

    # initialize visited array
    visited = [[0] * num_columns for i in range(num_rows)]

    q = Queue()
    q.put(start)    
    while q.empty() == False:
        el = q.get()
        if visited[el[0]][el[1]] == 1:
            continue
        visited[el[0]][el[1]] = 1
        if el == end:
            return True
        if el[0] < num_rows - 1 and maze[el[0] + 1][el[1]] == 1:
            q.put((el[0]+1, el[1]))
        if el[1] < num_columns - 1 and maze[el[0]][el[1] + 1] == 1:
            q.put((el[0], el[1]+1))
        if el[0] > 1 and maze[el[0] - 1][el[1]] == 1:
            q.put((el[0]-1, el[1]))
        if el[1] > 1 and maze[el[0]][el[1] - 1] == 1:
            q.put((el[0], el[1]-1))
    return False
        
if __name__ == '__main__':
    test_cases = [
        ([
            [1,0,0,1],
            [1,1,1,0],
            [0,0,1,1],
            [1,1,0,1],], (0,0), (3,3)),
        ([
            [1,0,0,1],
            [1,1,1,0],
            [0,0,0,1],
            [1,1,0,1],], (0,0), (3,3)),
    ]
    for t in test_cases:
        maze, start, end = t[0], t[1], t[2]
        print(maze_search(maze, start, end))
