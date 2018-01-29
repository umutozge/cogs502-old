
def func(x):
	x[0] = 8
	x = [1,2,3]
	return x

def funk(x):
	s = x
	x[0] = 7
	s[1] = 6 
	return x

k = [0,0,0]
print(func(k))
print(funk(k))
print(k)
