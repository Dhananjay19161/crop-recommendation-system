# prediction function
from flask import Flask,render_template
from flask import request;
import joblib;
import numpy as np;
app = Flask(__name__)
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 12)
    loaded_model = joblib.load("model.pkl")
    result = loaded_model.predict(to_predict)
    return result[0]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        # to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)       
        return render_template("result.html", prediction = result)

if __name__ == "__main__":
    app.run()
