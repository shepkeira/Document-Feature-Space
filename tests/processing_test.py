import unittest

import processing

class TestGuesser(unittest.TestCase):
    def test_undo_contractions_hello(self):
        word = "Hello"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'Hello')
    def test_undo_contractions_hes(self):
        word = "he's"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'he is')
    def test_undo_contractions_lets(self):
        word = "let's"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'let is')
    def test_undo_contractions_dont(self):
        word = "don't"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'don not')
    def test_undo_contractions_possessive(self):
        word = "Sarah's"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'Sarah is')
    def test_undo_contractions_im(self):
        word = "i'm"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'i am')
    def test_undo_contractions_theyve(self):
        word = "they've"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'they have')
    def test_undo_contractions_were(self):
        word = "we're"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'we are')
    def test_undo_contractions_shell(self):
        word = "she'll"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'she will')
    def test_undo_contractions_yallve(self):
        word = "ya'll've"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'ya will have')
    def test_undo_contractions_yavell(self):
        word = "ya've'll"
        resulting_word = processing.undo_contractions(word)
        self.assertEqual(resulting_word, 'ya have will')
    def test_remove_contractions_yallve_shell_hello(self):
        phrase = ["ya'll've", "she'll", "hello"]
        resulting_phrase = processing.remove_contractions(phrase)
        self.assertEqual(resulting_phrase, ["ya", "will", "have", "she", "will", "hello"])
    def test_remove_special_character_from_words_apostrphe(self):
        word = "hi'"
        result_word = processing.remove_special_characers_from_word(word)
        self.assertEqual(result_word, "hi")
    def test_remove_special_character_from_words_bracket(self):
        word = "hi)"
        result_word = processing.remove_special_characers_from_word(word)
        self.assertEqual(result_word, "hi")
    def test_remove_special_character_from_words_colon(self):
        word = "h:i"
        result_word = processing.remove_special_characers_from_word(word)
        self.assertEqual(result_word, "hi")
    def test_remove_special_character_from_words_precent(self):
        word = "hi%"
        result_word = processing.remove_special_characers_from_word(word)
        self.assertEqual(result_word, "hi")
    def test_remove_special_character_from_words_question(self):
        word = "hi?"
        result_word = processing.remove_special_characers_from_word(word)
        self.assertEqual(result_word, "hi")
    def test_remove_special_character_from_words_number(self):
        word = "hi14"
        result_word = processing.remove_special_characers_from_word(word)
        self.assertEqual(result_word, "hi")
    def test_remove_special_character_from_words_dash(self):
        word = "hi—•"
        result_word = processing.remove_special_characers_from_word(word)
        self.assertEqual(result_word, "hi")
    def test_remove_special_characters_from_phrase_no_contractions(self):
        phrase = ["hi—•", "bonjour!", 'hi']
        resulting_phrase = processing.remove_special_characters(phrase)
        self.assertEqual(resulting_phrase, ["hi", "bonjour", "hi"])
    def test_remove_special_characters_from_phrase_remove_contractions(self):
        phrase = ["hi—•", "ya'll've", 'hi']
        resulting_phrase = processing.remove_special_characers_from_phrase(phrase)
        self.assertEqual(resulting_phrase, ["hi", "ya", "will", "have", "hi"])
    def test_process_file(self):
        file_contents = "hi—• ya'll've hi\nhow do you do"
        resulting_phrases = processing.process_file(file_contents)
        self.assertEqual(resulting_phrases, [["hi", "ya", "will", "have", "hi"], ["how", "do", "you", "do"]])
    

if __name__ == '__main__':
    unittest.main()