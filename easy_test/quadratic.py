def quadratic(a, b, c):
	import math
	x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
	if b * b - 4 * a * c >= 0:
		return x1, x2
	else:
		print('无解')

print(quadratic(2, 3, 1) == (-0.5, -1.0))
print(quadratic(1, 3, -4) == (1.0, -4.0))