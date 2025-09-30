from django.test import SimpleTestCase
from utils import mix_word, process_text


class TextProcessingTests(SimpleTestCase):

    def test_mix_word_short_word(self):
        self.assertEqual(mix_word("hi"), "hi")
        self.assertEqual(mix_word("eva"), "eva")
