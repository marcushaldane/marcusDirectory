
def open_or_senior(data):
    categories = []
    for member in data:
        if(member[0] >= 55 and member[1] > 7):
            categories.append('Senior')
        else:
            categories.append('Open')
    return categories

result = open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])
print(result)