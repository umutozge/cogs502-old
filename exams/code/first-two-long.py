k = eval(input("Enter a non-empty set of positive integers: "))

x = 0
y = x

for i in k:
	if i >= x:
		z = x
		y = z
		x = i
	elif i > y:
		y = i

print(x)
print(y)
