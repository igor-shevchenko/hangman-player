

class WordProvider:
    def __init__(self, filename):
        f = open(filename)
        words = f.readlines()
        map(lambda word: word.strip(), words)
        self.words = words

    def get_words(self):
        return self.words
