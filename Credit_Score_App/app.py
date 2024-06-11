from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form['age']
    income = request.form['income']
    loan_amount = request.form['loan_amount']

    input_features = np.array([[age, income, loan_amount]])
    input_features = scaler.transform(input_features)

    prediction = model.predict(input_features)
    prediction_text = 'Good Credit Score' if prediction == 1 else 'Bad Credit Score'

    return render_template('result.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
