import random

# g*g, x/g, g+x/g, 

# make g*g close to x

def sqrt(x):
	g = random.randint(1, 1000)
	gg = 0
	while gg != x:
		gg = g*g
		x_g = x/g
		g = (g+x/g)/2
	return g


x = int(input("Enter number to sqrt: "))
print(f"{x}: {sqrt(x)}")
		