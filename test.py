import lexicon
import unittest

lexicon.LEXICON_FILENAME = 'lecsicon-sampl.txt'
lex = lexicon.Lexicon()

class TestLexicon(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(lex.generate_spelling('Llanfair', 'Llanfair'), ['Ll', 'a', 'n', 'f', 'a', 'i', 'r'], 'capital Ll')
        self.assertEqual(lex.generate_spelling('tango', 'tango'), ['t', 'a', 'n', 'g', 'o'], 'split ng')
        self.assertEqual(lex.generate_spelling('thango', 'tango'), ['th', 'a', 'n', 'g', 'o'], 'split ng but join th')
        self.assertEqual(lex.generate_spelling('Bangor', 'Bangor'), ['B', 'a', 'n', 'g', 'o', 'r'], 'split ng')
        self.assertEqual(lex.generate_spelling('ungell', 'ungell'), ['u', 'n', 'g', 'e', 'll'], 'split ng but join ll')
        self.assertEqual(lex.generate_spelling('blingo', 'blingo'), ['b', 'l', 'i', 'ng', 'o'], 'join ng')
        self.assertEqual(lex.generate_spelling('flingodd', 'blingo'), ['f', 'l', 'i', 'ng', 'o', 'dd'], 'join ng and dd')

if __name__ == '__main__':
    unittest.main()
