def longest(words):
	length = 0
	long_word = ""
	for word in words:
		if len(word) > length:
			length = len(word)
			long_word = word
	return long_word, length
	
	
print(longest(["ayomide", "fola", "fuhad", "jimi", "okiki"]))
