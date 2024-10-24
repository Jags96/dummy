def report_counter(filename, word):
    """Count how many times a word appears in a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            # Split text into words and count occurrences
            return text.split().count(word.lower())
    except FileNotFoundError:
        return 0