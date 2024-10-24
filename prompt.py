from .counter import report_counter


def report_count(token):
    """Generate a report of how many times a token appears in the corpus."""
    count = report_counter('corpus.txt', token)
    return f"The term {token} shows up in the corpus {count} times."