#-*- coding: utf-8 -*-

import opencorporaparser

FILENAME = '../data/dict.opcorpora.txt'

requirements = opencorporaparser.ExtractionRequirements(
    required_tags=['NOUN', 'nomn', 'sing'],
    restricted_tags=['Abbr', 'Name', 'Surn', 'Patr', 'Geox', 'Trad', 'Orgn']
)

parser = opencorporaparser.OpenCorporaDictionaryParser(FILENAME)

count = 0

apellatives = [word.replace('Ё', 'E') for word in parser.extract(requirements)
                                        if word.find('-') == -1]
for word in set(apellatives):
    print word