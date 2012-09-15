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
    results = []
    for x in xrange(20):
        results.append(l.play(word)[2])
    print >> log, "%s\t%s\t%s" %(word, results, len([res for res in results if res >= 10]))