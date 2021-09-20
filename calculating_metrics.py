VOWELS = ['a', 'e', 'i', 'o', 'u']
from counting_syllables import count_syllables_in_word

# input: an array of numbers
# output: a sum of all numbers in an array
def sum(array):
    total = 0
    for x in array:
        total += x
    return total

# input: an array of words
# output: length of the array
def count_words(sentence):
    return len(sentence)

# input: an array of sentences which are arrays of words
# output: the number of syllabes in the word with the most syllables
def max_syllabes_per_word(file_contents):
    max = 0
    for sentence in file_contents:
        for word in sentence:
            syllable_count = count_syllables_in_word(word)
            if syllable_count > max:
                max = syllable_count
    return max

# input: an array of sentences which are arrays of words
# output: the number of syllables in a word with the least number of syllables
def min_syllables_per_word(file_contents):
    min = 1
    for sentence in file_contents:
        for word in sentence:
            syllable_count = count_syllables_in_word(word)
            if syllable_count < min:
                min = syllable_count
    return min

# input: an array of sentences which are arrays of words
# output: the average number of syllables in words for a file
def avg_syllables_per_word(file_contents):
    syllables_per_file = syllables_per_word(file_contents)
    total = sum(syllables_per_file)
    count = len(syllables_per_file)
    if count > 0:
        return total/count
    else:
        return 0

# input: an array of sentences which are arrays of words
# output: the number of syllables in a word
def syllables_per_word(file_contents):
    syllables_per_file = []
    for sentence in file_contents:
        for word in sentence:
            syllables_per_file.append(count_syllables_in_word(word))
    return syllables_per_file

# input: an array of sentences which are arrays of words
# output: a count of all the sentences in a file
def number_of_senteneces(file_contents):
    return len(file_contents)

# input: an array of sentences which are arrays of words
# output: a sum of words in all sentences
def count_words_in_file(file_contents):
    total_word_count = 0
    for sentence in file_contents:
        total_word_count += count_words(sentence)
    return total_word_count

# input: an array of sentences which are arrays of words
# output: the number of words in a sentence with the most words
def max_words_per_sen(file_contents):
    max = 0
    for sentence in file_contents:
        word_count = count_words(sentence)
        if word_count > max:
            max = word_count
    return max

# input: an array of sentences which are arrays of words
# output: the number of words in a sentence with the least number of words
def min_words_per_sen(file_contents):
    min = 1
    for sentence in file_contents:
        word_count = count_words(sentence)
        if word_count < min:
            min = word_count
    return min

# input: an array of sentences which are arrays of words
# output: the average number of words in a sentence (0 if there are no words)
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

# input: an array of sentences which are arrays of words
# output: the flesch reading ease score for the file
def calculate_flesch_reading_ease_score(file_contents):
    total_num_words = count_words_in_file(file_contents)
    total_num_sentences = len(file_contents)
    total_num_syllables = sum(syllables_per_word(file_contents))
    # FRES = 206.835 - 1.015 * sentence_difficulty - 84.6*word_difficulty
    sentence_difficulty = total_num_words / total_num_sentences
    word_difficulty = total_num_syllables / total_num_words
    fres = 206.835 - 1.015 * sentence_difficulty - 84.6*word_difficulty
    return fres 

# input: an array of sentences which are arrays of words
# output: an array of metrics in order (#words, max_syllables, min_syllabes, avg_syllables, #sentences, max_words, min_words, avg_words, flesch_score)
def calculate_metrics(file_contents):
    total_words = count_words_in_file(file_contents)
    max_syllables = max_syllabes_per_word(file_contents)
    min_syllables = min_syllables_per_word(file_contents)
    avg_syllables = avg_syllables_per_word(file_contents)
    total_sentences = number_of_senteneces(file_contents)
    max_words_per_sentence = max_words_per_sen(file_contents)
    min_words_per_sentence = min_words_per_sen(file_contents)
    avg_words_per_sentence = avg_words_per_sen(file_contents)
    flesch_reading_ease_score = calculate_flesch_reading_ease_score(file_contents)
    return [
        total_words, #check on this one I think its off a bit
        max_syllables,
        min_syllables,
        round(avg_syllables, 2),
        total_sentences,
        max_words_per_sentence,
        min_words_per_sentence,
        round(avg_words_per_sentence,2),
        round(flesch_reading_ease_score,2)
    ]