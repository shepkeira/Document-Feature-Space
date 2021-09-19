import os
import re

VOWELS = ['a', 'e', 'i', 'o', 'u']

def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f:
        file_contents = f.read()
        return file_contents

def get_file_names(directory_path):
    files = os.listdir(directory_path)
    return files

def get_file_contents():
    articles_path = os.path.join(os.getcwd(), "articles")
    if os.path.exists(articles_path):
        file_names = get_file_names(articles_path)
        files_contents = {}
        for file_name in file_names:
            article_path = os.path.join(articles_path, file_name)
            files_contents[file_name] = read_file(article_path)
        return files_contents
    else:
        print("Articles are not found.")
        return 0

def main():
    # Step 1 - Read in data
    files_contents = get_file_contents()
    if files_contents == 0:
        print("There was an error. Please confirm that the files are located in /articles.")
    # Step 2 - Process files
    for file_name, file_contents in files_contents.items():
        # Convert everything to lower case
        processed_contents = process_file(file_contents)
        # print(processed_contents)

        metrics = calculate_metrics(processed_contents)
        print(file_name + ": " + str(metrics))

        # Step 6 - caculate metrics
#           - total # words
#           - max # syllabls per word
#           - min # syllabls per word
#           - avg # syllable per word
#           - total # sentences
#           - max # words / sentence
#           - min # words / sentence
#           - avg # words / sentene
#           - flesch reading ease score

def count_words(sentence):
    return len(sentence)

def count_words_in_file(file_contents):
    total_word_count = 0
    for sentence in file_contents:
        total_word_count += count_words(sentence)
    return total_word_count

def max_words_per_sen(file_contents):
    max = 0
    for sentence in file_contents:
        word_count = count_words(sentence)
        if word_count > max:
            max = word_count
    return max

def min_words_per_sen(file_contents):
    min = 1
    for sentence in file_contents:
        word_count = count_words(sentence)
        if word_count < min:
            min = word_count
    return min

def sum(array):
    total = 0
    for x in array:
        total += x
    return total

def avg_words_per_sen(file_contents):
    words_per_sentence = []
    for sentence in file_contents:
        words_per_sentence.append(count_words(sentence))
    total = sum(words_per_sentence)
    count = len(words_per_sentence)
    if count > 0:
        return total/count
    else:
        return 0

def calculate_flesch_reading_ease_score(file_contents):
    total_num_words = count_words_in_file(file_contents)
    total_num_sentences = len(file_contents)
    total_num_syllables = sum(syllables_per_word(file_contents))
    # FRES = 206.835 - 1.015 * sentence_difficulty - 84.6*word_difficulty
    sentence_difficulty = total_num_words / total_num_sentences
    word_difficulty = total_num_syllables / total_num_words
    fres = 206.835 - 1.015 * sentence_difficulty - 84.6*word_difficulty
    return fres 

def max_syllabes_per_word(file_contents):
    max = 0
    for sentence in file_contents:
        for word in sentence:
            syllable_count = count_syllables_in_word(word)
            if syllable_count > max:
                max = syllable_count
    return max

def min_syllables_per_word(file_contents):
    min = 1
    for sentence in file_contents:
        for word in sentence:
            syllable_count = count_syllables_in_word(word)
            if syllable_count < min:
                min = syllable_count
    return min

def avg_syllables_per_word(file_contents):
    syllables_per_file = syllables_per_word(file_contents)
    total = sum(syllables_per_file)
    count = len(syllables_per_file)
    if count > 0:
        return total/count
    else:
        return 0

def syllables_per_word(file_contents):
    syllables_per_file = []
    for sentence in file_contents:
        for word in sentence:
            syllables_per_file.append(count_syllables_in_word(word))
    return syllables_per_file

# count_syllables_in_word
def calculate_metrics(file_contents):
    total_words = count_words_in_file(file_contents)
    max_syllables = max_syllabes_per_word(file_contents)
    min_syllables = min_syllables_per_word(file_contents)
    avg_syllables = avg_syllables_per_word(file_contents)
    total_sentences = len(file_contents)
    max_words_per_sentence = max_words_per_sen(file_contents)
    min_words_per_sentence = min_words_per_sen(file_contents)
    avg_words_per_sentence = avg_words_per_sen(file_contents)
    flesch_reading_ease_score = calculate_flesch_reading_ease_score(file_contents)
    return [
        total_words, #check on this one I think its off a bit
        max_syllables,
        min_syllables, #not working
        round(avg_syllables, 2),
        total_sentences,
        max_words_per_sentence,
        min_words_per_sentence,
        round(avg_words_per_sentence,2),
        round(flesch_reading_ease_score,2)
    ]
        
