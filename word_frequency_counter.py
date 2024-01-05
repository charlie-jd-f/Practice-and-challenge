sentence = "hello. world! hello python world"

def word_frequency_counter(sentence):
    
    # empty dictionary, words and number of words to be added
    result = {}
    
    # change sentence lower case to avoid errors in capitalisation
    sentence = sentence.lower()
    
    # place each word in the string into a list
    words = sentence.split()
    
    # a list to store words already looped over
    bin = []
    
    # loop through each word
    for word in words:
            
        # remove any punctionation from the word
        word = "".join(char for char in word if char.isalpha())
        
        # if the word has been seen, update the value of the word by one
        if word in bin:
            result[word] += 1
            
        # if the word has not been seen, add it to the result with a
        # a value 1
        else:
            result.update({word: 1})
            
            # add word to the bin, so we know its been seen again
            bin.append(word)
            
    
    return result

print(word_frequency_counter(sentence))