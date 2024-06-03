import re

			
def score(password):
	score = 0
	if re.search(r"(?=.*[A-Z])", password):
		score += 1
	if re.search(r"(?=.*[a-z])", password):
		score += 1
	if re.search(r"(?=.*\d)", password):
		score += 1
	if re.search(r"(?=.*[\W_])", password):
		score += 1
	return score

		
def eval_strength(score):
	if score == 4:
		return "Strong"
	elif score == 3:
		return "Good"
	elif score == 2:
		return "Weak"
	elif score <= 1:
		return "Very Weak"
	
	
def insert():
	while True:
		password = input("Enter password: ")
		if len(password) < 8:
			print("Enter at least 8 caharacters long. Try again")
		else:
			break
	pass_score = score(password)
	evaluation = eval_strength(pass_score)
	print(evaluation)
	

if  __name__ == "__main__":
	insert()
else: 
	print("Run on the same file")
