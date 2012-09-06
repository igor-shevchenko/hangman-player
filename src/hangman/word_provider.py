class WordProvider:
    def __init__(self, words):
        self.words = words

    def get_words(self):
        return self.words

    def get_matching_words(self, regex):
        return (word for word in self.get_words() if regex.match(word))


class FileWordProvider(WordProvider):
    def __init__(self, filename):
        f = open(filename)
        words = f.readlines()
        f.close()
        map(lambda word: word.strip(), words)
        WordProvider.__init__(self, words)
