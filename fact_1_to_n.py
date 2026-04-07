def factorial(n):
    f = 1
    for i in range(1,n + 1):
        f *= i
    return f
n = int(input("Enter n: "))

for i in range(n + 1):
    print("Factorial of", i, "=", factorial(i))