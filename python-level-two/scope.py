#local Scope

def myfunc():
  x = 300
  print(x)

myfunc()

#Function Inside Function
def myfunc1():
  xx = 300
  def myinnerfunc():
    print(xx)
  myinnerfunc()

myfunc1()

#Global Scope
xxx = 300

def myfunc2():
  print(xxx)

myfunc2()

print(xxx)
