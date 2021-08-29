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
	loaded_model = pickle.load(handle)

def fake_news_det(news):
    prediction = loaded_model.predict([news])
    return prediction

def fake_news_det_proba(news):
    prediction_proba = loaded_model.predict_proba([news])
    return prediction_proba

@app.route('/')
def main():
    return render_template('predictor.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/predictor', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        prediction = fake_news_det(message)
        print(prediction)
        prediction_proba = fake_news_det_proba(message)
        prediction_proba_2f = "{:.2f}".format(max(max(prediction_proba))*100)
        print(prediction_proba_2f)
        return render_template('predictor.html', prediction=prediction, prediction_proba=prediction_proba_2f)
    else:
        return render_template('predictor.html', prediction="Something went wrong")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    port=int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)