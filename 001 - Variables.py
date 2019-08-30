# this is a line comment. can't do block comments in python.
# for a good laugh read the comments of these nerds discussing it https://stackoverflow.com/questions/675442/how-to-comment-out-a-block-of-code-in-python

# this is a variable with an integer
myint = 7
print(myint)


# some variables with strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# multi line assignment
a, b = 1, 2
print(a, b)

# nulls (none) - interesting conversation about it https://stackoverflow.com/questions/3289601/null-object-in-python
something = None
print(something) # prints as 'None'
if something is None:
    print('something was none')