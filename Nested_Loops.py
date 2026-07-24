rows = int(input("Enter numbers of rows"))
for i in range(1,rows +1):
 # why plus one because last ki value to exclude kr deta hai 
# like range(1,10) to 9 tak hi range hai
    for j in range(0,i):
        print("*",end=" ")
    print("")
