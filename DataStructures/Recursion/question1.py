# ====  ===== ===== How to find the sum of digit of positive integers using recursion??? ====  ===== =====

def sumOfDigits(n):
    assert n>=0 and int(n) == n, 'Number should be positive'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))

print(sumOfDigits(54))