#-*- coding: utf-8 -*-

import opencorporaparser

FILENAME = ''

requirements = opencorporaparser.ExtractionRequirements(
    required_tags=['NOUN', 'nomn', 'sing'],
    restricted_tags=['Abbr', 'Name', 'Surn', 'Patr', 'Geox', 'Trad', 'Orgn']
)

parser = opencorporaparser.OpenCorporaDictionaryParser(FILENAME)

apellatives = [word.replace('Ё', 'Е') for word in parser.extract(requirements)
                                        if word.find('-') == -1]
for word in set(apellatives):
    print word