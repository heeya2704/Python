# Given the following code, identify which variables are local and which are global, and 
# explain what will be printed when you call outer() and then print(x) at the end:<br><br> python
# x = 'global'
# def outer():
# x = 'outer'
# def inner():
# nonlocal x
# x = 'inner'
# inner()
# print('Inside outer:', x)
# outer()
# print('Outside:', x)
# <br><br><em><strong>Hint:</strong> Focus on the scope of x inside and outside the functions.</em>

x = "global"

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

    inner()
    print("Inside outer:", x)

outer()
print("Outside:", x)

# x = "global" is a global variable.
# x = "outer" is a local variable inside the outer() function.
# inner() uses nonlocal x, so it modifies the x variable from outer(), changing it from "outer" to "inner".
# The global variable x is not changed.