# variables are mostly used when we dont know what will be used at some place in future
# variables basically means jo vary krne waala hota hai
# defination is simple containers for the future use

name = "sufi"
print(name)

# there is no variable declaration in python
# eg int num = 10 like this 
# we can directly use like this 
# num = 10

# Dynamic Typing 

# when we create a variable we dont need to tell python its datatype
# python automatically understand its datatype and this is called as Dynamic Typing 

# eg 
Number = 100
print(Number)

# Dynamic typing ka exact opposite hota hai Static Typing 
# where we have to specify the type of datatype 
# eg int num1= 10


# python me ek variable kisi datatypes se binded nhi hai
# u can change it anytime and this is called as Dynamic Binding
# in simple ek variable mulitple datatype store kr paaye
# and iska exact opposite hota hai static binding

name ="Sohail"
print (name)

name = 4
print(name)

name = True
print (name)


# special declaration syntax
# multiple varibles agr declare krne ho ek line me just use semicolon in between them to separate them

a=1; b=2; c=3
print(a)
print(b)
print(c)

# or u can use 
a,b,c = 4,5,6
print(a)
print(b)
print(c)

# one another technique
a = b = c = 10
print(a)
print(b)
print(c)