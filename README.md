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
![homepageimage](https://user-images.githubusercontent.com/73010548/110580111-d2c31600-811c-11eb-8213-6ae2cb2961a6.PNG)

<br>

<h2> Interactive COVID map: by Ketki</h2> <br>
This map pulls data from the same source as the table. When you hover on each state, you see the data for that state. States are also color coded based on the number of cases there. The map code has mostly been taken from <a href="https://leafletjs.com/examples/choropleth/"> here</a> with some modifications.
<br>
link to code: <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/map.html">click here</a> and <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/base.html"> here</a> and <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py"> here</a>
<br>
![mapimage](https://user-images.githubusercontent.com/73010548/110580126-d9518d80-811c-11eb-8e90-3697acbf6149.PNG)

<br>

<h2> Easter Egg: by Iniyaa </h2> <br>
The easter egg, which can be accessed by clicking on the image of California under the CA page (accessed from navbar), displays our study journals, which have information on the College Board exam, as well as AP CSP fundamental standards.
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/Easter.html
<br>

<h2> Covid Trivia: by Iniyaa </h2> <br>
The Trivia page was created using Flask WTForms. The code on main.py is in python and connects with the code in quiz.html and submit.html which have the code for the visual aspects of the trivia. In the top part of main.py, under the imports, you can see the arrays and class that were created for the trivia form. These are referencend towards the bottom of the filed werhe the quiz form and response page are created and the routes are. Here, you can see the python logic behind the code for the quiz. In quiz.html and submit.html, you can see the html code and jinja components of the trivia quiz page. Try it out and see how much you know about being safe during the pandemic!
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py, https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/quiz.html, https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/submit.html
<br>
![quiz image](https://user-images.githubusercontent.com/73010548/110580142-e3738c00-811c-11eb-8350-5f006666ce66.PNG)
<br>
![quiz results image](https://user-images.githubusercontent.com/73010548/110580147-e5d5e600-811c-11eb-8415-c2640bcb4460.PNG)

<br>

<h2> Website Outline: by Iniyaa </h2> <br>
The Website outline was the first ticket completed. This is the framework for the website, which includes the app.routes in main.py, the html pages in templates, the nav bar in base.html and more. This website was created primarily in python and html, but also has some css, jinja, and bootstrap. <br>

<h2> Database: by Lucas </h2> <br>
The database has a full hsitory of who used and signed up for the website via SQLite. The tab for the database can be found under the Sign-Up tab on the nav bar. After the database is complete, a session should be connected to that part of the website so only those who has signed up by giving there email and password can access the covid data. 
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py
<br>
![register page image](https://user-images.githubusercontent.com/73010548/110580160-ee2e2100-811c-11eb-8da5-dfbe8f8d58eb.PNG)
<br>
![login page image](https://user-images.githubusercontent.com/73010548/110580165-eff7e480-811c-11eb-8e4a-2cb69baf9ddc.PNG)
<br>
![after login page image](https://user-images.githubusercontent.com/73010548/110580170-f25a3e80-811c-11eb-998f-4510cf197e4c.PNG)

<br>

<h2> Raspberry Pi: by Dayita </h2> <br>
The database has a full hsitory of who used and signed up for the website via SQLite. The tab for the database can be found under the Sign-Up tab on the nav bar. After the database is complete, a session should be connected to that part of the website so only those who has signed up by giving there email and password can access the covid data. 
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py
<br>

# Who am I in computer science!
<h2>Ketki</h2> <br>
type stuff <br>

<h2>Iniyaa</h2> <br>
I can build a Python/Flask webpage using html and python(frontend and backend code). I can develop web front ends(shown in the state html pages along with quiz, navbar, and home page). I am learning the concepts of HTML forms and exchanging data between frontend and backend using Flask Framework and Jinja variables(shown by quiz page and results page). I am a collaborative worker who can effectively communicate and work on a shared platform wiht scrum team members.</a> <br>

<h2>Lucas</h2> <br>
type stuff <br>

<h2>Dayita</h2> <br>
type stuff <br>

# College Board Requirements
<h2> Inputs</h2> <br>
We have multiple places where user input is necessary on our website. Users must input their username, email, and password to sign up, and must input their username and password to login to our website. Additionally, users must input their choices for the covid trivia quiz in order to get their score/the correct answers. Links to code with corresponding ticket items. <br>

<h2>Lists</h2> <br>
We use lists for thq covid trivia, as the correct answers are stored in a list as are the the answer choices. Additionally, the state abbreviations are stored in a dictionary that counts in the list category in terms of college board requirements. <br>

<h2>Procedures</h2> <br>
We use procedures which can be seen in our main.py file. The procedures each render a html file and the different routes correspond to pages on the website. Additionally, the quiz and login are both procedures, and the results from the quiz procedure is passed to submit to display the correct/incorrect answers.<br>

<h2>Output</h2> <br>
The COVID map is an output with all the color coded states and state statistics. The RestAPI data is displayed in both the table and the map. Additionally, the results page of the COVID trivia quiz are also an output which is in response to the users input.<br>

<h2>Algorithm</h2> <br>
We have many algorithms in our project. We have if/elif statements in the quiz part of the website which appends to a list, collecting how many answers you get right. Additionally, we use GET and POST in both the quiz and the login, which takes account of the input the user puts into the website. The quiz uses the users choices and the POST prodedure is used in the results/submit portion. Additionally, GET is used for getting the data from the user when they are signing up, and POST is used to send data to the server, which then remembers the user. <br>


