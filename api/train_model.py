#!flask/bin/python

# Import Flask:
import gensim
from gensim.models import word2vec
import logging
import os


# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# model = None
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


# print model.most_similar(positive=['tradition'], topn=5)
# def run():
print "training model..."
sentencesR = MySentences('allRight') # a memory-friendly iterator
modelR = gensim.models.Word2Vec(sentencesR, min_count=3, size=160) # freq of words and number of vectors

sentencesL = MySentences('allLeft') # a memory-friendly iterator
modelL = gensim.models.Word2Vec(sentencesL, min_count=3, size=160) # freq of words and number of vectors

print "saving model..."

modelR.save("models/saved_modelR")
modelL.save("models/saved_modelL")

