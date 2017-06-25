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
    #### It gets stored as 'str'
    ##print (type(d))

    print ("Division is " + d)
    print ("State is " + s)
    print ("Feedback: " + f)

    print ("Storing the survey now")
    r.hmset('newsurvey',{'division':d,'state':str(s),'feedback':f})

    #### When retrieved is 'bytes'
    ##print (type(r.hget('newsurvey','division')))
    
    print ("--------------------------")
    print ("Reading it back from Redis")
    ####Need to use str(bytes_string, 'utf-8') to display properly without b''
    print ("Division : ", str(r.hget('newsurvey','division'),'utf-8'))
    print ("State    : ", str(r.hget('newsurvey','state'),'utf-8'))
    print ("Feedback : ", str(r.hget('newsurvey','feedback'),'utf-8'))
	
    resp = """
    <h3> - THANKS FOR TAKING THE SURVEY - </h3>
    """
    return resp
	
if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', \
                port=int(os.getenv('PORT', '5000')), threaded=True)
