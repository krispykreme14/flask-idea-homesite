import requests
import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
  data = get_current_state_data()
  return render_template("home.html", data=data)

def get_current_state_data():
  response = requests.get("https://api.covidtracking.com/v1/states/current.json")
  remotedata = response.json()
  return remotedata

@app.route('/map/')
def map_route():
  return render_template("map.html")


#connects /hello path of server to render NY.html
@app.route('/NY/')
def NY_route():
  return render_template("NY.html", projects=projects.setup())

#connects /historyofcomedy path of server to render NJ.html
@app.route('/NJ/')
def NJ_route():
  return render_template("NJ.html", projects=projects.setup())

#connects /knock path of server to render FL.html
@app.route('/FL')
def FL_route():
  return render_template("FL.html", projects=projects.setup())

#connects /iniyaa path of server to render MA.html
@app.route('/MA')
def MA_route():
  return render_template("MA.html", projects=projects.setup())

#connects /ketki path of server to render OR.html
@app.route('/OR')
def OR_route():
  return render_template("OR.html", projects=projects.setup())

#connects /ava path of server to render CA.html
@app.route('/CA')
def CA_route():
  return render_template("CA.html", projects=projects.setup())

#connects /lucas path of server to render TX.html
@app.route('/TX')
def TX_route():
  return render_template("TX.html", projects=projects.setup())

#connects /submit path of server to render submit.html
@app.route('/submit')
def submit_route():
  return render_template("submit.html", projects=projects.setup())

@app.route("/playground")
def playground_route():
  return render_template("playground.html")

@app.route("/Signup")
def Signup_route():
  return render_template("Signup.html")

if __name__ == "__main__":
  app.run(debug=True, port='3000', host='127.0.0.1') #192.168.1.228
