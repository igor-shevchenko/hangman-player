
NUMBER_OF_FEEBLE_ATTEMPTS = 10
UNGUESSED_LETTER_PLACEHOLDER = '*'

class HangmanLeader:
    def __init__(self, asker, guesser):
        self.asker = asker
        self.guesser = guesser

    def play(self):
        word = self.asker.get_word()
        attempts_left = NUMBER_OF_FEEBLE_ATTEMPTS
        guessed_letters = []
        wrong_letters = []
        word_mask = self.get_mask(word, guessed_letters)

    def get_mask(self, word, guessed_letters):
        mask = [letter if letter in guessed_letters
                        else UNGUESSED_LETTER_PLACEHOLDER
                for letter in word]
        return ''.join(mask)
