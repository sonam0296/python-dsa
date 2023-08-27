def factorial(n):
    # assert keyword let you test if a condition is true or not .i.e, base contraint
    assert n >= 0 and int(n) == n, 'Number should be positive'   # Negative numbers
    if n in [0,1]:  # base condition i.e if number is 0 or 1
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))