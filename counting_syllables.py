VOWELS = ['a', 'e', 'i', 'o', 'u']
import re

# input: a single word
# output: the number of syllables in the word
def count_syllables_in_word(word):
    # process word
    dealt_with_es = deal_with_es(word)
    # deal with pairs before ys to account for lying -> li/ing where it should be 2 syllables
    dealt_with_pairs = deal_with_pairs(dealt_with_es)
    dealt_with_ys = deal_with_ys(dealt_with_pairs)
    # return the count of "syllables" (vowels)
    return count_syllables(dealt_with_ys)

# input: a single word (already processed)
# output: the count of vowels in a word
def count_syllables(word):
    syllables = 0
    for char in word:
        if char in VOWELS:
            syllables += 1
    if syllables == 0:
        # this is an acronym since none of its elements are vowels
        # we will count each acronym letter as one syllable
        syllables = len(word)
    return syllables

# input: a single word
# output: remove e's at the end of the word if they are not creating a syllable
def deal_with_es(word):
    consonants_that_make_e_silent = ['c','d','f','g','h','k','m','n','p','q','r','s','t','v','w','x','z']
    word_length = len(word)
    last_char = word[word_length - 1]
    prev_char = word[word_length - 2]
    if last_char == 'e':
        # if e at the end of 2/3 length remove e if more than one vowel
        if word_length <= 3:
            if count_syllables(word) > 1:
                word = word[0:(word_length-1)]
        # if e at the end of the word, remove if it follows one of the known letters (also word_length > 3)
        elif prev_char in consonants_that_make_e_silent:
            word = word[0:(word_length-1)]
    return word

# input: a single word
# output: word without pairs of vowels (second vowel replaced with z to keep length)
def deal_with_pairs(word):
    last_char = 0
    word_length = len(word)
    for curr_char in range(1, word_length):
        if word[last_char] in VOWELS and word[curr_char] in VOWELS:
            #pair of VOWELS
            word = word[:curr_char] + 'z' + word[(curr_char+1):] #adding consonant to keep length the same
            
        last_char = curr_char
    return word

# input: a word, the index of the character after y, the index of the character before y, the length of the word
# output: the word where if there is a vowel followed by ye then remove last e unless its followed by an r
def vowel_y_e(word, next_index, last_index, word_length):
    # vowel y e
    if (next_index <= word_length - 1 and last_index >= 0 and
        word[next_index] == 'e' and word[last_index] in VOWELS):
            index_after_e = next_index + 1
            if index_after_e <= word_length - 1 and word[index_after_e] != 'r':
                word = re.sub('ye', 'y', word)
    return word

# input: a word, the index of the character after y, the index of the character before y, the index of the y, the length of the word
# output: the word where if there is a vowel follow or procedded by a y, remove the y
def vowel_y_or_y_vowel(word, next_index, last_index, index_y, word_length):
    if next_index > word_length - 1 and word[last_index] in VOWELS:
        #y at end of word
        word = word[:index_y]
    elif last_index < 0 and word[next_index] in VOWELS:
        #y at beginning of word
        word = word[(index_y+1):]
    elif (next_index <= (word_length - 1) and last_index >= 0
        and word[next_index] in VOWELS or word[last_index] in VOWELS):
        #y in the middle of the word
        word = word[:index_y] + word[(index_y+1):]
    return word

# input: a word, the index of the character after y, the index of the character before y, the length of the word
# output: the word where if there is a y after a consonant that y is treated like a vowel (i)
def consonant_y(word, next_index, last_index, word_length):
    if next_index > word_length - 1 and word[last_index] not in VOWELS:
        #y at end of word
        word = re.sub('y', 'i', word)
    elif next_index <= word_length - 1 and last_index >= 0 and word[last_index] not in VOWELS:
        word = re.sub('y', 'i', word)
    return word

# input: a single word
# output: the word where if there is a y is it dealth with appropriatly
def deal_with_ys(word):
    word_length = len(word)
    while 'y' in word:
        index_y = word.find('y')
        next_index = index_y + 1
        last_index = index_y - 1
        word = vowel_y_e(word, next_index, last_index, word_length)
        word = vowel_y_or_y_vowel(word, next_index, last_index, index_y, word_length)  
        word = consonant_y(word, next_index, last_index, word_length)
    return word