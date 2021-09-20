import unittest

import counting_syllables

class TestGuesser(unittest.TestCase):
    def test_count_syllables_correct(self):
        word = "Hello"
        count = counting_syllables.count_syllables(word)
        self.assertEqual(count, 2)
    def test_count_syllables_y(self):
        word = "Hey"
        count = counting_syllables.count_syllables(word)
        self.assertEqual(count, 1)
    def test_count_syllables_ii(self):
        word = "liing"
        count = counting_syllables.count_syllables(word)
        self.assertEqual(count, 2)
    def test_deal_with_es_be(self):
        word = 'be'
        processed_word = counting_syllables.deal_with_es(word)
        self.assertEqual(processed_word, 'be')
    def test_deal_with_es_ace(self):
        word = 'ace'
        processed_word = counting_syllables.deal_with_es(word)
        self.assertEqual(processed_word, 'ac')
    def test_deal_with_es_bee(self):
        word = 'bee'
        processed_word = counting_syllables.deal_with_es(word)
        self.assertEqual(processed_word, 'be')
    def test_deal_with_es_the(self):
        word = 'the'
        processed_word = counting_syllables.deal_with_es(word)
        self.assertEqual(processed_word, 'the')
    def test_deal_with_es_cake(self):
        word = 'cake'
        processed_word = counting_syllables.deal_with_es(word)
        self.assertEqual(processed_word, 'cak')
    def test_deal_with_es_cadence(self):
        word = 'cadence'
        processed_word = counting_syllables.deal_with_es(word)
        self.assertEqual(processed_word, 'cadenc')
    def test_deal_with_pairs_none(self):
        word = 'cadence'
        processed_word = counting_syllables.deal_with_pairs(word)
        self.assertEqual(processed_word, 'cadence')
    def test_deal_with_soon(self):
        word = 'soon'
        processed_word = counting_syllables.deal_with_pairs(word)
        self.assertEqual(processed_word, 'sozn')
    def test_deal_with_should(self):
        word = 'should'
        processed_word = counting_syllables.deal_with_pairs(word)
        self.assertEqual(processed_word, 'shozld')
    def test_deal_with_creation(self):
        word = 'creation'
        processed_word = counting_syllables.deal_with_pairs(word)
        self.assertEqual(processed_word, 'creztizn')
    def test_deal_with_ys_sockeye(self):
        word = 'sockeye'
        processed_word = counting_syllables.deal_with_ys(word)
        self.assertEqual(processed_word, 'sockez')
    def test_deal_with_ys_players(self):
        word = 'players'
        processed_word = counting_syllables.deal_with_ys(word)
        self.assertEqual(processed_word, 'plaers')
    def test_deal_with_ys_layer(self):
        word = 'layer'
        processed_word = counting_syllables.deal_with_ys(word)
        self.assertEqual(processed_word, 'laer')
    def test_deal_with_ys_lying(self):
        word = 'lying'
        processed_word = counting_syllables.deal_with_ys(word)
        self.assertEqual(processed_word, 'liing')
    def test_deal_with_ys_ya(self):
        word = 'ya'
        processed_word = counting_syllables.deal_with_ys(word)
        self.assertEqual(processed_word, 'a')
    def test_deal_with_ys_ya(self):
        word = 'oy'
        processed_word = counting_syllables.deal_with_ys(word)
        self.assertEqual(processed_word, 'o')
    def test_deal_with_ys_ya(self):
        word = 'oyo'
        processed_word = counting_syllables.deal_with_ys(word)
        self.assertEqual(processed_word, 'oo')
    def test_count_syllables_lying(self):
        word = "lying"
        count = counting_syllables.count_syllables_in_word(word)
        self.assertEqual(count, 2)
    def test_count_syllables_hello(self):
        word = "hello"
        count = counting_syllables.count_syllables_in_word(word)
        self.assertEqual(count, 2)
    def test_count_syllables_sockeye(self):
        word = "sockeye"
        count = counting_syllables.count_syllables_in_word(word)
        self.assertEqual(count, 2)
    def test_count_syllables_sockeye(self):
        word = "creation"
        count = counting_syllables.count_syllables_in_word(word)
        self.assertEqual(count, 2)
    def test_count_syllables_sockeye(self):
        word = "the"
        count = counting_syllables.count_syllables_in_word(word)
        self.assertEqual(count, 1)
    def test_count_syllables_acronym(self):
        word = "RL"
        count = counting_syllables.count_syllables_in_word(word)
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()