

class OpenCorporaDictionaryParser:
    def __init__(self, filename):
        self.filename = filename

    def extract(self, requirements):
        lines = self.extract_lines_that_satisfy(requirements)
        return (word for word in (self.get_words_from(lines)))

    def extract_lines_that_satisfy(self, requirements):
       return (line for line in open(self.filename) if requirements.are_satisfied_by(line))

    def get_words_from(self, lines):
        return (line.split('\t')[0] for line in lines)



class ExtractionRequirements:
    def __init__(self, required_tags = None, restricted_tags = None):
        self.required_tags = required_tags or []
        self.restricted_tags = restricted_tags or []

    def are_satisfied_by(self, line):
        for tag in self.required_tags:
            if line.find(tag) == -1:
                return False
        for tag in self.restricted_tags:
            if line.find(tag) != -1:
                return False
        return True
