import unittest
from translator import english_to_french, french_to_english


class TestTranslation(unittest.TestCase):

    def test_english_to_french_translation(self):
        text = "eat"
        expected_translation = "manger"
        translation = english_to_french(text)
        self.assertEqual(translation.lower(), expected_translation.lower())

    def test_french_to_english_translation(self):
        text = "Bonjour"
        expected_translation = "Hello"
        translation = french_to_english(text)
        self.assertEqual(translation.lower(), expected_translation.lower())

if __name__ == '__main__':
    unittest.main()