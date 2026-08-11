# Slicing => used to extract multiple characters
# syntax [starting index : jaha tak chahiye wo index uske aage ek number]

msg = "Hello World"
print(msg[0:5])

print(msg[2:])
# output => llo World
# this means 2 onwards sab kch

print(msg[:4])
# output => Hell
# this means 4 se ek minus se shuru tak (start tak)

print(msg[:])
# output => Hello World
# pura ka pura string mil jayega


msg = "Hello World"
print(msg[2:6:2])
# output => lo
# selected string llo 
# 2 se start hoga 5 tak chalega 
# starts from l ends on space
# aur 2 step chhodte chalega  yaani 
# pehele l aaya phr l chhoot gya phr o aaya aur space chho0t gya

msg = "Hello World"
print(msg[0:8:3])
# output => HlW

# print(msg[0:6:-1]) 
# this will give empty string
# u cant use negative step while working with positive indexing

msg = "Hello World"
print(msg[-5:-1:2])
# output => Wr
# selected string = Worl (because last one is not included)
# -5 = W
# -1 = d 


msg = "Hello World"
print(msg[::-1])
# output => dlroW olleH in this case ur string is reversed

msg = "Hello World"
print(msg[-1:-5:-1])
# output => dlro
# selected string = orld (because last one is not included)
# and isko reverse kr dia
# -1 = d
# -5 = o