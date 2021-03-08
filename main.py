import json

import requests
# import projects #projects definitions are placed in different file
from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, Length


import projects

##!!! MUST PIP INSTALL ALL DEPENDANCIES INCLUDING email-validator
# projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/

# create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'I<+g/P2N$}0GXOf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
# IMPORTANT - GENERATES CSRF TOKEN
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager.login_view = 'login'

SESSION_COOKIE_SECURE = False

a, b, c, d = '', '', '', ''
correct_ans = []
given_ans = []


class User(UserMixin, db.Model):  # Creates columns inside of the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)  # username column
    email = db.Column(db.String(50), unique=True)  # email column
    password = db.Column(db.String(80))  # password column


class QuizForm(FlaskForm):
    choice = RadioField('Answer', choices=[(a, 'A'), (b, 'B'), (c, 'C'), (d, 'D')])


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


# connects default URL of server to render home.html
@app.route('/')
def home_route():
    data = get_current_state_data()
    return render_template("home.html", data=data)


def get_current_state_data():
    response = requests.get("https://api.covidtracking.com/v1/states/current.json")
    remotedata = response.json()
    return remotedata


def merge_covid_info_with_geojson():
    # geoJson data for state geometry from https://eric.clst.org/tech/usgeojson/
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


def get_state_images(state):
    state_images = {
        'AL': 'Alabama',
        'AK': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fgeology.com%2Fstate-map%2Falaska.shtml&psig=AOvVaw375d8Y37lXves10XooyhdG&ust=1615054548306000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDnjJfhme8CFQAAAAAdAAAAABAE',
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
    return state_images.get(state.lower())


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


# connects /hello path of server to render NY.html
@app.route('/NY/')
def NY_route():
    return render_template("NY.html", projects=projects.setup())


# connects /historyofcomedy path of server to render NJ.html
@app.route('/NJ/')
def NJ_route():
    return render_template("NJ.html", projects=projects.setup())


# connects /state/:code to render dynamic state detailed data
@app.route('/state/<state>')
def state_route(state):
    response = requests.get("https://api.covidtracking.com/v1/states/" + state + "/current.json")
    remotedata = response.json()

    data = {'name': state, 'coviddata': remotedata, 'mapimage': get_state_images(state)}
    return render_template("State.html", data=data)


# connects /knock path of server to render FL.html
@app.route('/FL')
def FL_route():
    return render_template("FL.html", projects=projects.setup())


# connects /iniyaa path of server to render MA.html
@app.route('/MA')
def MA_route():
    return render_template("MA.html", projects=projects.setup())


# connects /ketki path of server to render OR.html
@app.route('/OR')
def OR_route():
    return render_template("OR.html", projects=projects.setup())


@app.route('/Easter')
def Easter_route():
    return render_template("Easter.html", projects=projects.setup())


# connects /ava path of server to render CA.html
@app.route('/CA')
def CA_route():
    return render_template("CA.html", projects=projects.setup())


# connects /lucas path of server to render TX.html
@app.route('/TX')
def TX_route():
    return render_template("TX.html", projects=projects.setup())


# connects /submit path of server to render submit.html
# @app.route('/submit')
# def submit_route():
#   return render_template("submit.html", projects=projects.setup())


# @app.route('/covidrisk', methods=['post', 'get'])
# def covidrisk_route():
#   form = CovidForm()
#  if form.validate():
#   print(form.example.data)
# else:
# print(form.errors)

# return render_template('quiz.html', project=projects.setup(), form=form)
@csrf.exempt
@app.route('/quiz')
def main():
    form = QuizForm(meta={'csrf': False})
    quest = ["What is the highest risk tier?", "What is the safest activity to do in quarantine?", "When should you "
                                                                                                   "wear a mask?",
             "What country currently has the most covid cases?"]
    given_ans.clear()
    global correct_ans
    correct_ans = ["Purple", "Go on a walk with a mask on",
                   "When you are outside your house and may interact with other people", "USA"]
    options = [
        ["Purple", "Orange", "Red", "Yellow"],
        ["Eat at a restaurant with indoor dining", "Go on a walk with a mask on",
         "Eat at a restaurant with outdoor dining", "Go to a party with 100 people"],
        ["Always", "Never", "When you are outside your house and may interact with other people",
         "When you feel like it"],
        ["Brazil", "Australia", "Kazakhstan", "USA"]]

    print(session['csrf_token'] )
    return render_template('quiz.html', quest=quest, correct_ans=correct_ans, options=options, form=form)

@csrf.exempt
@app.route('/submit', methods=['POST'])
def submit_form():
    count = 0
    new = []
    for i in range(4):
        given_ans.append(request.form[str(i)])
        if request.form[str(i)] == correct_ans[i]:
            count += 1
            new.append(1)
        else:
            new.append(0)
    msg = ''
    if count < 2:
        msg = "Poor Result...Shame on You"
    elif count > 3:
        msg = "Excellent Result...Your Parents Must Be Proud"
    else:
        msg = "NICE ONE"

    print(session['csrf_token'] )
    return render_template('submit.html', count=count, given_ans=given_ans, correct_ans=correct_ans, msg=msg)


@app.route("/playground")
def playground_route():
    return render_template("playground.html")


# @app.route("/Signup")
# def Signup_route():
#   return render_template("Signup.html")

# LOGIN, REGISTER, DASHBOARD, LOGOUT

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return render_template('invalid.html', form=form)
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        # redirect to page when user is created
        return render_template(
            'usercreatedredirect.html')  # If you do not want to go to redirect page to confirm change this
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('Signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port='3000', host='127.0.0.1')  # 192.168.1.228
