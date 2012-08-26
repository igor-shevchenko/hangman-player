import mask
import re

class HangmanGuesser:
    def __init__(self, word_provider):
        self.word_provider = word_provider

    def guess_letter(self, word_mask, guessed_letters, wrong_letters):
        disallowed_letters = wrong_letters + guessed_letters
        regex = mask.make_regex_for_mask(word_mask, disallowed_letters)
        possible_words = self.get_possible_words(regex)
        possible_letters = self.get_letter_statistics(possible_words)
        for letter in possible_letters:
            if letter not in disallowed_letters:
                return letter
        # if word not in dictionary

        if word_mask != mask.UNGUESSED_LETTER_PLACEHOLDER * len(word_mask):
            # try common statistics for words of that length
            return self.guess_letter(mask.UNGUESSED_LETTER_PLACEHOLDE\
                                     * len(word_mask), guessed_letters,
                                     wrong_letters)
        elif word_mask != mask.ALL_WORDS_MASK:
            # try common statistics for all words
            return self.guess_letter(mask.ALL_WORDS_MASK, guessed_letters,
                                     wrong_letters)
        else:
            raise Exception()

    def get_possible_words(self, regex):
        return (word for word in self.word_provider.get_words() if regex.match(word))

    def get_letter_statistics(self, words):
        statistics = {}
        for word in words:
            for letter in set(word):
                statistics[letter] = statistics.get(letter, 0) + 1
        result = statistics.items()
        result.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return result


