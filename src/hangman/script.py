import word_provider
import guesser
import leader

FILENAME = "../../data/apellatives.txt"

wp = word_provider.FileWordProvider(FILENAME)
g = guesser.DeterminedHangmanGuesser(wp)
l = leader.HangmanLeader(g)

for word in wp.get_words():
    result = l.play(word)
    print "%s : %s (%s, %d attempts)" % (word, "WIN" if result[0] else "LOSE",
                                        result[1], result[2])

