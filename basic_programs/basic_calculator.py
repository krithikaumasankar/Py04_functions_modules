def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
   return a * b

def div(a, b):
    if b == 0:
      print(“Division by zero…!!”)
    else:
      return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Add =", add(a, b))
print("Sub =", sub(a, b))
print("Mul =", mul(a, b))
print("Div =", div(a, b))
