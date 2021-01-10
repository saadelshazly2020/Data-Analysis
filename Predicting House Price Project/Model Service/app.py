from flask import Flask, request, render_template,send_from_directory,jsonify
import pickle
from pathlib import Path
import pandas as pd
import numpy as np

app = Flask(__name__,template_folder='templates')
print('root: ',app.root_path)
#abspath = pathlib.Path('GBoost_model.pkl').absolute()
path_pkl = '{}/{}'.format( Path(__file__).parent.absolute() , 'GBoost_model.pkl')

with open(path_pkl, 'rb') as f:
    print(f)
    model = pickle.load(f)

@app.route('/')
def home():
    global df 
    df=pd.read_csv('{}/{}'.format( Path(__file__).parent.absolute() , 'olx_data_cleaned_for_model.csv'))
    return render_template('index.html')

@app.route('/cities',methods=['GET'])
def getCities():
    cities=list(df['location'].unique())
    return jsonify(cities)
@app.route('/compound',methods=['GET'])
def getCompounds():
    comp=list(df['Compound'].unique())
    return jsonify(comp)
@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

@app.route('/predict',methods=['POST'])
def predict():
    print(request.form['Area'])

    #features_list = [x for x in request.form.values()]

    dict_test={'Area':100,'Bathrooms':1,'Bedrooms':2,"Compound":"Not in Compound",'Furnished':0,'Level':3,'location':"Nasr City"}
    dict_test['Area']=request.form['Area']   
    dict_test['Bedrooms']=request.form['Bedrooms']
    dict_test['Bathrooms']=request.form['Bathrooms']
    dict_test['Level']=request.form['Level']
    dict_test['Compound']=request.form['Compound']
    dict_test['location']=request.form['location']
    dict_test['Furnished']=request.form['Furnished']
    columns = list(dict_test.keys())
    values = list(dict_test.values())
    arr_len = len(values)
    test_row=pd.DataFrame(np.array(values, dtype=object).reshape(1, arr_len), columns=columns)
    
    prediction = model.predict(test_row)
    output = round(prediction[0], 2)
    print(dict_test)
    return str('The Predicted Appartment Price: {:,.2f}'.format(output) ) #render_template('index.html', prediction_text='The Predicted Appartment Price: {:,.2f}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)