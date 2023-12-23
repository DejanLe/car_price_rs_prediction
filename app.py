from flask import Flask, render_template, request
import joblib
import pickle

app = Flask(__name__)





# Load the trained machine learning model
#model = joblib.load('linear_regression_model.pkl')

# Load the model from the .pkl file

with open('car_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None
    if request.method == 'POST':
        # Extract input data from the form
        godina_proizvodnje = int(request.form['godina_proizvodnje'])
        predjena_kilometraza = int(request.form['predjena_kilometraza'])
        kw_snaga = int(request.form['kw_snaga'])
        cm3_kubikaza = int(request.form['cm3_kubikaza'])
        

        # Prepare the input data for prediction
        new_data = [[godina_proizvodnje, predjena_kilometraza, kw_snaga, cm3_kubikaza]]

        # Perform prediction
        predicted_price = loaded_model.predict(new_data)[0]
        prediction_result = round(predicted_price, 2)

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)