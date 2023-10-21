s1 = set(input("Enter first set: ").split())
s2 = set(input("Enter second set: ").split())

print("Is subset: ", (s1 < s2) or (s1 > s2))
