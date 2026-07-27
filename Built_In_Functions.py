# 1 absolute function (it is just the modulous function)
print(abs(4))
# output => 4 

# 2 power function (it basically means power function) 
print(pow(2,3))
# output => 8 

# 3 min/max function (it will give the minimum or maximum value)
# we need to pass iterable example string list tuples 
print(min([2,1,3,0]))
# output => 0
print(max([2,1,3,0]))
# output => 3

# in case of alphabet it depends on ASCII value
print(min("ABC")) 
# output => A
print(max("ABC"))
# output => C

# 4 round function gives round value 
# after the comma is how many digits after point
c = 22/7
print(round(c,3))
# output => 3.143
# till 3 digits after the decimal or point

# 5 divmod function (returns tuple)
# gives integer division result first x/y
# and then modulous division result x%y

print(divmod(5,2))
# output => (2,1) 
# 5/2 quotient will be 2
# 5%2 remainder will be 1

# 6 ord function 
# Return the Unicode code point for a one-character string.
# u should use when we need to know ASCII value

print(ord('A'))
# output => 65

# 6 len function basically gives the length of iterable
name = "Arkan"
print(name)
print(len(name))
# output => 5

# 7 sum function basically gives the sum of iterable
numbers = [10,20,30,40]
print(sum(numbers))
# output => 100

# 8 help function gives documentation