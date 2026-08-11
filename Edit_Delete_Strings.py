# Summary
# in short u can not edit a string naahi u can edit or add character 
# simply u can reassign it
# also u can not partially delete a string 
# u can just completely delete it


# 1 Editing
c = "hello"
# print(c)

# c[0] ='X'
# TypeError: 'str' object does not support item assignment
# item assignment = eidting

c = "World"
# print(c)
# strings are a immutable data type 
# (strings me editing nhi hota we can simply assign he new value)

# c = "World"
# print(c[5]="X")
# u can not add characters nor u can edit the string

# 2 Deletion

msg = "This message will be deleted"
# print(msg)
# output => This message will be deleted

# del is used to delete a string
del msg
# print(msg)  
# output => NameError: name 'msg' is not defined

a = "Hi"
print(a)
del a[0]
# print(a)
# output => TypeError: 'str' object doesn't support item deletion
# u can not delete a particular character from the string 
# because agr tum aisa kroge to usme(existing string me) change aajye i.e mutation hojayega
# and string is immutable

