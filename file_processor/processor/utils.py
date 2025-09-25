import random


def mix_word(word: str) -> str:
    """
    Shuffle the letters inside a single word while keeping
    the first and last character unchanged.

    Example:
        "hello" -> "hlelo" or "hlleo" (random result)

    Args:
        word (str): A single word to be mixed.

    Returns:
        str: The word with its inner characters shuffled.
             Words with length <= 3 are returned unchanged.
    """
    if len(word) <= 3:
        return word
    else:
        inner_word = list(word[1:-1])
        random.shuffle(inner_word)
        return word[0] + ''.join(inner_word) + word[-1]


def process_text(text: str) -> str:
    """
    Process a block of text by applying `mix_word` to every word
    while preserving the original line structure.

    Args:
        text (str): The full text content, possibly containing
                    multiple lines.

    Returns:
        str: The processed text, where each word has its internal
             letters shuffled but the first and last letters remain
             unchanged.
    """
    output = []
    for line in text.splitlines():
        words = line.split(' ')
        mixed_words = [mix_word(word) for word in words]
        output.append(' '.join(mixed_words))
    return '\n'.join(output)
