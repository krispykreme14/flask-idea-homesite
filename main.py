import requests
import json
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

def merge_covid_info_with_geojson():
  #geoJson data for state geometry from https://eric.clst.org/tech/usgeojson/
  with open('./templates/gz_2010_us_040_00_20m.json') as json_file:
    statesData = json.loads(json_file.read())
    response = requests.get(
      "https://api.covidtracking.com/v1/states/current.json")
    covid_data = response.json()
    for state_data in covid_data:
      state = state_data['state']
      full_state = state_abbrev_to_full(state)
      if full_state:
        ddd = [sd for sd in statesData['features']
               if sd['properties']['NAME'] == full_state]
        ddd[0]['properties'].update(state_data)
  return statesData


def state_abbrev_to_full(abbrev):
  us_state_abbrev = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
  }
  return us_state_abbrev.get(abbrev)

@app.route('/map/')
def map_route():
  data = merge_covid_info_with_geojson()
  return render_template("map.html", data=data)


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

@app.route('/Easter')
def Easter_route():
  return render_template("Easter.html", projects=projects.setup())

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