def process_file(file_contents):
    lower_case_file = file_contents.lower()
    # Seperate differnt centences to new lines (sentences are separed by ! ?. or :)
    split_file = re.split('\.|\?|\!|\:|\\n', lower_case_file)
    # Undo contractions 's -> is/us n't -> n not 'm -> am 've -> have 're -> are 'll-> will
    # remove non character words (punctiation, special characters, bullet points, etc.)
    processed_phrases = []
    for phrase in split_file:
        final_phrase = remove_special_characers_from_phrase(phrase)
        if len(final_phrase) != 0:
            processed_phrases.append(final_phrase)
    return processed_phrases


def undo_contractions(word):
    final_word = word
    if "\'s" in final_word:
        # is/us
        final_word = re.sub("\'s", " is", final_word)
    if "n\'t" in final_word:
        # n not
        final_word = re.sub("\'t", " not", final_word)
    if "\'m" in final_word:
        # m
        final_word = re.sub("\'m", " am", final_word)
    if "\'ve" in final_word:
        # have
        final_word = re.sub("\'ve", " have", final_word)
    if "\'re" in final_word:
        # are
        final_word = re.sub("\'re", " are", final_word)
    if "\'ll" in final_word:
        # will
        final_word = re.sub("\'ll", " will", final_word)
    return final_word

def remove_special_characers_from_word(word):
    final_string = ""
    for character in word:
        if(character.isalnum()):
            final_string += character
    return final_string

def remove_special_characers_from_phrase(phrase):
    words = re.split(' ', phrase)
    no_contraction_words = remove_contractions(words)
    final_words = remove_special_characters(no_contraction_words)
    return final_words

def remove_contractions(words):
    no_contraction_words = []
    for word in words:
        no_contractions = undo_contractions(word)
        no_contractions_list = re.split(' ', no_contractions)
        for no_contractions_word in no_contractions_list:
            no_contraction_words.append(no_contractions_word)
    return no_contraction_words

def remove_special_characters(words):
    no_special_character_words = []
    for word in words:
        no_special_characters = remove_special_characers_from_word(word)
        if len(no_special_characters) != 0:
            no_special_character_words.append(no_special_characters)
    return no_special_character_words

def count_syllables_in_word(word):
    dealt_with_pairs = deal_with_pairs(word)
    dealt_with_ys = deal_with_ys(dealt_with_pairs)
    dealt_with_es = deal_with_es(dealt_with_ys)
    return count_syllables(dealt_with_es)

def count_syllables(word):
    syllables = 0
    for char in word:
        if char in VOWELS:
            syllables += 1
    return syllables

def deal_with_es(word):
    consonants_that_make_e_silent = ['c','d','f','g','h','k','m','n','p','q','r','s','t','v','w','x','z']
    word_length = len(word)
    last_char = word[word_length - 1]
    prev_char = word[word_length - 2]
    if last_char == 'e':
        if word_length <= 3 and count_syllables(word) > 1:
            word = word[0:(word_length-1)]
        elif prev_char in consonants_that_make_e_silent:
            word = word[0:(word_length-1)]
    return word


def deal_with_pairs(word):
    last_char = 0
    word_length = len(word)
    for curr_char in range(1, word_length):
        if word[last_char] in VOWELS and word[curr_char] in VOWELS:
            #pair of VOWELS
            word = word[:curr_char] + 'z' + word[(curr_char+1):] #adding consonant to keep length the same
            
        last_char = curr_char
    return word


def vowel_y_e(word, next_index, last_index, word_length):
    # vowel y e
    if (next_index <= word_length - 1 and last_index >= 0 and
        word[next_index] == 'e' and word[last_index] in VOWELS):
            index_after_e = next_index + 1
            if index_after_e <= word_length - 1 and word[index_after_e] != 'r':
                word = re.sub('ye', 'y', word)
    return word

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

def consonant_y(word, next_index, last_index, word_length):
    if next_index > word_length - 1 and word[last_index] not in VOWELS:
        #y at end of word
        word = re.sub('y', 'i', word)
    elif next_index <= word_length - 1 and last_index >= 0 and word[last_index] not in VOWELS:
        word = re.sub('y', 'i', word)
    return word

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

if __name__ == "__main__":
    main()
