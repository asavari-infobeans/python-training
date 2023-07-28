#STRINGS

# Basic
str= "Hi , what's going on"
print(str)
# Indexing
string = "abcdefg"
print("print 1st letter")
print(string[0])
print("print last letter")
print(string[-1])
print("print any middle letter")
print(string[3])
# Slicing
b = "Hello, World!"
print(b[2:5])
print("Slice From the Start")
print(b[:5])
print("Slice From the End")
print(b[2:])
print("print whole string")
print(b[:])
print("step Slicing")
print(b[::2])

# Basic Methods
c='qwertyuiiooop'
print("convert to uppercase")
x=c.upper()
print(x)

d='ABCDEF'
print("convert to lowercase")
y=d.lower()
print(y)

print("capitalize")
y=d.capitalize()
print(y)

d='Hello World'
print("Split method")
y=d.split('o')
print(y)

# String formatting

x= "Item one: {} Item two: {}".format("apple","orange")
print(x);
x= "Item one: {a} Item two: {b}".format(a="apple",b="orange")
print(x);