import numpy as np 
import pandas as pd 
from sklearn import linear_model 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#X is indipendent variable 
#y contain the target variable (price)

data = pd.read_excel('carpriceprediction.xlsx')

X = data[[ 'godina_proizvodnje', 'predjena_kilometraza',
       'kw_snaga', 'cm3_kubikaza']]
y = data['cena']

# split dataset into training and testing sets using sklearns train test split function
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#select feauture namese for X to avoid the warning message:
feauture_names = ['godina_proizvodnje', 'predjena_kilometraza',
       'kw_snaga', 'cm3_kubikaza']

X_train.columns = feauture_names
X_test.colmns = feauture_names



#now you can build linear regression model usin sklearn LinearRegression class:
model = LinearRegression()

model.fit(X_train, y_train)

#once the model trained you can use to make prediction 

y_pred = model.predict(X_test)

#to evaulate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

#print("Mean Squared Error: ", mse)
#print("R-squared: ", r2)
#save pickle trained model to a .pkl file 

import pickle 
with open('car_model.pkl', 'wb') as file:
    pickle.dump(model, file)


    
































#