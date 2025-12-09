```python
def spam():  # Function to modify the global variable 'eggs'
    global eggs  # Declare the function can modify the global variable 'eggs'
    eggs = 'spam'  # Assign the value 'spam' to the global variable 'eggs'

eggs = 'global'  # Initialize the global variable 'eggs' with the value 'global'
spam()  # Call the function 'spam' to modify the global variable 'eggs'
print(eggs)  # Print the value of the global variable 'eggs'
```