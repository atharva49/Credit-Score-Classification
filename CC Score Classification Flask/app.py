# import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
import pickle
from flask import Flask, request, jsonify,render_template


#Create Flask App
app = Flask(__name__)

#Load the pickle model
model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def Home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict():

    creditworthiness = {1:'Good',2:'Standard',3:'Poor'}

    Annual_Income = request.form.get("Annual_Income")
    Monthly_Inhand_Salary= request.form.get("Monthly_Inhand_Salary")
    Num_Bank_Accounts = request.form.get("Num_Bank_Accounts")
    Num_Credit_Card = request.form.get("Num_Credit_Card")
    Interest_Rate = request.form.get("Interest_Rate")
    Num_of_Loan = request.form.get("Num_of_Loan")
    Delay_from_due_date = request.form.get("Delay_from_due_date")
    Num_of_Delayed_Payment = request.form.get("Num_of_Delayed_Payment")
    Credit_Mix = request.form.get("Credit_Mix")
    Outstanding_Debt = request.form.get("Outstanding_Debt")
    Credit_History_Age = request.form.get("Credit_History_Age")
    Monthly_Balance = request.form.get("Monthly_Balance")

    features = np.array([[Annual_Income,Monthly_Inhand_Salary,Num_Bank_Accounts,Num_Credit_Card,Interest_Rate,Num_of_Loan,Delay_from_due_date,Num_of_Delayed_Payment,Credit_Mix,Outstanding_Debt,Credit_History_Age,Monthly_Balance]])
    prediction = model.predict(features)
    
    return render_template("prediction_result.html",prediction_text = f'The customer has {creditworthiness.get(prediction[0])} credit worthiness')


if __name__ == "__main__":
    app.run(debug=True)