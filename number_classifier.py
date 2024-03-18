class NumConverter:
	"""
	Convert numbers 1-10 to words:
		phrase: takes a string argument
		return: a string with numbers 1-10 converted
		"""
	num_dict = { "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}
	char = ["[", "]", ",", "'"]


  
	def __init__(self, phrase):
		self.sentence = phrase
		self.a_list = list(phrase.split(" "))

	def num_classifier(self):
		""" Identify the instance of int """
    
		nums = []
		for item in self.a_list:
			try: 
				item = int(item)
				is_num = isinstance(item, int)
				if is_num:
					nums.append(item)
			except: pass
		return nums


	def s_changer(self):
    """ Check if the number is from 1-10 and replace it with words """

		num_list = self.num_classifier()
		for num in num_list:
			num_s = str(num)
			if num_s in NumConverter.num_dict and num <= 10:
				index_to_replace = self.a_list.index(num_s)
				self.a_list[index_to_replace] = NumConverter.num_dict[num_s]

	def change(self):
		self.s_changer()
		num_sentence = str(self.a_list)
		for a in range(4):
			num_sentence = num_sentence.replace(NumConverter.char[a], "")
		return num_sentence
