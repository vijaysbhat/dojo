
def parity_brute_force(x):
    res = 0
    while x > 0:
        res ^= x & 0x1
        x = x >> 1
    return res

def parity_bit_shifting(x):
    four_bit_parity_lookup_table = 0x6996  #= 0b0110100110010110

    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x &= 0xF

    return (four_bit_parity_lookup_table >> x) & 0x1

if __name__ == '__main__':
    test_cases = [
        1,
        20,
        29,
        28,
        45
    ]
    print('Brute force')
    for t in test_cases:
        print(t, parity_brute_force(t))
        
    print('Bit shifting')
    for t in test_cases:
        print(t, parity_bit_shifting(t))
        
