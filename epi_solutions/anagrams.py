
'''
Take a set of input words and return groups of anagrams for those words.

Notes:
* in python, calling sorted on a string returns a sorted array of characters
* what went wrong
    * returned singleton groups, need to only return groups with size >= 2
'''
def anagrams(arr):
    lookup = {}
    for s in arr:
        key = ''.join(sorted(s))
        if key in lookup:
            lookup[key].append(s)
        else:
            lookup[key] = [s]
    return [x for x in filter(lambda x: len(x) > 1, lookup.values())]

if __name__ == '__main__':
    test_cases = [
        ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis']
    ]
    for t in test_cases:
        print(t, anagrams(t))

