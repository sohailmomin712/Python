# TypeConversion 
# It is a simple process jiska use kr ke ham ek datatype ko dusre datatype me convert kr skte hai but there some limitations for example u can convert kolkata into number right

# There are 2 types of Typeconversion

# 1 implicit {jab python apne aap conversion kr deta hai}
# print (4 + 5.5)  integer and float ka
# print (4.5 + 5+5j)   float and complex ka
# output aayega 9.5 apko python ko kch bolna nhi pada wo apne aap kr dega isi ko implicit typeconversion kehte hai


# 2 explicit {when as a programmer aapko batana padta hai python ko ki yaha type conversion krdo}

# explicit conversion krne ke liye aapke pass built in functions hote hai
# for every datatype u have typeconversion function

print(int(4.5))
# it will print 4 it basically converted float into integer

print(int("45"))
# it will print 45 it basically converted string into integer

# int => integer 
print(int(4.5))
# output => 4

# float => float
print(float(4))
# output => 4.0

# str => string
print(str(4))
# output => '4'

# bool => true 
print(bool(1))
# output => True

# complex => complex number 
print(complex(4))
# output => 4+0j

# list => list 
print(list("Hello"))
# output => ['H', 'e', 'l', 'l', 'o']

a = 6.5
print(int(a))
# output => '6'

print(a)
# output => 6.5
# type conversion is not a permanent operation 
# type casting is a permanent operation