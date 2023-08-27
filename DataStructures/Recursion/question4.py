# ======= How to convert a number from Decimal to Binary using recursion ======= 

#Step 1 ==>>> Recursion case - the flow
#
#   1. Divide number by 2
#   2. Get the integer quotient for the next iteration
#   3. Get the remainder for the binary digit 
#   4. Repeat until quotient is 0

# Eg - 13 to binary ===>>> 1011

def demicalToBinary(num):
    assert int(num) == num, 'Number should be positive'
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * demicalToBinary(int(num/2))

print(demicalToBinary(12))