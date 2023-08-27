# ===== Calculate the power of number using recursion ===

def power(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, 'Exponent must be positive integers'
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)  

print(power(-2, 4))