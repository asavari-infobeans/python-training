def new_decorator(func):
   def wrap_func():
      print("CODE HERE BEFORE EXECUTE FUNC")
      func()
      print("FUNC HAS BEEN CALLED")

   return wrap_func

@new_decorator
def func_needs_decarator():
    print("THIS FUNCTION HAS A NEED OF A  DECORATOR")

#func_needs_decarator = new_decorator(func_needs_decarator);
func_needs_decarator()