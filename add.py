def add_at_the_end(word):
	if word[-3:] == "ing":
		return word + "ly"
	elif len(word) >= 3:
		return word + "ing"
	elif len(word) < 3:
		return word
		
print(add_at_the_end("on"))
