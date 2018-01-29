k = eval(input("Enter a non-empty set of positive integers: "))

x = 0
y = x

for i in k:
	if i >= y:
		y = i
		if i > x:
			if x != 0:
				y = x
				x = i
			else:
				x = y


print(x)
print(y)
