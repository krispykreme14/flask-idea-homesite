from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
import projects 
##!!! MUST PIP INSTALL ALL DEPENDANCIES INCLUDING email-validator
#projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/

#create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'I<+g/94L$}0GXOf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
# IMPORTANT - GENERATES CSRF TOKEN
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model): #Creates columns inside of the database
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True) #username column
  email = db.Column(db.String(50), unique=True) #email column
  password = db.Column(db.String(80)) #password column

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

#LOGIN, REGISTER, DASHBOARD, LOGOUT

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
    #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

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
    return render_template('usercreatedredirect.html') #If you do not want to go to redirect page to confirm change this
    # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
  return render_template('signup.html', form=form)



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
  app.run(debug=True, port='3000', host='127.0.0.1') #192.168.1.228
