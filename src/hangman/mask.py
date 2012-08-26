#-*- coding: utf-8 -*-
import re

UNGUESSED_LETTER_PLACEHOLDER = '*'
ALL_LETTERS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def get_mask(word, guessed_letters):
    mask = [letter if letter in guessed_letters
            else UNGUESSED_LETTER_PLACEHOLDER
            for letter in word]
    return ''.join(mask)

def make_regex_for_mask(mask, wrong_letters, guessed_letters):
    excluded_letters = wrong_letters + guessed_letters
    allowed_letters = [letter for letter in ALL_LETTERS if letter not in excluded_letters]
    allowed_letters = ''.join(allowed_letters)
    # it can be more efficient if a sequence of * was replaced with
    # "[letter_pattern]{n}"
    unguessed_letter_pattern = "[%s]" % allowed_letters
    regex = '^%s$' % mask.replace(UNGUESSED_LETTER_PLACEHOLDER, unguessed_letter_pattern)
    return re.compile(regex, re.MULTILINE)