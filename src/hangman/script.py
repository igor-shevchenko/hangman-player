#-*- coding: utf-8 -*-

import word_provider
import guesser
import leader
import random

FILENAME = "../../data/apellatives.txt"

wp = word_provider.GroupingByLengthFileWordProvider(FILENAME, 'UTF-8')
g = guesser.UndeterminedHangmanGuesser(wp, random.Random())
l = leader.HangmanLeader(g)
log = open('log.txt', 'w')

for word in wp.get_words():
    result = []
    for i in xrange(10):
        result.append(l.play(word)[2])
    result = map(str,sorted(result))
    print "%s\t\t%s" %(word, '\t'.join(result))
