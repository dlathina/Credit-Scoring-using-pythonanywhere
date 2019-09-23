# Import libraries
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import numpy as np


app = Flask(__name__)

# Load the model From model.pkl
model = joblib.load(open('/home/dwilarasathina/mysite/model_randomforest.pkl','rb'))

#Untuk menerima masukan API
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    pred=[]
    k=1;

    for i in data:
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([np.array([i['PAY_1'],i['PAY_2'],i['LIMIT_BAL']])])

        # Take the first value of prediction
        output = int(prediction[0])
        out = 'Approved' if output==0  else 'Not Approved, Credit must be stopped'
        # print result to pred
        pred.append(k)
        pred.append(out)
        k=k+1

    return jsonify(pred)