# Welcome to our COVID information site.

<h2>Website Overview:</h2>
This website is a COVID 19 Website designed to make sure you can take appropriate precautitons to stay safe during this global pandemic. The home page contains a table which is the output of a RestAPI. This table provides some of the most important COVID stats in all 50 states. When you click on a state, it takes you to an individual state page that contains the COVID stats for that specific state. In the navigation bar, you can see that there are multiple pages. The map page is interactive and has additional covid stats rgarding each state but in a geographical view for a better understanding of the severity of covid in different states. The different colors represent the varying number of cases in different states. There is also a surprise dropdown, which contains a link to a California page, and if you click on the California image, you will be directed to our easter egg. Another section is the sighnup section. Those who create an account and log in get directed to a new page, which contains the link to our COVID trivia quiz. This quiz, which utilizes Flask forms, tells the viewer how knowledgeable they are about covid precautitons.  

<h2>How to acces COVID information site:</h2>
Link to website: http://p4donsabcd.cf/
Link to Easter Egg file: http://p4donsabcd.cf/Easter
To use simply click the links in the nav bar! This website was designed with ease of navigation in mind! Enjoy learning about COVID 19 and stay safe!!!

# Completed Tickets!
<h2> COVID Data REST API: by Ketki</h2> <br>
This api pulls data from a json formatted file, and it displays the data on the homescreen of the website. The Json file contains lots of data for all 50 states, but I have only displayed key categories of data in the table. The table also uses features from bootstrap.
<br>
Link to Code: <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py">click here</a> and <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/home.html"> here</a> <br>
Link on Website: http://p4donsabcd.cf/
<br>

<h2> Interactive COVID map: by Ketki</h2> <br>
This map pulls data from the same source as the table. When you hover on each state, you see the data for that state. States are also color coded based on the number of cases there. The map code has mostly been taken from <a href="https://leafletjs.com/examples/choropleth/"> here</a> with some modifications.
<br>
link to code: <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/map.html">click here</a> and <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/base.html"> here</a> and <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py"> here</a><br>
Link on Website: http://p4donsabcd.cf/map/
<br>

<h2> Easter Egg: by Iniyaa </h2> <br>
The easter egg, which can be accessed by clicking on the image of California under the CA page (accessed from navbar), displays our study journals, which have information on the College Board exam, as well as AP CSP fundamental standards.
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/Easter.html
Link on Website: http://p4donsabcd.cf/Easter
<br>

<h2> Covid Trivia: by Iniyaa </h2> <br>
The Trivia page was created using Flask WTForms. The code on main.py is in python and connects with the code in quiz.html and submit.html which have the code for the visual aspects of the trivia. In the top part of main.py, under the imports, you can see the arrays and class that were created for the trivia form. These are referencend towards the bottom of the filed werhe the quiz form and response page are created and the routes are. Here, you can see the python logic behind the code for the quiz. In quiz.html and submit.html, you can see the html code and jinja components of the trivia quiz page. Try it out and see how much you know about being safe during the pandemic!
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py, https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/quiz.html, https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/submit.html
Link on Website: http://p4donsabcd.cf<br>

<h2> Website Outline: by Iniyaa </h2> <br>
The Website outline was the first ticket completed. This is the framework for the website, which includes the app.routes in main.py, the html pages in templates, the nav bar in base.html and more. This website was created primarily in python and html, but also has some css, jinja, and bootstrap. <br>

<h2> Database: by Lucas </h2> <br>
The database has a full hsitory of who used and signed up for the website via SQLite. The tab for the database can be found under the Sign-Up tab on the nav bar. After the database is complete, a session should be connected to that part of the website so only those who has signed up by giving there email and password can access the covid data. 
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py
Link on Website: http://p4donsabcd.cf/Sign-Up
<br>

<h2> Raspberry Pi: by Dayita </h2> <br>
The database has a full hsitory of who used and signed up for the website via SQLite. The tab for the database can be found under the Sign-Up tab on the nav bar. After the database is complete, a session should be connected to that part of the website so only those who has signed up by giving there email and password can access the covid data. 
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py
Link on Website: http://p4donsabcd.cf/Sign-Up
<br>

# Who am I in computer science!
<h2> Ketki</h2> <br>
asdasdfjasdf"> here</a> <br>

<h2> Ketki</h2> <br>
asdasdfjasdf"> here</a> <br>

<h2> Ketki</h2> <br>
asdasdfjasdf"> here</a> <br>

<h2> Ketki</h2> <br>
asdasdfjasdf"> here</a> <br>


# College Board Requirements
<h2> Inputs</h2> <br>
We have multiple places where user input is necessary on our website. Users must input their username, email, and password to sign up, and must input their username and password to login to our website. Additionally, users must input their choices for the covid trivia quiz in order to get their score/the correct answers. Links to code with corresponding ticket items. <br>
