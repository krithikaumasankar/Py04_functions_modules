import set_module

a = set()
b = set()

n1 = int(input("Enter number of elements in set A: "))
for i in range(n1):
    a.add(int(input()))

n2 = int(input("Enter number of elements in set B: "))
for i in range(n2):
    b.add(int(input()))

print("Set A:", a)
print("Set B:", b)

print(f"\n{'Union':<22}", set_module.union_set(a, b))
print(f"{'Intersection':<22}", set_module.intersection_set(a, b))
print(f"{'Difference (A-B)':<22}", set_module.difference_set(a, b))
print(f"{'Symmetric Difference':<22}", set_module.symmetric_set(a, b))
