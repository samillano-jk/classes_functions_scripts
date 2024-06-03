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

		
def eval(score):
	if score == 4:
		return "Strong"
	if score == 3:
		return "Good"
	if score == 2:
		return "Weak"
	if score <= 1:
		return "Very Weak"
	
	
def insert():
	while True:
		password = str(input("Enter password: "))
		if len(password) < 8:
			print("Enter at least 8 caharacters long. Try again")
		else:
			break
	pass_score = score(password)
	evaluation = eval(pass_score)
	print(evaluation)
	

insert()