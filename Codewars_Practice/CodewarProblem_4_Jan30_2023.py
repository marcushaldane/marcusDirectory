
def get_sum(a,b):
    nums = [a,b]
    return sum(range(min(nums),max(nums)+1))

print("TEST 1")
result = get_sum(1, 0)
print("Expected: 1 | Result: " + str(result))
print("TEST 2")
result = get_sum(1, 2)
print("Expected: 3 | Result: " + str(result))
print("TEST 3")
result = get_sum(0, 1)
print("Expected: 1 | Result: " + str(result))
print("TEST 4")
result = get_sum(1, 1)
print("Expected: 1 | Result: " + str(result))
print("TEST 5")
result = get_sum(-1, 0)
print("Expected: -1 | Result: " + str(result))
print("TEST 6")
result = get_sum(-1, 2)
print("Expected: 2 | Result: " + str(result))

'''
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
'''