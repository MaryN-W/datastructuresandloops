# Function - a reusable collection of code that performs a particular task
# consists of several items: 
# def => defining / creating a function
# naming the function
# list of parameters enclosed in parenthesis

def greet(name, profession, country='Australia'): # Declaring a function # Positional arguments i.e name then profession, country=Australia provides a default value 
    print(f'Hey There, {name}! You are a {profession} in the making!')
    print(f'And you live in {country}')
    print('Keep Going!')

#greet('Wangari', 'Coder') # Same as being explicit greet(name='Wangari') # Call the function => means execute or run the code in the function
greet(profession='Coder', name='Wangari') # keywords provides semantics for positional arguments sequence when interchanged
# greet('James', 'Plumber') # Call the function as many times as you want
greet('Shimenga', 'Scientist', 'Kenya')

