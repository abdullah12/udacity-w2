
from flask import Flask, render_template,redirect,request,session,abort
from Udacian import Udacian 

a = Udacian('ali','dammam','Elham','fullstack','ontrack')
b = a.get_udacian()

app = Flask(__name__)
 
@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('test.html')
    else:
        a = request.form
        udacian = Udacian(a['name'],a['city'],a['enrollment'],a['nanodegree'],a['status'])
        return render_template('test.html',name=udacian.get_udacian())
    


if __name__ == '__main__':
    app.run(port=3000,host='0.0.0.0', debug=True)