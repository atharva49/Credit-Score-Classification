# Credit-Score-Classification deployed on FLASK web service framework
Banks and credit card companies calculate your credit score to determine your creditworthiness.
There are three credit scores that banks and credit card companies use to label their customers:  Good Standard Poor A person with a good credit score will get loans from any bank and financial institution.
It helps banks and credit card companies immediately to issue loans to customers with good creditworthiness and reduce the chances of fraud from its culstomers.
I have used Random Forest algorithm to classify the customer based on their credit history in the database. 

The following model is deployed on FLASK webservice.

This project is a Flask-based web application that classifies credit scores using a machine learning model. Users can input their age, income, and loan amount to receive a prediction of their credit score status (good or bad).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Project Details](#project-details)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

The goal of this project is to provide a simple web interface for predicting credit scores based on user inputs. The application uses a logistic regression model trained on a hypothetical dataset. This project aims to demonstrate how machine learning models can be integrated into web applications to provide real-time predictions.

## Features

- User-friendly web interface for inputting data.
- Real-time prediction of credit score status.
- Preprocessing and scaling of input data for accurate predictions.
- Clear and informative result presentation.

## Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- Numpy
- HTML
- CSS

## Project Details

### Data Collection

The application uses a hypothetical dataset (`credit_data.csv`) containing features such as age, income, and loan amount, which are relevant for credit score classification. The dataset is used to train a logistic regression model to distinguish between good and bad credit scores.

### Data Preprocessing

The data is preprocessed to handle missing values, scale numerical features, and split into training and testing sets. The preprocessing steps ensure the model performs well on unseen data.

### Machine Learning Model

A logistic regression model is chosen for its simplicity and effectiveness in binary classification tasks. The model is trained using the preprocessed data, and its performance is evaluated to ensure accuracy.

### Web Application

The Flask framework is used to create a web application that allows users to input their data and receive credit score predictions. The application consists of two main pages:
- **Home Page**: A form where users can input their age, income, and loan amount.
- **Result Page**: Displays the prediction result based on the user input.

### Deployment

The application is designed to be run locally. Detailed instructions are provided to set up the environment, train the model, and start the Flask server.

## Contributing


The following graphs are used to get idea relational between the variables

Credit Scores Based on Occupation
![Credit Scores Based on Occupation](https://user-images.githubusercontent.com/56105570/215379989-38d2bdd3-8ad8-433a-bdda-2d1a71c8ae97.png)


Credit Scores Based on Annual Income
![Credit Scores Based on Annual Income](https://user-images.githubusercontent.com/56105570/215380107-791b9f8e-cf9a-4bd6-9f33-6715f8578ce9.png)


Credit Scores Based on Number of Bank Accounts
![Credit Scores Based on Number of Bank Accounts](https://user-images.githubusercontent.com/56105570/215380130-0d9459e4-6426-4d72-9c1f-22fa8dc238ca.png)


Credit Scores Based on Number of Credit cards
![Credit Scores Based on Number of Credit cards](https://user-images.githubusercontent.com/56105570/215380148-a359fec1-e51c-4e5a-9a37-88651b438c18.png)


Credit Scores Based on Monthly Inhand Salary
![Credit Scores Based on Monthly Inhand Salary](https://user-images.githubusercontent.com/56105570/215380176-a56f0239-1349-4a45-877d-eb31ebc0d49b.png)


Credit Scores Based on the Average Interest rates
![Credit Scores Based on the Average Interest rates](https://user-images.githubusercontent.com/56105570/215380201-56cdacbd-9a4b-462d-bb5f-b42e389b2a59.png)


Credit Scores Based on Number of Loans Taken by the Person
![Credit Scores Based on Number of Loans Taken by the Person](https://user-images.githubusercontent.com/56105570/215380216-768f15dd-a510-443f-b321-4175a7f40176.png)


Credit Scores Based on Average Number of Days Delayed for Credit card Payments
![Credit Scores Based on Average Number of Days Delayed for Credit card Payments](https://user-images.githubusercontent.com/56105570/215380232-291acff4-408b-4943-b141-edc6a5e0d976.png)


Credit Scores Based on Number of Delayed Payments
![Credit Scores Based on Number of Delayed Payments](https://user-images.githubusercontent.com/56105570/215380249-3e4be481-081a-4127-8e02-e38d6b624595.png)


Credit Scores Based on Outstanding Debt
![redit Scores Based on Outstanding Debt](https://user-images.githubusercontent.com/56105570/215380269-2fa6a0b1-8c35-4e43-b489-49f1b02e0aaa.png)


Credit Scores Based on Credit Utilization Ratio
![Credit Scores Based on Credit Utilization Ratio](https://user-images.githubusercontent.com/56105570/215380308-e70c4dba-ae78-4bf2-ab21-f0700f18b528.png)


Credit Scores Based on Credit History Age
![Credit Scores Based on Credit History Age](https://user-images.githubusercontent.com/56105570/215380324-ae37cb59-7510-4661-832b-f650ffd05cf2.png)


Credit Scores Based on Total Number of EMIs per Month
![Credit Scores Based on Total Number of EMIs per Month](https://user-images.githubusercontent.com/56105570/215380347-5acac4e8-b9b2-4da8-bbc5-cded700dc7a5.png)


Credit Scores Based on Amount Invested Monthly
![Credit Scores Based on Amount Invested Monthly](https://user-images.githubusercontent.com/56105570/215380392-8ff5ad65-fa39-4517-a1d9-a4b3e990e5a4.png)


Credit Scores Based on Monthly Balance Left
![Credit Scores Based on Monthly Balance Left](https://user-images.githubusercontent.com/56105570/215380411-ff96b92f-2d8c-4adb-a8e6-ca90ff5a7341.png)


The following co-relation heat-map is used to select the variables for training the model.
![CreditScoreClassificationOutput](https://user-images.githubusercontent.com/56105570/215377794-be889693-a577-467d-8593-4d450ace89ed.png)
