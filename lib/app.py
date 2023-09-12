import ipdb

print("Hello Flatiron! Class is in session!")

def add (num1, num2):
   if (type (num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
     
      return num1 + num2
   else: 
      raise Exception('num1 and num2 must be either integers or floats')
   
def subtract(num1, num2):
   if (type (num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
     
      return num1 - num2
   else: 
      raise Exception('num1 and num2 must be either integers or floats')
   
def multiply(num1, num2):
   if (type (num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
     
      return num1 * num2
   else: 
      raise Exception('num1 and num2 must be either integers or floats')
   
def divide(num1, num2):
   if (type (num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
     
      return num1 / num2
   else: 
      raise Exception('num1 and num2 must be either integers or floats')

def calculator(operation, num1, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        raise Exception('Operation must be either +,-,*, or/')
    
def print_greeting_loop(greeting):
   for char in greeting:
        print(char)
      


