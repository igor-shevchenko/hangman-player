import mask
import operator

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
        for letters in possible_letters:
            if letters[0] not in used_letters:
                return letters[0]

        # if word not in dictionary, try common statistics for all words
        if word_mask != mask.ALL_WORDS_MASK:
            return self.guess_letter(mask.ALL_WORDS_MASK, guessed_letters,
                                     wrong_letters)

        raise Exception()

    def get_letter_statistics(self, words):
        statistics = {}
        for word in words:
            for letter in set(word):
                if letter in statistics:
                    statistics[letter] += 1
                else:
                    statistics[letter] = 0
        result = sorted(statistics.iteritems(), key=operator.itemgetter(1),
                        reverse=True)
        return result



