# PROMPT: An isogram is a word that has no repeating letters, 
# consecutive or non-consecutive. Implement a function that determines 
# whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

# EXAMPLE: (Input --> Output)
# "Dermatoglyphics" --> true 
# "aba" --> false 
# "moOse" --> false (ignore letter case)

print("===============================================================")
# SOLUTION
def is_isogram(givenString):
	word = givenString
	for letter in word:
		#print(letter)
		if any((c in [letter.lower(), letter.upper()]) for c in word[word.index(letter)+1:]):
		#if (letter in word[word.index(letter)+1:]):
			return False
	return True

#FUNCTION TESTS
word = "Dermatoglyphics"
#print(word[1:])
print(is_isogram(word))
print("===============================================================")

