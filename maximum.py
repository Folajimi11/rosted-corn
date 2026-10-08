def maximum_number(numbers):
	largest = numbers[0]
	for number in numbers:
		if number > largest:
			largest = number
	return largest
			
print(maximum_number([8,4,9,2,5,7,3]))
