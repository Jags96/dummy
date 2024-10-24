def token_count(token):
    count = 0
    with open('corpus.txt') as file:
        text = file.read()
    for w in text.split():
        if w == token:
            count += 1
    return count