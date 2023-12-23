source 
https://studygyaan.com/data-science/deploy-machine-learning-model-in-flask-project

python app.py

import pickle

# Load the model from the .pkl file
with open('linear_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)