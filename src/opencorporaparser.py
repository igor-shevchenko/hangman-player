

class OpenCorporaDictionaryParser:
    def __init__(self, filename):
        self.filename = filename

    def extract(self, requirements):
        return (word for word in (self.get_words(self.extract_lines(requirements))))

    def extract_lines(self, requirements):
       return (line for line in open(self.filename) if requirements.are_satisfied_by(line))

    def get_words(self, lines):
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
