**Images that correspond to tickets**
<br>
This set of images highlights some of the more notable aspects of our website, scroll down to see more details about our website/college board requirements
<br>
Home page w/ COVID data RestAPI
<br>
![covidhomepagealsdkjfa;sldkjf](https://user-images.githubusercontent.com/73010548/110581769-018ebb80-8120-11eb-98a1-42f649f2e3b4.PNG)
<br>
COVID Map
<br>
![covid map als;dkjfasl;kdjfa;lskdjf](https://user-images.githubusercontent.com/73010548/110581778-03f11580-8120-11eb-9f1c-371ecd279c57.PNG)
<br>
Register Page
<br>
![register page al;dsfkjasldkjf](https://user-images.githubusercontent.com/73010548/110581791-094e6000-8120-11eb-9447-5131d0017f06.PNG)
<br>
Sign In Page for returning users
<br>
![login as;dlfal;sdkfjalskdjf;aslkdfj;laks](https://user-images.githubusercontent.com/73010548/110581801-0eabaa80-8120-11eb-9c8b-f81dfa391728.PNG)
<br>
Page after login
<br>
![after login al;dskjfaldskjfa;lskdjf](https://user-images.githubusercontent.com/73010548/110581806-11a69b00-8120-11eb-9c7f-d1e98967f681.PNG)
<br>
Quiz Page
<br>
![quiz page al;dskjfa;sldkfj;asldkj](https://user-images.githubusercontent.com/73010548/110581816-1408f500-8120-11eb-8e07-bcd7052f6b76.PNG)
<br>
Results Page
<br>
![results alsd;kfjasl;dkjfal;skdjasldk](https://user-images.githubusercontent.com/73010548/110581821-18351280-8120-11eb-9896-f0f7b1e09cab.PNG)


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


<br>

<h2> Interactive COVID map: by Ketki</h2> <br>
This map pulls data from the same source as the table. When you hover on each state, you see the data for that state. States are also color coded based on the number of cases there. The map code has mostly been taken from <a href="https://leafletjs.com/examples/choropleth/"> here</a> with some modifications.
<br>
link to code: <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/map.html">click here</a> and <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/base.html"> here</a> and <a href="https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py"> here</a>
<br>


<h2> Easter Egg: by Iniyaa </h2> <br>
The easter egg, which can be accessed by clicking on the image of California under the CA page (accessed from navbar), displays our study journals, which have information on the College Board exam, as well as AP CSP fundamental standards.
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/Easter.html
<br>

<h2> Covid Trivia: by Iniyaa </h2> <br>
The Trivia page was created using Flask WTForms. The code on main.py is in python and connects with the code in quiz.html and submit.html which have the code for the visual aspects of the trivia. In the top part of main.py, under the imports, you can see the arrays and class that were created for the trivia form. These are referencend towards the bottom of the filed werhe the quiz form and response page are created and the routes are. Here, you can see the python logic behind the code for the quiz. In quiz.html and submit.html, you can see the html code and jinja components of the trivia quiz page. Try it out and see how much you know about being safe during the pandemic!
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py, https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/quiz.html, https://github.com/krispykreme14/flask-idea-homesite/blob/master/templates/submit.html
<br>

<h2> Website Outline: by Iniyaa </h2> <br>
The Website outline was the first ticket completed. This is the framework for the website, which includes the app.routes in main.py, the html pages in templates, the nav bar in base.html and more. This website was created primarily in python and html, but also has some css, jinja, and bootstrap. <br>

<h2> Database: by Lucas </h2> <br>
The database has a full hsitory of who used and signed up for the website via SQLite. The tab for the database can be found under the Sign-Up tab on the nav bar. After the database is complete, a session should be connected to that part of the website so only those who has signed up by giving there email and password can access the covid data. 
link to code: https://github.com/krispykreme14/flask-idea-homesite/blob/master/main.py


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

<h2>Algorithms</h2> <br>
We have many algorithms in our project. We have if/elif statements in the quiz part of the website which appends to a list, collecting how many answers you get right. Additionally, we use GET and POST in both the quiz and the login, which takes account of the input the user puts into the website. The quiz uses the users choices and the POST prodedure is used in the results/submit portion. Additionally, GET is used for getting the data from the user when they are signing up, and POST is used to send data to the server, which then remembers the user. <br>

# College Board Big Ideas
<h2>1. Creative Development</h2> <br>
Our website is a creative outlet for all our team members. The look and contents of the website reflects each of our creative thoughts and ideas. We worked collaborativley to bring togeather a COVID webscraper site which gives the user information about the pandemic. <br>

<h2>2. Data</h2> <br>
We use SQLite for the login page and use RestAPIs for our data that is shown in the map and table. We use GET and POST in our login and quiz pages. This is connected in our python bakcend. <br>

<h2>3. Algorithms and Programming</h2> <br>
We use Python, HTML, JINJA, and bootstrap on our website to create an aesthetic website. We use python for the backend code which includes more logic, and we use HTML and JINJA for our front end code which is the visual aspect of the website. <br>

<h2>4. Computer Systems and Networks</h2> <br>
Our website is deployed on a Raspberry Pi server, which allows anyone to acess the website. WE also use HTTP to get data from the use and POST to update our database of logins. <br>

<h2>5. Impact of Computing</h2> <br>
Not only did building this website help each of our team members grow intellectually, our website can also help people living today worried about their wellbeind during this global pandemic. Since this website shows statistics about covid and even has a trivia quiz which tests a person's aptitude in covid related situations. Our team was able to expand our computer science horizons, and looks forward to learning even more aspects of computer science next trimester and beyond <br>


# Goals for Tri 3
<br>
Expand python knowledge, become more familiar with using databases, find new areas in computer science to learn about <br>
