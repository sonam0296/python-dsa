# Swapping vaiables
# ------------->>>><<<<-------------
a = 15
b = 23
print('Before Swapping : ', 'a = ', a, 'b = ', b)
a,b = b,a
print('After Swapping : ', 'a = ', a, 'b = ', b)
# ------------->>>><<<<-------------
c, d = 10, 20
print('Before Swapping : ', 'c = ', c, 'd = ', d)
temp = c # store c value to temp
c = d # store dvalue to c
d = temp  # store temp value to d
print('After Swapping : ', 'c = ', c, 'd = ', d)

#  Conditions ===>>>>
marks = int(input('Enter the marks obtained in test: '))
if marks < 0 or marks > 100:
    print('Invalid Marks')


# while loops

#  WAP to display the count of digits in number

num = int(input('Enter any num: '))

count = 0
while num > 0:
    count += 1
    num //= 10 # remove last digit 

print('Count of digits: ', count)

# WAP to display multiplication table

num = int(input('Enter a numb: '))
i = 1
while i <= 10:
    print(num ," * ", i ,' = ', num * i )
    i += 1

# For Loops
    
#  WAP to display numbers from 1 to n
num = int(input('Enter number: '))

for i in range(1, num + 1):
    print(i, end=' \n')

# break and continue

for i in range(1, 10):
    if i == 5:
        continue
    print('Break and Continue : ',i)
    
# WAP to find sum of 1st 10 natural numbers
    
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum of 1st 10 natural numbers : ", total)

# Display sum of digits in given number

num = int(input('Enter num for sum of digits: '))

total = 0
while num > 0:
    digit = num % 10  # extract last digit
    total = total + digit # adding that last digit 
    num = num // 10 # removing last digit

print('Sum of digits: ', total)