def add(num1, num2):
    sum = num1 + num2
    return sum # optimization of above return num1 + num2


# total = add(20, 10)
# final = add(total, 50) # add third value to above
final = add(add(20, 10), 50) # substitution of above
#print(total)
print(final) # the 3 values

