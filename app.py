#Importing the Libraries
import numpy as np
from flask import Flask, request,render_template
from flask_cors import CORS
import os
import joblib as jb
import pickle
import flask
import os
import newspaper
from newspaper import Article
import urllib
import nltk
# nltk.download('punkt')

app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__, template_folder='templates')

with open('yslc-jordan-model.pickle', 'rb') as handle:
	model = pickle.load(handle)

@app.route('/')
def main():
    return render_template('index.html')

def fake_news_det(news):
    pred = model.predict([news])
    return pred

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        pred = fake_news_det(message)
        print(pred)
        return render_template('index.html', prediction=pred)
    else:
        return render_template('index.html', prediction="Something went wrong")

if __name__=="__main__":
    port=int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)