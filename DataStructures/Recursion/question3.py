#==========   How to find GCD i.e Greatest Common Divisor of two numbers using recursion =========

#Step 1 ==>>> Recursion case - the flow
#
# GCD --->> It is the largest positive integer that divides the numbers without remainder #
# Eg->  gcd(8, 12) ===>>> 4 i.e 8 = 2 * 2 * 2, 12 = 2 * 2 * 3 
# Another way to find GCD is Euclidean Algo --->> 
#    gdc(48, 18) =>> 48/18 and so on till remainder is 0 #
#


def gcd(a,b):
    assert int(a) == a and int(b) == b, 'Number should be integer'
    if a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(-48,-18))