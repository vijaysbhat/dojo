'''
Search a sorted list for the first element equal to k

Notes:
* For binary search, right hand index should be inclusive of the range being considered to calculate the midpoint
* what went right
    * got the termination conditions right
* what went wrong
    * cast midpoint as an int otherwise python will try to index by float which will throw an exception
'''
def first_element_equal(arr, left, right, k):
    if left > right:
        return -1
    mid = int((left + right) / 2)
    if arr[mid] < k:
        return first_element_equal(arr, mid+1, right, k)
    elif arr[mid] > k:
        return first_element_equal(arr, left, mid-1, k)
    else:
        if mid == 0 or arr[mid-1] < k:
            return mid
        else:
            return first_element_equal(arr, left, mid-1, k)


if __name__ == '__main__':
    test_cases = [
            ([1,3,6,6,6,7,9,11], 6), 
            ([1,3,6,6,6,7,9,11], 3), 
            ([1,3,6,6,6,7,9,11], 9), 
            ([1,3,6,6,6,7,9,11], 11), 
            ([1,3,6,6,6,7,9,11], 12), 
    ]
    for t in test_cases:
        print(t[0], t[1], first_element_equal(t[0], 0, len(t[0])-1, t[1]))
