import re

# input: a word
# output: the word(s) with contraction(s) removed
def undo_contractions(word):
    final_word = word
    if "\'s" in final_word:
        #'s -> is (could also be us but same number of vowels so it doesn't matter
        final_word = re.sub("\'s", " is", final_word)
    if "n\'t" in final_word:
        # n't -> n not (extra n doesn't change anything)
        final_word = re.sub("\'t", " not", final_word)
    if "\'m" in final_word:
        # 'm -> am
        final_word = re.sub("\'m", " am", final_word)
    if "\'ve" in final_word:
        # 've -> have
        final_word = re.sub("\'ve", " have", final_word)
    if "\'re" in final_word:
        # 're -> are
        final_word = re.sub("\'re", " are", final_word)
    if "\'ll" in final_word:
        # 'll -> will
        final_word = re.sub("\'ll", " will", final_word)
    return final_word

# input: an array of words possibly with contractions
# output: an array of words with no contractions
def remove_contractions(words):
    no_contraction_words = []
    for word in words:
        no_contractions = undo_contractions(word)
        no_contractions_list = re.split(' ', no_contractions)
        for no_contractions_word in no_contractions_list:
            no_contraction_words.append(no_contractions_word)
    return no_contraction_words

# input: word that possibly has special characters
# output: word with only alpha numeria characters (non alphanumeric characters are removed)
def remove_special_characers_from_word(word):
    final_string = ""
    for character in word:
        if(character.isalnum()):
            final_string += character
    return final_string

# input: an array of words possibly with speical characters
# output: an array of words with only alpha numerica characters
def remove_special_characters(words):
    no_special_character_words = []
    for word in words:
        no_special_characters = remove_special_characers_from_word(word)
        if len(no_special_characters) != 0:
            no_special_character_words.append(no_special_characters)
    return no_special_character_words

# input: takes in a phrase which is an array of words
# output: the phrase with no special characters (contractions are treated as a speical case)
def remove_special_characers_from_phrase(phrase):
    words = re.split(' ', phrase)
    # Undo contractions 's -> is n't -> n not 'm -> am 've -> have 're -> are 'll-> will
    no_contraction_words = remove_contractions(words)
    final_words = remove_special_characters(no_contraction_words)
    return final_words

# input: contents of a file
# output: processed contents of a file (split into sentences, no contractions or special characters)
def process_file(file_contents):
    lower_case_file = file_contents.lower()
    # Seperate different sentences to new lines (sentences are separed by ! ?. or :)
    split_file = re.split('\.|\?|\!|\:|\\n', lower_case_file)
    
    processed_phrases = []
    for phrase in split_file:
        # remove non character words (punctiation, special characters, bullet points, apostrophes etc.)
        # contractions are taken as a speical case
        final_phrase = remove_special_characers_from_phrase(phrase)
        # don't include empty sentences
        if len(final_phrase) != 0:
            processed_phrases.append(final_phrase)
    return processed_phrases