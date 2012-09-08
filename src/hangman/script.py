#-*- coding: utf-8 -*-

import word_provider
import guesser
import leader

FILENAME = "../../data/apellatives.txt"

wp = word_provider.FileWordProvider(FILENAME, 'UTF-8')
g = guesser.DeterminedHangmanGuesser(wp)
l = leader.HangmanLeader(g)
log = open('log.txt', 'w')

for word in wp.get_words():
    result = l.play(word)
    print "%s : %s (%s, %d attempts)" % (word, "WIN" if result[0] else "LOSE",
                                        result[1], result[2])