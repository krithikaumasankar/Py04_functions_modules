import factor_module
n = int(input("Enter number: "))
f = factor_module.factors(n)
pf = factor_module.prime_fact(n)
print(f"{‘Factors’:<15}", f)
print("{’Prime factors’:<15}", pf)
