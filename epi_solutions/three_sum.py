'''
From an array A, determine if there is there are 3 elements can be chosen (with replacement)
to add up to a number t

Notes:
* Use the 2-sum technique of sorting the array and iterating from both ends toward the middle
* what went right
    * got the iteration termination conditions right
* what went wrong
    * returned the return value of list append() which is always None in Python
'''
def find_two_sum_sorted(sorted_arr, t):
    i = 0
    j = len(sorted_arr) - 1
    while i <= j:
        if sorted_arr[i] + sorted_arr[j] == t:
            return [sorted_arr[i], sorted_arr[j]]
        elif sorted_arr[i] + sorted_arr[j] < t:
            i += 1
        else:
            j -= 1
    return None


def find_three_sum(arr, t):
    sorted_arr = sorted(arr)
    for el in sorted_arr:
        two_sum = find_two_sum_sorted(sorted_arr, t - el)
        if two_sum is not None:
            two_sum.append(el)
            return two_sum
    return None 

if __name__ == '__main__':
    test_cases = [
        ([10,3,2,5,1], 13),
        ([10,3,2,5,1], 11)
    ]
    for t in test_cases:
        arr, t = t[0], t[1]
        print('Array', arr, 'Sum', t, find_three_sum(arr, t))

