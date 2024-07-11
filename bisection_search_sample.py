# Given
total_cost = 1000000
portion_down_payment = .25
down_payment = total_cost * portion_down_payment

# Personal account
initial_salary = int(input("Enter annual salary: ")) #percent to save


# Salary raise 
semi_annual_raise = .07


# Increase
r = .04  # ROI rate
rate_a = .001
rate_b = 1.0


while True:
	
	rate_c = (rate_a+rate_b)/2
	current_savings = 0
	annual_salary = initial_salary
	#
	for i in range(1, 37):
		roi = (current_savings*r)/12
		savings_increase = roi + (annual_salary/12)*rate_c
		current_savings += savings_increase
		
		if i%6 == 0: 
			annual_salary = annual_salary + (annual_salary*semi_annual_raise)
	
	
	
	precision = rate_b - rate_a
	diff = current_savings - down_payment
	#
	if rate_c > .99 and diff < -100: 
		print(f"Salary can't reach downpayment with {round(rate_c,0)*100}% saving rate")
		print(f"Precision rate: {precision:.4f}")
		break
		
	elif  diff > 100:
		rate_b = rate_c
		print(f"Left: {current_savings} rate: {rate_c:.2f}")
		
	elif diff < -100:
		rate_a = rate_c
		print(f"Right: {current_savings} rate: {rate_c:.2f}")
			
	else:
		print(f"Rate reached at {rate_c:.2f}")
		print(f"Precision rate: {precision:.4f}")
		break
	
		
		