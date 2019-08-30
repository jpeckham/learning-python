# from https://www.w3schools.com/python/python_functions.asp
def my_function():
  print("Hello from a function")

my_function()

#using params
def with_param(fname):
  print(fname + " Refsnes")

with_param("Emil")
with_param("Tobias")
with_param("Linus")

#default values
def default_params(country = "Norway"):
  print("I am from " + country)

default_params("Sweden")
default_params("India")
default_params()
default_params("Brazil")

# return values
def retvals(x):
  return 5 * x

print(retvals(3))
print(retvals(5))
print(retvals(9))

# using named params - aka ignore ordering
def using_named(one, two, three):
  print("one " + one + " two "+two+" three "+three)

using_named(two="TWO", one="ONE", three="THREE")

# 'arbitrary arguments' like params in c#
def arbitrary(*args):
  print("the string is " + args[2])

arbitrary(1, 3.0, "Linus")
