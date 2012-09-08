#-*- coding: utf-8 -*-

import mask

NUMBER_OF_FEEBLE_ATTEMPTS = 40

class HangmanLeader:
    def __init__(self, guesser):
        self.guesser = guesser

    def play(self, word):
        feeble_attempts = 0
        guessed_letters = set()
        wrong_letters = set()
        word_mask = mask.get_mask(word, guessed_letters)
        while feeble_attempts < NUMBER_OF_FEEBLE_ATTEMPTS and word != word_mask:
            letter = self.guesser.guess_letter(word_mask, guessed_letters, wrong_letters)
            if letter in guessed_letters or letter in wrong_letters:
                raise Exception()
            if letter in word:
                guessed_letters.add(letter)
                word_mask = mask.get_mask(word, guessed_letters)
            else:
                wrong_letters.add(letter)
                feeble_attempts += 1
        return word == word_mask, word_mask, feeble_attempts
