#-*- coding: utf-8 -*-

class WordProvider:
    def __init__(self, words):
        self.words = words

    def get_words(self):
        return self.words

    def get_matching_words(self, regex):
        return list([word for word in self.get_words() if regex.match(word)])

    def get_filtered_words(self, function):
        return filter(function, self.get_words())


class FileWordProvider(WordProvider):
    def __init__(self, filename, encoding):
        f = open(filename)
        words = f.readlines()
        f.close()
        words = map(lambda word: word.decode(encoding).strip(), words)
        WordProvider.__init__(self, words)

class GroupingByLengthFileWordProvider(FileWordProvider):
    def __init__(self, filename, encoding):
        FileWordProvider.__init__(self, filename, encoding)
        self.words_by_len = {}
        for word in self.words:
            wlen = len(word)
            if wlen not in self.words_by_len:
                self.words_by_len[wlen] = [word]
            else:
                self.words_by_len[wlen].append(word)

    def get_words_with_length(self, length):
        return self.words_by_len.get(length, [])

    def get_filtered_words_with_length(self, function, length):
        return filter(function, self.get_words_with_length(length))