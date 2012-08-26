#-*- coding: utf-8 -*-
import re

UNGUESSED_LETTER_PLACEHOLDER = '*'
ALL_LETTERS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALL_WORDS_MASK = '.*'

def get_mask(word, guessed_letters):
    mask = [letter if letter in guessed_letters
            else UNGUESSED_LETTER_PLACEHOLDER
            for letter in word]
    return ''.join(mask)

def make_regex_for_mask(mask, disallowed_letters):
    allowed_letters = [letter for letter in ALL_LETTERS if letter not in disallowed_letters]
    allowed_letters = ''.join(allowed_letters)
    # it can be more efficient if a sequence of * was replaced with
    # "[letter_pattern]{n}"
    unguessed_letter_pattern = "[%s]" % allowed_letters
    if mask == ALL_WORDS_MASK:
        regex = '^%s+$' % unguessed_letter_pattern
    else:
        regex = '^%s$' % mask.replace(UNGUESSED_LETTER_PLACEHOLDER, unguessed_letter_pattern)
    return re.compile(regex, re.MULTILINE)