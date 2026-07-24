# Break is used in Linear Searching
# for example in a database of 1000 people u are searching for person named Rahul u start searching for user with the name Rahul from 1st user right suppose u got Rahul at Number 50 do we need to go till 1000 no right that where we terminate the loop

# 1 Break Statement (Break ka kaam hota hai to terminate a loop on a specific condition)
for i in range(1,11):
    if i == 5:
        break
    print(i)
# output => 1,2,3,4
# here if the value of i == 5 the loop will break


# 2 Continue Statement (when condition is met code after continue is skipped)
# Where to use continue statement ek ecommerce website me products jo stock me hai wo show krne the so basically mai check kr rha tha ki wo product stock me hai ya nhi aur agr wo product available the to use show kr deta tha but agr wo stock me nhi rehta tha to mai "Continue Statement use krke jo stock me nhi tha usko skip kr deta tha"

for i in range(1,11):
    if i == 5:
        continue
    print(i)
# output => 1,2,3,4,6,7,8,9,10
# it did not print 5 as it met the condition i == 5
# so when condition is met the piece of code after the continue is skipped  

# 3 Pass Statement (Baadme dekhege when u are unsure tab use kr skte hai)
# its a filler basically when u are not sure about the code or logic but u want to move ahead and u want to come back to that specific code later 

# for i in range(1,11):
# if we this execute it will give error like loop execute kr so just use pass

    for i in range(1,11):
     pass
