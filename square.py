def square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result
    
print(square([2,3,4,5,6]))
