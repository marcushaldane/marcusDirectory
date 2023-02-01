# PROMPT: Given a set of numbers, return the additive inverse of each. 
# Each positive becomes negatives, and the negatives become positives.
# You can assume that all values are integers. 
# Do not mutate the input array/list.

# EXAMPLE: 
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

print("===============================================================")

# SOLUTION
def invert(lst):
    return [-1*num for num in lst]
    

#FUNCTION TESTS
TestList = [-1, 2, -3, 4, -5, 6]
print(TestList)
newList = invert(TestList)
print(newList)
print("===============================================================")

