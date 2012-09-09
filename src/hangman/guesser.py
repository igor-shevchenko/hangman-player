import mask
import operator

class HangmanGuesser:
    def __init__(self, word_provider):
        self.word_provider = word_provider

    def guess_letter(self, word_mask, guessed_letters, wrong_letters):
        used_letters = wrong_letters.union(guessed_letters)
        filtering_function = mask.make_filter_function_for_mask(word_mask, used_letters)
        possible_words = self.word_provider.get_filtered_words_with_length\
            (filtering_function, len(word_mask))
        possible_letters_statistics = self.get_letter_statistics(possible_words)
        letter = self.pick_letter(possible_letters_statistics, used_letters)
        if not letter is None:
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
                if letter in statistics:
                    statistics[letter] += 1
                else:
                    statistics[letter] = 1
        result = sorted(statistics.iteritems(), key=operator.itemgetter(1),
            reverse=True)
        return result

    def pick_letter(self, possible_letters_statistics, used_letters):
        raise NotImplementedError()


class DeterminedHangmanGuesser(HangmanGuesser):
    def pick_letter(self, possible_letters_statistics, used_letters):
        for letters in possible_letters_statistics:
            if letters[0] not in used_letters:
                return letters[0]
        return None

class UndeterminedHangmanGuesser(HangmanGuesser):
    def __init__(self, word_provider, random_number_generator):
        HangmanGuesser.__init__(self, word_provider)
        self.rng = random_number_generator

    def pick_letter(self, possible_letters_statistics, used_letters):
        letters_sum = 0
        unused_letters_statistics = []
        for letters in possible_letters_statistics:
            if letters[0] not in used_letters:
                unused_letters_statistics.append(letters)
                letters_sum += letters[1]
        random_number = self.rng.randint(1, letters_sum)
        current_sum = 0
        for letters in unused_letters_statistics:
            current_sum += letters[1]
            if current_sum >= random_number:
                return letters[0]
        return None