import os
import redis
from flask import Flask, render_template, redirect, request, url_for, make_response

#r = redis.Redis(host='123.12.148.95', port='15379', password='ABCDEFG1231LQ4L')

app = Flask(__name__)

@app.route('/')
def survey():
    resp = make_response(render_template('survey.html'))
    return resp

@app.route('/suthankyou.html', methods=['POST'])
def suthankyou():

    ## This is how you grab the contents from the form
    f = request.form['feedback']

    ## Now you can now do someting with variable "f"
    print "The feedback received was:"
    print f

    resp = """
    <h3> - THANKS FOR TAKING THE SURVEY - </h3>
    <a href="/"><h3>Back to main menu</h3></a>
    """

    return resp
	
if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', \
                port=int(os.getenv('PORT', '5000')), threaded=True)
