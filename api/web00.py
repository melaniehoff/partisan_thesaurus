#!flask/bin/python

# Import Flask:
from flask import Flask, render_template, request, url_for, jsonify
import gensim
from gensim.models import word2vec
import logging
import os
from flask_cors import CORS, cross_origin


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
print "main in word200"
sentencesR = MySentences('allRight') # a memory-friendly iterator
modelR = gensim.models.Word2Vec(sentencesR, min_count=3, size=160) # freq of words and number of vectors

sentencesL = MySentences('allLeft') # a memory-friendly iterator
modelL = gensim.models.Word2Vec(sentencesL, min_count=3, size=160) # freq of words and number of vectors


#################################################################
#################################################################
#################################################################
#################################################################
#################################################################

# Initialize Flask app:
app = Flask(__name__)
CORS(app)

# Define default route:
@app.route('/')
@app.route('/index')
def index():
    # Render index page:
    return render_template( 'index.html' )


# Define form submission route:
@app.route('/get_synonymsR', methods=['GET'])
def getSynR():
    # Get user's name from submitted form data:
    word_string = request.args.get('word_entry')
    print word_string
    # Call the "external function" on the user-submitted data:

    try:
        synonym_list = modelR.most_similar(positive=[word_string], topn=5)
        return jsonify(synonym_list)
    except:
        return ""


@app.route('/get_synonymsL', methods=['GET'])
def getSynL():
    # Get user's name from submitted form data:
    word_string = request.args.get('word_entry')
    print word_string
    # Call the "external function" on the user-submitted data:
    try:
        synonym_list = modelL.most_similar(positive=[word_string], topn=5)
        return jsonify(synonym_list)
    except:
        return ""


# Run app:
if __name__ == '__main__':
    # word2v00.run()
    app.run( host='0.0.0.0', port=9998, debug=False )
