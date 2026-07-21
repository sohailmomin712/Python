print("Hello, World!")
print(6)
print(6.5)
print(False)
print("India","China","Nepal")
# you can print multiple things at same time just use comma 
# u can also different datatype in single go just use comma

# sep parameter ki wajah se unko bichme apne aap space aajaata hai
# suppose u want slash instead of space we will do sep='/' or sep='-'
print("India","China","Nepal", sep='/')
print("India","China","Nepal", sep='-')

# end='/n' default value of end is /n which means line change
print("Hello") 
# ye alag line pe print hoga
print("World")
# and ye alag line pe reason end parameter is /n 

# agr mujhe same line me print krna ho to
print("Hello",end=' ') 
print("World")