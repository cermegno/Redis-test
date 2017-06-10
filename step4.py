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

    d = request.form['division']
    s = request.form['state']
    f = request.form['feedback']

    print "Division is " + d
    print "State is " + s
    print "Feedback: " + f

    Counter = r.incr('new_counter')
    print "the counter is now: ", Counter
    ## Create a new key that includes the counter
    newsurvey = 'review' + str(Counter)
    print "the name of the new key is: " + newsurvey

    print "Storing the survey now"
    print "----------------------"
    ## Now the key name is the content of the variable newsurvey
    r.hmset(newsurvey,{'division':d,'state':s,'feedback':f})

    print "Reading it back from Redis"
    print "Division : " + r.hget(newsurvey,'division')
    print "State    : " + r.hget(newsurvey,'state')
    print "Feedback : " + r.hget(newsurvey,'feedback')
	
    resp = """
    <h3> - THANKS FOR TAKING THE SURVEY - </h3>
    """
    return resp
	
if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', \
                port=int(os.getenv('PORT', '5000')), threaded=True)
