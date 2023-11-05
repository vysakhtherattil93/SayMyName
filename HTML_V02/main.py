from token import RIGHTSHIFTEQUAL
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/')
# def response_form(): #Use when we are using actual URL
def process_form():
    data={"data":{
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
        ]
    },
    "results": [
        {
            "student_id": 2004930402,
            "votes": 1,
            "id": 1,
            "name_selection": "V-IH-JH-IY",
            "name": "vijay",
            "show": True
        }
    ]
    }

    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(host="127.0.0.9", port=8080, debug=True)

#Added to git