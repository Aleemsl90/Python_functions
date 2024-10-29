'''
Explanation:
1. sentence.split() splits the input string into a list of words.
2. The list comprehension iterates over each word:
   If the word has 5 or more letters (len(word) >= 5), it reverses it using word[::-1].
   Otherwise, it leaves the word as is.
3. ' '.join(...) joins the modified words back into a single string, separated by spaces.
'''
def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])
