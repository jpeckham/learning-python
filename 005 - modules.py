import module1 as mymodule

#not sure why pylint can't see this module
#pylint: disable=no-member
a = mymodule.person1["age"]
print(a)