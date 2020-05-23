'''
Take an array of non-negative real numbers denoting the daily price of a stock and returns the maximum profit
that could be made buying and selling the sotck over that time period

Notes:
* what went right
    * verified array counters being incremented in correct manner
* bugs
    * set min_price_so_far to zero

'''
def get_max_profit(arr):
    n = len(arr)
    if n <= 1:
        return 0

    min_price_so_far = arr[0]
    max_profit = 0
    i = 0
    while i < n:
        if arr[i] < min_price_so_far:
            min_price_so_far = arr[i]
        if arr[i] - min_price_so_far > max_profit:
            max_profit = arr[i] - min_price_so_far
        i += 1
    return max_profit 


def get_max_profit_brute_force(arr):
    n = len(arr)
    if n <= 1:
        return 0
    j = 1
    max_profit = 0
    while j < n:
        i = 0
        while i < j:
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i]
            i += 1
        j += 1
    return max_profit


if __name__ == '__main__':
    test_cases = [
        [310,315,275,295,260,270,290,230,255,260]
    ]
    for t in test_cases:
        print(t, get_max_profit_brute_force(t))
        print(t, get_max_profit(t))
