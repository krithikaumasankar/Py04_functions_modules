def fact(n):
    f=[]
    for i in range(1,n+1):
        if n % i == 0:
            f.append(i)
    return f

def isprime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def prime_fact(n):
    pf = []
    for i in range(1,n+1):
        if n % i == 0 and isprime(i):
            pf.append(i)
    return pf
