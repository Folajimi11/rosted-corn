def odd_index(word):
	new_word = ""
	for index in range(len(word)):
		if index % 2 != 0:
			new_word = new_word + word[index]
	return new_word
			
			
print(odd_index("semicolon"))




