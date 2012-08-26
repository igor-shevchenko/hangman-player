#-*- coding: utf-8 -*-
import re

UNGUESSED_LETTER_PLACEHOLDER = '*'

def get_mask(word, guessed_letters):
    mask = [letter if letter in guessed_letters
            else UNGUESSED_LETTER_PLACEHOLDER
            for letter in word]
    return ''.join(mask)

def make_regex_for_mask(mask):
    # it can be more efficient if a sequence of * was replaced with "[A-ЯЁ]{n}"
    letter_pattern = "[А-ЯЁ]"
    regex = '^%s$' % mask.replace(UNGUESSED_LETTER_PLACEHOLDER, letter_pattern)
    return re.compile(regex)