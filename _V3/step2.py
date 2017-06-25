#!/usr/bin/env python3
import os
import redis
import json
from flask import Flask, render_template, redirect, request, url_for, make_response

if 'VCAP_SERVICES' in os.environ:
    VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
    CREDENTIALS = VCAP_SERVICES["rediscloud"][0]["credentials"]
    r = redis.Redis(host=CREDENTIALS["hostname"], port=CREDENTIALS["port"], password=CREDENTIALS["password"])
else:
    r = redis.Redis(host='127.0.0.1', port='6379')

app = Flask(__name__)

@app.route('/')
def survey():
    resp = make_response(render_template('survey.html'))
    return resp

@app.route('/suthankyou.html', methods=['POST'])
def suthankyou():

    d = request.form['division']
    s = request.form['state']
    f = request.form['feedback']

    print ("Division is " + d)
    print ("State is " + s)
    print ("Feedback: " + f)
	
    resp = """
    <h3> - THANKS FOR TAKING THE SURVEY - </h3>
    Your answers were:<br>
    Division : {}<br>
    State    : {}<br>
    Feedback : {}<br>
    <a href="/"><h3>Back to main menu</h3></a>
    """.format(d, s, f)
    return resp
	
if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', \
                port=int(os.getenv('PORT', '5000')), threaded=True)
