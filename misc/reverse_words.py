'''
Reverse the words in a string.

Notes
* What went well
  * Saw the insight of reversing the string first and then reversing each word on a second pass
* What didn't go well
  * Didn't validate the termination condition of reversing each (reversed) word, so it didn't reverse the last word.

'''
def reverse_array(arr, i, j, n):
    if i >= j:
        return
    while i < j:
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t 
        i += 1
        j -= 1

def reverse_words(s):
    n = len(s)
    arr = list(s)
    reverse_array(arr, 0, n-1, n)
    i = 0
    j = 0
    while j < n:
        if arr[j] == ' ':
            reverse_array(arr, i, j-1, n)
            j += 1
            i = j
        j += 1
    reverse_array(arr, i, j-1, n)
    return ''.join(arr)

if __name__ == '__main__':
    test_cases = [
         'this is a string',
         'string',
         ' string',
         'this is a   string'
    ]
    for t in test_cases:
        print(reverse_words(t))
