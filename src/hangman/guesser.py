import mask
import re

class HangmanGuesser:
    def __init__(self, word_provider):
        self.word_provider = word_provider

    def guess_letter(self, word_mask, guessed_letters, wrong_letters):
        raise NotImplementedError()


class DeterminedHangmanGuesser(HangmanGuesser):
    def guess_letter(self, word_mask, guessed_letters, wrong_letters):
        used_letters = wrong_letters.union(guessed_letters)
        filtering_function = mask.make_filter_function_for_mask(word_mask, used_letters)
        possible_words = self.word_provider.get_filtered_words(filtering_function)
        possible_letters = self.get_letter_statistics(possible_words)
        for letter in possible_letters:
            if letter not in used_letters:
                return letter

        # if word not in dictionary, try common statistics for all words
        if word_mask != mask.ALL_WORDS_MASK:
            return self.guess_letter(mask.ALL_WORDS_MASK, guessed_letters,
                                     wrong_letters)

        raise Exception()

    def get_letter_statistics(self, words):
        statistics = {}
        for word in words:
            for letter in set(word):
                statistics[letter] = statistics.get(letter, 0) + 1
        result = statistics.items()
        result.sort(key=lambda x: (x[1], x[0]), reverse=True)
        result = map(lambda x: x[0], result)
        return result


