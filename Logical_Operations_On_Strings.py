# 3 Logical Operations

# " " => False {Empty string is always false}
# "random" => True {filled string is always true}
# 0 => False
# 1=> True

print("" and "world")
# op => '' (empty) {true and false = false}

print("" or "world")
# op => world {false and True = 1 i.e True}

print("hello" or "world")
# op => hello { because hello was already 1} 

print("hello" and "world")
# op => world { because world ke 1 hone pe aoko surety milti hai isiliye}

print( not "hello")
# output => False 
# because here hello is non empty string and
# non empty string ka opposite empty string hota hai which is internally false 

print( not "")
# output => True 
