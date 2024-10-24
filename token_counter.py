def token_count(token):
    count = 0
    try:
        with open('corpus.txt') as file:
            text = file.read()
        for w in text.split():
            if w == token:
                count += 1
        return count
    except :
        return f'FileError: check if corpus.txt exists or its in the right encoding and has correct text' 