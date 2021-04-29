from mrjob.job import MRJob
from mrjob.step import MRStep
import re

REGEXP_PALAVRA = re.compile(r"[\w']+")

class MRDataMining(MRJob):

    def steps(self):
        return [
            MRStep(mapper = self.mapper_get_words, reducer = self.reducer_count_words),
            MRStep(mapper = self.mapper_make_counts_key, reducer = self.reducer_output_words)
        ]

    def mapper_get_words(self, _, line):
        palavras = REGEXP_PALAVRA.findall(line)
        for palavra in palavras:
            yield palavra.lower(), 1

    def reducer_count_words(self, palavra, values):
        yield palavra, sum(values)

    def mapper_make_counts_key(self, palavra, count):
        yield '%04d'%int(count), palavra

    def reducer_output_words(self, count, palavras):
        for palavra in palavras:
            yield count, palavra


if __name__ == '__main__':
    MRDataMining.run()

    
