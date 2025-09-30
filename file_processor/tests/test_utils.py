from collections import Counter
from processor.utils import mix_word, process_text


def test_mix_word_short_word():
    """
    Test that words of length <= 3 are returned unchanged by `mix_word`.

    Examples:
        "hi"  -> "hi"
        "eva" -> "eva"
    """
    assert mix_word("hi") == "hi"
    assert mix_word("eva") == "eva"


def test_mix_word_long_word():
    """
    Test that `mix_word` shuffles the inner letters of a longer word
    while preserving the first and last letters.

    Verifies:
        - First letter remains the same
        - Last letter remains the same
        - Middle letters are a permutation of the original middle letters
    """
    word = "Annapurna"
    mixed = mix_word(word)
    assert mixed[0] == "A"
    assert mixed[-1] == "a"
    assert Counter(mixed[1:-1]) == Counter(list("nnapurn"))


def test_process_test_preserve_lines():
    """
    Test that `process_text` preserves the number of lines in the text
    while shuffling words on each line.

    Verifies:
        - The output has the same number of lines as the input
    """
    text = "Hello world\nDjango testing."
    output = process_text(text)
    assert len(output.splitlines()) == 2
