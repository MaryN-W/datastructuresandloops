# Function to determine if a number is even or odd

def even_or_odd(num):
    if num % 2 == 0:
        return 'Even' # compared to print function, return is explict => does not wait to execute the rest of the code
    else:
        return 'Odd'
    
print(even_or_odd(9))
result = even_or_odd(5)
even_or_odd(50)
# print(result) 
print(f'5 is {result}')



