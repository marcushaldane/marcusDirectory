def high_and_low(numbers):
    numberList = [int(x) for x in numbers.split(' ')]
    return str(max(numberList)) + " " + str(min(numberList))


print("RESULT: " + high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
#high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
#EXPECTS: "42 -9"