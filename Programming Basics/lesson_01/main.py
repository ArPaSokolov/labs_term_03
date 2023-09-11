a = int(input())
b = int(input())

s = "{} делить на {} = {:08.2f}"
t = s.format(a, b, a/b)

print (t)