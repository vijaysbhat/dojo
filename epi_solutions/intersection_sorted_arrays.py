
'''
Take two sorted arrays and return a new array containing elements present in both arrays.
The result should be free of duplicates. 

Notes:
* what went right
    * reviewed the code and found a mistake of not updating prev_match
* what went wrong
    * didn't cast mid point of binary search into int so python tried to index by float
'''
def intersection_sorted_arrays_iterative(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i1 = 0
    i2 = 0
    result = []
    prev_match = None
    while i1 < n1 and i2 < n2:
        if arr1[i1] == arr2[i2]:
            if prev_match is None or prev_match != arr1[i1]:
                result.append(arr1[i1])
            prev_match = arr1[i1]
            i1 += 1
            i2 += 1
        elif arr1[i1] > arr2[i2]:
            i2 += 1
        else:
            i1 += 1
    return result



def intersection_sorted_arrays_lookup(arr1, arr2):
    def search(arr, left, right, el):
        if left > right:
            return False
        mid = int((left + right) / 2)
        if arr[mid] > el:
            return search(arr, left, mid-1, el)
        elif arr[mid] < el:
            return search(arr, mid+1, right, el)
        return True
    
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    result = []
    n2 = len(arr2)
    prev_el = None
    for el in arr1:
        if (prev_el is None or prev_el != el) and search(arr2, 0, n2-1, el):
            result.append(el)
        prev_el = el
    return result

if __name__ == '__main__':
    test_cases = [
        [[2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10]],
        [[2,3,5,7,11], [3,7,15,31]]
    ]
    for t in test_cases:
        print(t, intersection_sorted_arrays_lookup(t[0], t[1]))
        print(t, intersection_sorted_arrays_iterative(t[0], t[1]))
