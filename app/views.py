from flask import render_template
from app import app
from vmail import testmail

@app.route("/")
def index():
    testmail()
    return render_template('testmail.html')

# @app.route("/submit_application", methods=['POST'])
# def submit_application(): 
