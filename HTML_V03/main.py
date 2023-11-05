from flask import Flask,request,render_template,make_response,json,redirect,url_for
app = Flask(__name__)

@app.route('/')
def process_form():
    data = {"data":{
        "student_id": 2004930410,
        "first_name": "vijay bhaskar",
        "last_name": "bonthu",
        "full_name": "vijay bhaskar bonthu",
        "first_name_p_eng": [
            ["V-J-Y"],
            ["V-JI-Y"],
            ["VI-JI-Y"]
        ],
        "first_name_p": [
            "V-IH-JH-IY",
            "B-AH-S-K-AA-R"
        ],
        "last_name_p_eng": ["B-O-N-THU"],
        "last_name_p": [
            "B-AA-N-TH-UW"
        ]}}
    return render_template('table.html',data = data)

@app.route('/result', methods=['POST'])
def result(request):
   option = request.form['option']
   return render_template('table_result.html', option = option)
 
if __name__ == '__main__':
    app.run(host="127.0.0.9", port=8080, debug=True)