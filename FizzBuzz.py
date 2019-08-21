for x in range (1, 100):
    output = ""
    if (x % 3 == 0):
        output += "Fizz"
    if (x % 5 == 0):
        output += "Buzz"
    if (output == ""):
        output += str(x)
    print(output)
    x += 1
