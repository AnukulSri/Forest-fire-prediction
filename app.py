from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))



@app.route('/')
def hello_world():
    return render_template("forest.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    print(predict)
    output='{0:.{1}f}'.format(prediction[0][1], 2)
    print(output)

    if output>str(0.5): # this means that if output is greater than 50% than prift this message 
        return render_template('forest.html',pred='Your Forest is in Danger.\n Probability of fire occuring is {}'.format(output))
    else:
        return render_template('forest.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output))








if __name__ == '__main__':
    app.run(debug=True)
