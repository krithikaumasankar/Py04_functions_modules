def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_sum_of_primes(num):
    found = 0    
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i):
            print(num, "=", i, "+", num - i)
            found = 1
    if not found:
        print("Not possible")

n = int(input("Enter number: "))
check_sum_of_primes(n)