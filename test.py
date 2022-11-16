import re
import unittest

import digraphs

RH_TEST_CASES = ['a rh y th m i a', 'rh a n n u', 'a n rh e g', 'a r h o l i', 'rh a g f y r h a u', 'b a r - rh o l i o']
NG_TEST_CASES = ['m a n g o', 'a n g i o p l a s t y', 'll u n g o p i', 't a n g y f l o g i', 't a ng i a d', 'Ll a n g o ll e n', 'b r o n g o ch', 'p e n f l i ng o', 'rh y ng w y n e b', 'll e n g a r', 'a ng h y f e i ll g a r']

class TestDigraphs(unittest.TestCase):
    def test_split_word(self):
        for test_case in RH_TEST_CASES + NG_TEST_CASES:
            word = test_case.replace(' ', '')
            actual = digraphs.split_word(word)
            expected = test_case.split(' ')
            self.assertEqual(actual, expected, word)

    def test_split_word_with_lemma(self):
        self.assertEqual(
                digraphs.split_word('nghwyngar', 'cwyngar'),
                ['ng', 'h', 'w', 'y', 'n', 'g', 'a', 'r'],
                'nghwyngar < cwyngar',
        )

if __name__ == '__main__':
    unittest.main()
