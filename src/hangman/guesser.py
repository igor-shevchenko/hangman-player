import mask
import re

class HangmanGuesser:
    def __init__(self, word_provider):
        self.word_provider = word_provider

    def guess_letter(self, mask, guessed_letters, wrong_letters):
        regex = mask.make_regex_for_mask(mask, wrong_letters, guessed_letters)
        possible_words = self.get_possible_words(regex)

    def get_possible_words(self, regex):
        return (word for word in self.word_provider.get_words() if regex.match(word))

#    def get_letter_statistics(self, words):
#        statistics = {}
#        for word in words:
#            for letter in set(word):
#                statistics[letter] = statistics.get()


