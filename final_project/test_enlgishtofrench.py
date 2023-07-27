from machinetranslation.translater import englishtoFrench,frenchtoEnglish
import unittest

class TestTranslater(unittest.TestCase):
    def test_english_French(self):
        self.assertEqual(englishtoFrench('Hello'), 'Bonjour')
        self.assertEqual(englishtoFrench('Good'), 'Bien')
        self.assertEqual(englishtoFrench('Boy'), 'Garçon')

        self.assertNotEqual(englishtoFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishtoFrench('Boy'), 'Bien')
        self.assertNotEqual(englishtoFrench('Boy'), 'Garçon')

if __name__ == '__main__':
    unittest.main()
