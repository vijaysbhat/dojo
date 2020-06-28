'''
Solve the sequence of moves needed for towers of Hanoi
Notes:
* what went right
    *
* what went wrong
    * didn't review recursion base case was returning correctly
'''
def towers_of_hanoi(n, from_peg, intermediate_peg, to_peg):
    if n == 0:
        return
    towers_of_hanoi(n-1, from_peg, to_peg, intermediate_peg)
    print('Move {} to peg {}'.format(n, to_peg))
    towers_of_hanoi(n-1, intermediate_peg, from_peg, to_peg)

if __name__ == '__main__':
    test_cases = [3, 5]
    for t in test_cases:
        print('Number of disks', t)
        towers_of_hanoi(t, 0, 1, 2)
