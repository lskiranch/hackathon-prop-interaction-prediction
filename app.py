import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('click-prediction-model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print(type(request.form.values()))
    print(request.form.values())
    final_features = []
    for x in request.form.values():
        '''ANYONE BACHELOR COMPANY FAMILY'''
        print(final_features)
        if x == 'ANYONE':
            final_features.extend([1,0,0,0])
        elif x == 'BACHELOR':
            final_features.extend([0,1,0,0])
        elif x == 'COMPANY':
            final_features.extend([0,0,1,0])
        elif x == 'FAMILY': 
            final_features.extend([0,0,0,1])
            '''BOTH FOUR_WHEELER NONE TWO_WHEELER'''
        elif x == 'BOTH':
             final_features.extend([1,0,0,0])
        elif x == 'FOUR_WHEELER':
             final_features.extend([0,1,0,0])
        elif x == 'NONE':
             final_features.extend([0,0,1,0])
        elif x == 'TWO_WHEELER':
             final_features.extend([0,0,0,1])
        else:
            final_features.append(int(x))
    print('final:',final_features)
    prediction = model.predict([final_features])

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Expected clicks : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
