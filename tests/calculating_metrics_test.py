import unittest

import calculating_metrics

class TestGuesser(unittest.TestCase):
    def test_sum(self):
        array = [1, 2, 3, 4]
        sum_of_array = calculating_metrics.sum(array)
        self.assertEqual(sum_of_array, 1+2+3+4)
    def test_count_words(self):
        array = ["hi", "how", "are", "you"]
        count_of_array = calculating_metrics.count_words(array)
        self.assertEqual(count_of_array, 4)
    def test_max_syllables(self):
        array = [["hi", "how", "are", "you"]]
        count_of_array = calculating_metrics.max_syllabes_per_word(array)
        self.assertEqual(count_of_array, 1)
    def test_min_syllables(self):
        array = [["hi", "how", "are", "you"]]
        count_of_array = calculating_metrics.min_syllables_per_word(array)
        self.assertEqual(count_of_array, 1)
    def test_syllables_per_word(self):
        array = [["hi", "how", "are", "you"]]
        array_of_syllable_counts = calculating_metrics.syllables_per_word(array)
        self.assertEqual(array_of_syllable_counts, [1, 1, 1, 1])
    def test_syllables_per_word_different_numbers(self):
        array = [["hi", "syllables", "creation", "differentation"]]
        array_of_syllable_counts = calculating_metrics.syllables_per_word(array)
        self.assertEqual(array_of_syllable_counts, [1, 3, 2, 5])
    def test_avg_syllables_per_word(self):
        array = [["hi", "syllables", "creation", "differentation"]]
        avg_syllables = calculating_metrics.avg_syllables_per_word(array)
        self.assertEqual(avg_syllables, (1+2+3+5)/4)
    def test_num_of_sentences(self):
        array = [["hi", "syllables", "creation", "differentation"], ["hi", "syllables", "creation", "differentation"], ["hi", "syllables", "creation", "differentation"]]
        count_of_sentences = calculating_metrics.number_of_senteneces(array)
        self.assertEqual(count_of_sentences, 3)
    def test_count_words_in_file(self):
        array = [["hi", "syllables", "creation", "differentation"], ["hi", "syllables", "creation", "differentation"], ["hi", "syllables", "creation", "differentation"]]
        count_of_words = calculating_metrics.count_words_in_file(array)
        self.assertEqual(count_of_words, 12)
    def test_max_words_in_file(self):
        array = [["hi", "syllables", "creation", "differentation"], ["hi", "creation", "differentation"], ["hi"]]
        count_of_words = calculating_metrics.max_words_per_sen(array)
        self.assertEqual(count_of_words, 4)
    def test_min_words_in_file(self):
        array = [["hi", "syllables", "creation", "differentation"], ["hi", "creation", "differentation"], ["hi"]]
        count_of_words = calculating_metrics.min_words_per_sen(array)
        self.assertEqual(count_of_words, 1)
    def test_avg_words_in_file(self):
        array = [["hi", "syllables", "creation", "differentation"], ["hi", "creation", "differentation"], ["hi"]]
        count_of_words = calculating_metrics.avg_words_per_sen(array)
        self.assertEqual(count_of_words, (4+1+3)/3)
    def test_calculate_flesch_reading_ease_score(self):
        array = [["hi", "syllables", "creation", "differentation"], ["hi", "creation", "differentation"], ["hi"]]
        flesch_score = calculating_metrics.calculate_flesch_reading_ease_score(array)
        expected_score = 206.835 - 1.015 * (8/3) - 84.6*(20/8)
        self.assertEqual(flesch_score, expected_score)
    def test_calculate_metrics(self):
        array = [["hi", "syllables", "creation", "differentation"], ["hi", "creation", "differentation"], ["hi"]]
        actual_metrics = calculating_metrics.calculate_metrics(array)
        expected_score = 206.835 - 1.015 * (8/3) - 84.6*(20/8)
        expected_metrics = [
            8,
            5,
            1,
            round(2.5, 2),
            3,
            4,
            1,
            round((8/3),2),
            round(expected_score,2)
        ]
        self.assertEqual(actual_metrics, expected_metrics)
    

if __name__ == '__main__':
    unittest.main()