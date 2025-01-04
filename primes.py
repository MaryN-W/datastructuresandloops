# Output if a number is prime example
# Number is prime iff(if and only if) it is divisible by 1 and itself only
# 16 -> 1, 2, 4, 8, 16 -> Not prime
# 17 -> 1, 17 -> Prime

number = 17
for i in range(2, number):
    if number % i == 0:
        print('Not a prime')
        break
else:
    print('Is prime')