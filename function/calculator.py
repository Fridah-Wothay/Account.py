def add(x,y):
   result = x+y
   return result

def subtract(x,y):
    result = x-y
    return result 

def divide(x,y):
    result = x/y
    return result

def multiply(x,y):
    result = x*y
    return result

def remainder(x,y):
    result = x%y
    return result

def power_of (x,y):
    result = x**y
    return result  

def sum (*numbers):
    total = 0
    for number in numbers:
        total += number
    return total    

      

def sum_and_greet (*args,**kwargs):    
    total = 0
    for x in args:
        total += x
    f = kwargs ["first_name"]
    l = kwargs["last_name"]
    greeting = f"Hello {f} {l} the sum of your numbers is {total}"
    return greeting

