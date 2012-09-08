class WordProvider:
    def __init__(self, words):
        self.words = words

    def get_words(self):
        return self.words

    def get_matching_words(self, regex):
        return list([word for word in self.words if regex.match(word)])

    def get_filtered_words(self, function):
        return filter(function, self.words)


class FileWordProvider(WordProvider):
    def __init__(self, filename):
        f = open(filename)
        words = f.readlines()
        f.close()
        words = map(lambda word: word.strip(), words)
        WordProvider.__init__(self, words)
