'''
Merge sorted files

Notes:
* what went right
    * remembered PriorityQueue API for heap implementation without having to look up
'''
from queue import PriorityQueue

def merge_sorted(t):
    q = PriorityQueue()
    n = len(t)
    # what location is currently being merged in each list
    lists_next_pos = {i : 0 for i in range(n)}
    lists_length = {i: len(t[i]) for i in range(n)}
    merged_list = []
    # seed the heap
    for i, l in enumerate(t):
        q.put((l[0], i))
        lists_next_pos[i] += 1        
    while True:
        if q.empty():
            break
        val, list_index = q.get()
        merged_list.append(val)
        if lists_next_pos[list_index] < lists_length[list_index]:
            q.put((t[list_index][lists_next_pos[list_index]], list_index))
            lists_next_pos[list_index] += 1
    return merged_list

if __name__ == '__main__':
    test_cases = [
        [
            [1,3,6,11],
            [4],
            [2,20,21],
            [3,5,7],
            [8]
        ]
    ]
    for t in test_cases:
        print(merge_sorted(t))
