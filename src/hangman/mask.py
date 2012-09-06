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
    unguessed_letter_pattern = "[%s]" % allowed_letters
    if mask == ALL_WORDS_MASK:
        regex = '^%s+$' % unguessed_letter_pattern
    else:
        placeholder_count = 0
        regex = '^'
        for char in mask:
            if char == UNGUESSED_LETTER_PLACEHOLDER:
                placeholder_count += 1
            else:
                if placeholder_count > 0:
                    regex = '%s%s{%d}' % (regex, unguessed_letter_pattern, placeholder_count)
                    placeholder_count = 0
                regex += char
        if placeholder_count > 0:
            regex = '%s%s{%d}' % (regex, unguessed_letter_pattern, placeholder_count)
        regex += '$'
    return re.compile(regex, re.MULTILINE)