'''
Notes:
* My initial approach was to use quicksort partition twice, once on array and another time on the part >= pivot. 
  Turns out I misremembered how Hoare's partitioning handles duplicates, they can go either side of the pivot. Which means
  we would end up completing the sort to satisfy the partitioning requirements.
* Used the EPI solution instead - turns out the Dutch National Flag approach is an alternative quicksort partitioning scheme 
  proposed by Djikstra (in the 90s?), so it's not something EPI authors came up with.

Bugs in quicksort partition:
* Forgot to update i and j after the swap
* Set j to n instead of n - 1
* Thought I had misremembered Hoare partitioning but turns out there is also another partitioning method (Lomuto)

'''

def swap_elements(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def quicksort_partition(arr, k):
    i = 0
    n = len(arr)
    j = n - 1
    pivot = arr[k]
    while i < j:
        # break on arr[i] >= pivot, duplicates can go on either side of the pivot in classic Hoare partitioning
        while i < n and arr[i] < pivot:
            i += 1
        # break on arr[j] <= pivot, duplicates can go on either side of pivot in classic Hoare partitioning
        while j >= 0 and arr[j] > pivot:
            j -= 1
        if i < j  and i < n and j >= 0:
            swap_elements(arr, i, j)
            i += 1
            j -= 1
    return arr, j    

def dutch_national_flag(arr, k):
    '''
    Doesn't work. Left here for illustrative purposes
    '''
    pivot = arr[k]
    arr, j = quicksort_partition(arr, k)
    quicksort_partition(arr[j:], pivot)
    return arr

def dutch_national_flag_epi(arr, k):
    n = len(arr)
    pivot = arr[k]
    '''
    Keep the following invariants during partitioning
    * bottom group: arr[0, smaller -1]
    * middle group: arr[smaller: equal - 1]
    * unclassified group: arr[equal: larger]
    * top group: arr[larger + 1: n - 1]
    '''
    smaller = equal = 0
    larger = n - 1
    while equal <= larger:
        if (arr[equal] < pivot):
            swap_elements(arr, smaller, equal)
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            swap_elements(arr, equal, larger)
            larger -= 1
    return arr

if __name__ == '__main__':
    test_cases = [
        ([3,1,4,10,1,3,1,10], 0)
    ]
    print('Quicksort Partition')
    for t in test_cases:
        print(t, quicksort_partition(t[0].copy(), t[1]))

    print('Dutch National Flag Partition')
    for t in test_cases:
        print(t, dutch_national_flag_epi(t[0].copy(), t[1]))
        print(t, dutch_national_flag(t[0].copy(), t[1]))

        
