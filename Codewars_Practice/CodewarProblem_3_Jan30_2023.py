def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.pop(numbers.index(min1))
    min2 = min(numbers)
    return min1 + min2


result = sum_two_smallest_numbers([5, 8, 12, 18, 22])
print("RESULT: " + str(result))
#EXPECTS: 13