#!flask/bin/python

# Import Flask:
from flask import Flask, render_template, request, url_for, jsonify
import gensim
from gensim.models import word2vec
import logging
import os
from flask_cors import CORS, cross_origin


modelR = gensim.models.Word2Vec.load("models/saved_modelR")
modelL = gensim.models.Word2Vec.load("models/saved_modelL")


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



@app.route('/get_phraseL', methods=['GET'])
def getphraseL():
    # Get user's name from submitted form data:
    phrase_string = request.args.get('phrase_entry')
    print phrase_string
    ## Call the "external function" on the user-submitted data:
    # try:
    #     synonym_list = modelL.most_similar(positive=[word_string], topn=5)
    #     return jsonify(synonym_list)
    # except:
    return phrase_string



# Run app:
if __name__ == '__main__':
    # word2v00.run()
    app.run( host='0.0.0.0', port=9998, debug=False )
