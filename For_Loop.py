# for loop 
# for loop iterates on range function or sequence
# range function built in function whose work is to generate integers

print(range(1,11))
# output => 1,11 (but 1 se 10 tak numbers included hai isme 11 nhi rahega included)

print(list (range(1,11))) 
# output => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list (range(1,11,2))) 
# range (start,stop,step) step is basically gap between numbers
# output => [1, 3, 5, 7, 9]

# sequence means jo bhi order me ho

for i in range(1,11):
    print(i)
# output => 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for i in range(1,11,2):
    print(i)
# output => 1, 3, 5, 7, 9

for i in range(10,0,-1):
    print(i)

for i in "Delhi":
    print(i)
# output => D,e,l,h,i 
# as Delhi is sequence of characters

for i in [1,2,3,5]:
    print(i)
# output => 1,2,3,5,

# when to use for loop
# jab aapko pta hai ki loop itni baar hi chalega 

# when to use while loop
# jab aapko pta nhi hai ki loop kitni baar chalega 
# (guessing game because we did not know ki user kitne attempts lega )