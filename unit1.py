# Example 1: Printing a string
print("Welcome to TIP101!") # Prints "Welcome to TIP101!" to the console

# Example 2: Printing an integer
print(100) # Prints 100 to the console

# Example 3: Printing a variable
s = "Welcome to CodePath!"
num = 7
print(s)   # Prints "Welcome to CodePath" to the console
print(num) # Prints 7 to the console

# Example 4: Printing a list
lst = ["TIP101", "TIP102", "TIP103"]
print(lst) # Prints ["TIP101", "TIP102", "TIP103"] to the console

# Example 5: Printing an expression
x = 5
y = 3
print(x + y) # Prints 8 to the console

# Example 1: Getting the length of a list
lst = ['a', 'b', 'c']
lst_length = len(lst) 
print(lst_length) # Output: 3

# Example 2: Getting the length of string
s = 'abcd'
s_length = len(s)
print(s_length) # Output: 4

# Example 1: Just the stop value 
range(10) # Evaluates to the sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Example 2: Start and stop value
range(1, 11) # Evaluates to the sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Example 3: Start, stop, and step value
range(0, 30, 5) # Evaluates to the sequence: 0, 5, 10, 15, 20, 25

# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Outputs each fruit on a new line

# Example 2: Using a for loop with a range
for i in range(5):
    print(i)  # Prints numbers 0 to 4


# Example 1: Add an integer to the list
lst = [1, 2, 3, 4]
lst.append(5)
print(lst) # Prints [1, 2, 3, 4, 5]


# Example 1: List of integers
lst = [4, 2, 1, 3]
lst.sort()
print(lst) # Prints [1, 2, 3, 4]


# Example 2: List of strings
lst = ['b', 'a', 'd', 'c']
lst.sort()
print(lst) # Prints ['a', 'b', 'c', 'd']

# methods not required in unit 1:
# lst.insert(x, item) Inserts item into list at index x
# lst.remove(item) Removes item from list
# lst.pop(x) Removes element at index x from list
# lst.copy() Creates a copy of a list
# abs(x) Returns the absolute value of a number x.
# enumerate() Returns indices and values of list as pairs. Helpful for looping over indices and values of a list simultaneously!




# problem 1

def hello_world():
    print("Hello world!")

    hello_world()