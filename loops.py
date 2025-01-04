# print(1) # longhand, not DRY
# print(2)
# print(3)
# print(4)
# print(5)


# # instead - condense repetitive code with while loop
# number = 1
# while number <=5: # boolean expression - while will repeatedly execute if the condition remains true
#     print(number) # prints infinite loop of 1 because condition is always true
#     number = number + 1 # increment. solves above

# # For loop
# names = ['Kamau', 'Ngigi', 'Gitau']
# for name in names: # visit each element in turn and put value in name and keep looping
#     print(name)

# for index, name in enumerate(names):  # enumerate() function takes a collection anc creates creates a new list with index paired with element  

#     print(f'{index+1}. {name}') # Prints ordered list

# # List all numbers between 10 and 100 and state whether they are odd or even
# for num in range(10, 101): # num is arbitrary # end value is exclusive
#      #if num % 2 == 0:
# #         print(f'{num} is even')
# #     else:
# #         print(f'{num} is odd')

# # DRY of above with ternary expression: integrate the condition above and rearrange it
#       print(f'{num} is {'even' if num % 2 == 0 else 'odd'}')
# refine above further
# num % 2 == 0 to num % 2 and swap odd and even

# for else -> see usage example in prime numbers
for i in range(10):
    print(i)
    if i == 6: # breaks out of the loop and else doesnt happen
        break
else:
    print('loop finished')
