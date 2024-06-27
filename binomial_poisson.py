from math import factorial as f, exp as e

#def factorial(num):	
#	total = num
#	for i in range(1, num):
#		total *= i
#	return total

def binomial_d(k, n, p):
	n_c_k = f(n)/(f(k)*f(n-k))
	result = n_c_k * (p**k)*((1-p)**(n-k))
	return round(result, 4)


def poisson(prob, _lambda):
	result = (_lambda**prob)*(e(-_lambda))/f(prob)
	return round(result, 4)
	
	
def binomial_start(): 	
	while True: 	
		try: 
			p = float(input("Probability: "))
			if p == 0:
				print("Quitting....")
				break
			else: 
				t = int((input("# Trials: ")))
				s = int(input("Success: "))
				print(f"{binomial_d(s, t, p)}")
				print()
		except Exception as e:
			print(e)
		
		
def poisson_start():
	try:
		while True:
			prob = int(input("Enter probability: "))	
			if prob == 0:
				print("Quitting...")
			else:
				n = int(input("Enter # trials: "))
				print(f"Trials: {n} Probability: {poisson(n, prob)} ")
				print()
	except Exception as e:
		print(e)
		

def start():
	while True: 
		type = input("(poisson/binomial: ")
		if type == "poisson":
			poisson_start()
			break
		elif type == "binomial":
			binomial_start()
			break
		else:
			print("Type 'binomial' or 'poisson' only")
		
		
		
if __name__ == "__main__":
	start()