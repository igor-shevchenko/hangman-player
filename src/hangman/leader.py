import mask

NUMBER_OF_FEEBLE_ATTEMPTS = 10

class HangmanLeader:
    def __init__(self, word_provider, guesser):
        self.word_provider = word_provider
        self.guesser = guesser

    def play(self):
        word = self.word_provider.get_word()
        feeble_attempts = 0
        guessed_letters = []
        wrong_letters = []
        word_mask = mask.get_mask(word, guessed_letters)
        while feeble_attempts < NUMBER_OF_FEEBLE_ATTEMPTS and word != word_mask:
            letter = self.guesser.get_letter(word_mask, guessed_letters, wrong_letters)
            if letter in guessed_letters or letter in wrong_letters:
                raise Exception()
            if letter in word:
                guessed_letters.append(letter)
                word_mask = self.get_mask(word, guessed_letters)
            else:
                wrong_letters.append(letter)
                feeble_attempts += 1
        return word == word_mask, word_mask, feeble_attempts
