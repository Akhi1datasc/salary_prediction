from flask import Flask, render_template, request, jsonify
import pickle
app = Flask(__name__)

@app.route("/")
def fun1():
    return render_template("salary_pred.html")
@app.route("/predict",methods=['POST'])
def fun2():
    name = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('salary_model.pkl','rb'))
    sal = round(mymodel.predict([[exp]])[0],2)
    return "<h1>Hi {}, Your predicted salary is {}</h1>".format(name, sal)
if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)