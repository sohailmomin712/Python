# Membership Operators

# c = "hello world"
# for i in c:
#     # print(i)

# c = "hello world"
# for i in c[2:7]:
#     print(i)

# op=> l l o  w {2 se 7 tak}

c = "hello world"
for i in c[2:7:2]:
    print(i)

# op=> l  o  w {2 se 7 tak aur 2 ke step pr}

c = "hello world"
for i in c[::-1]:
    print(i)
# op=> # reverse print hota sab

d = "Sufi is good"
print('S' in d)
# output => True

print('G' in d)
# output => False

print('good' not in d)
# output => False