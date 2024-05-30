import pandas as pd
import time
# Functions

# Function for separating the input
def sep(words):
	list_w = list(words.split(" "))
	return list_w

# Function for intro
def intro():
	print("Enter (Date, Hours, Minutes, Description)")
	print("Date(YYYY-MM-DD)")
	print("Use space as separator")
	print("Type 'quit' to quit")
	print("_______________________________________")

# Function to preview df
def preview():
	see_df = str(input("\nDo you want to preview?y/n: ")).upper()

	if see_df == "Y":
		print(df)
	elif see_df == "N":
		pass
	elif see_df != "Y" or see_df != "N":
		print("Invalid input: 'y' or 'n' only!")
		return "invalid"
	
# Function to combine inputs
def val_inputter(df):
	df_comp = pd.DataFrame()
	insert = ""
	while True:
		insert = str(input("\nEnter: "))
		if insert == "quit":
			break
		else:
			inputt = sep(insert)
			add_df = pd.DataFrame([inputt], columns=df.columns)
			df_comp = pd.concat([df_comp, add_df], ignore_index=True)
	return df_comp

# Function to add inputs to DataFrame
def confirm(df, adds_df):
	print(adds_df)
	confirm = str(input("\nDo you want to add these:(y/n): ")).upper()
	if confirm == "Y":
		df = pd.concat([df, adds_df], ignore_index=True)
		df.to_csv("/storage/69FA-10F1/Documents/Report/report_2024.csv", index=False)
		print(df)
	else: 
		print("\nNo changes\n\nQuitting...")
		time.sleep(2)
	
		
			
					

# READ FILE
df = pd.read_csv("/storage/69FA-10F1/Documents/Report/report_2024.csv")


# INTRO
intro()

# PREVIEW
prev = preview()
prev

# INSERTING INPUT TO DF
try: 
	if prev != "invalid":
		adds_df = val_inputter(df)
		if not adds_df.empty:
			print("\nInputting...\n\n")
			time.sleep(3)
	
	# CONFIRMATION MESSAGE
			try: 
				confirm(df, adds_df)
			except Exception as e:
				print("Invalid input: 'y'  or 'n' only!")
		else: 
			print("Quitting...")
			time.sleep(2)
		
except Exception as e:
	print("\nPass 4 data only")
