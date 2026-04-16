# Write a Python program to count occurrences of a substring in a string. 

# Count occurrences of a substring in a string can be done using the built-in `count()` method of strings in Python.

string = input("Enter string: ")
sub = input("Enter substring: ")

count = string.count(sub)

print("Occurrences =", count)