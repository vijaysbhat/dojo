'''
Implement string / integer interconversion functions

Notes:
* in python string to char array conversion and back is cumbersome. use native strings and operations on them instead
* what went right
    * checked for boundary conditions of i == 0 for int_to_str
* bugs
    * str_to_int
        * wrote out val += 10 * val... instead of val = 10 * val...
    * int_to_str
        * in python need to cast i/10 as int otherwise it auto converts to float
        * in python need to cast remainder as an int otherwise chr (char from ascii value) fails
        * forgot to add ord('0') to the digit value calculated

'''
def str_to_int(s):
    if s is None or s == '':
        return 0
    sign_multiplier = 1
    if s[0] == '-':
        sign_multiplier = -1
        s = s[1:]
    val = 0
    for d in s:
        val = 10 * val + (ord(d) - ord('0'))

    return sign_multiplier * val
    
def int_to_str(i):
    sign = ''
    if i < 0:
        sign = '-'
        i = i * -1
    s = ''
    if i == 0:
        return '0'
    while i > 0:
        s = chr(int(i % 10) + ord('0')) + s
        i = int(i / 10)
    return sign + s


if __name__ == '__main__':
    str_to_int_test_cases = [
        '34',
        '-210',
        '0',
        '12',
        '',
        '-',
    ]

    int_to_str_test_cases = [
        34,
        -210,
        0,
        12
    ]
    
    print('String to Integer')
    for t in str_to_int_test_cases:
        print(t, str_to_int(t))

    print('Integer to String')
    for t in int_to_str_test_cases:
        print(t, int_to_str(t))
