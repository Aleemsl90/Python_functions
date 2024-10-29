'''
Explanation
1. Strip extra spaces: morse_code.strip() removes any leading or trailing spaces from the input.
2. Split words: morse_code.split(" ") splits the morse code into words (using three spaces as delimiters).
3. Decode each word: For each word in words, split it into characters with word.split() and map each Morse character to its corresponding letter using MORSE_CODE.
4. Join decoded words: Finally, join the decoded words with a single space between each.
'''
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Split the input morse code into words (separated by three spaces)
    words = morse_code.strip().split("   ")
    
    # Decode each word separately
    decoded_words = []
    for word in words:
        # Split each word into characters (separated by single spaces)
        characters = word.split()
        # Decode each character and join them to form the word
        decoded_word = ''.join([MORSE_CODE[char] for char in characters])
        decoded_words.append(decoded_word)
    
    # Join decoded words with a single space
    return ' '.join(decoded_words)

''' another solution
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[c] for c in word.split(' ')) for word in morseCode.strip().split('   '))
'''
