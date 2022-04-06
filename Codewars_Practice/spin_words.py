def spin_words(sentence):
    words = sentence.split(" ") #split the provided string into a list of substrings seperated by a space
    newlist = [] #define a new list to be used to build the spun words string
    for x in words: #navigates through the words list
        if len(x) >= 5: #checks for strings longer than 5 chars
            x = x [::-1] #reverses long strings
        newlist.append(x) #adds all words to newList
    return  " ".join(newlist) #joins all of the words in newlist and returns the final string

def spin_words2(sentence): # NOT MY CODE
    return ' '.join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def main(): # Defining main function
    print(spin_words("Hey there Marcus Haldane."))
    #print(spin_words2("Number 2 Hey there Marcus Haldane."))

if __name__=="__main__":
    main()
