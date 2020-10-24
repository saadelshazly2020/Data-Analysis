import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pathlib
from pathlib import Path
import os
import pandas as pd

app = Flask(__name__,template_folder='templates')
print('root: ',app.root_path)
#abspath = pathlib.Path('GBoost_model.pkl').absolute()
path_pkl = '{}\\{}'.format( Path(__file__).parent.absolute() , 'GBoost_model.pkl')
path_root = Path(__file__).parent.absolute() 

#print(path_root)
#model = pickle.load(open(path_pkl, 'rb'))
with open(path_pkl, 'rb') as f:
    print(f)
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features_list = [x for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    #output = round(prediction[0], 2)
    dict_test={'Area':100,'Bathrooms':1,'Bedrooms':2,"Compound":"Not in Compound",'Furnished':0,'Level':3,'location':"Nasr City"}
    columns = list(dict_test.keys())
    values = list(dict_test.values())
    arr_len = len(values)
    test_row=pd.DataFrame(np.array(values, dtype=object).reshape(1, arr_len), columns=columns)
    test_row['Area']=features_list[0]
    test_row['Bedrooms']=features_list[1]
    test_row['Bathrooms']=features_list[2]
    test_row['Level']=features_list[3]
    test_row['Compound']=features_list[4]
    test_row['location']=features_list[5]
    test_row['Furnished']=features_list[6]
    prediction = model.predict(test_row)
    output = round(prediction[0], 2)
    #print(test_row)
    return render_template('index.html', prediction_text='The Predicted Appartment Price: {:,.2f}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
if __name__ == "__main__":
    app.run(debug=True)