from token import RIGHTSHIFTEQUAL
from flask import Flask,request,render_template
app = Flask(__name__)
 
@app.route('/')
def input_form():
    return render_template('input_form.html')

@app.route('/process', methods=['POST'])
def process_form():
   data = {
   'name' : request.form['name'],
   'mname' : request.form['mname'],
   'lname' : request.form['lname'],
   'id' : request.form['id'],
   'program': request.form['program'],
   'intake': request.form['intake'],
   'language': request.form['language'],
   'date': request.form['date']}
   return render_template('result.html', data=data)
   
if __name__ == '__main__':
    app.run(host="127.0.0.9", port=8080, debug=True)