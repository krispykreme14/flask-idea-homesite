# Welcome to our COVID information site.

<h2>Website Overview:</h2>
This website is a COVID 19 Website designed to make sure you can take appropriate precautitons to stay safe during this global pandemic. The home page contains a table which is the output of a RestAPI. This table provides some of the most important COVID stats in all 50 states. In the navigation bar, you can see that there are multiple pages. The map page is interactive and has additional covid stats rgarding each state but in a geographical view for a better understanding of the severity of covid in different states. There is also a big states dropdown, which highlights the information in some states. There is also a login page which requries an email and password. Those who create an account and log in get directed to a new page. This page is still being worked on and will be a covid risk assesment program. This requries the user to imput some details about themselves and the output will be the level of their COVID 19 risk. 

<h2>How to acces COVID information site:</h2>
Link to website: http://p4donsabcd.cf/
Link to Easter Egg file: http://p4donsabcd.cf/Easter

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

# Goals for Tickets! (more details on <a href="https://github.com/krispykreme14/flask-idea-homesite/projects/1">project board</a>

 -->Add CSS, images, and other graphics to make website look more professional;remove jumbotrons, etc.  <br>

 -->Get the database working!!
  
 -->Add mini apis for each of the individual states pages  have them show live data, as opposed to typed numbers  <br>
  
 -->Add exclusive section for people who log inanalyze their risk based on their location/other factors  <br>

 --> Incorporate Scrum Crossover suggestions: Having the database login take you to an individual page for each user, add commas for the numbers on the table so it would be easier to look at the data. 
 <br>
 
 # College Board Components in Project:

<h2> Lists </h2> <br>
<h2> Inputs </h2> <br>
<h2> Outputs </h2> <br>
<h2> Procedures </h2> <br>
<h2> Algorithms </h2> <br>
 
# Previous Information

Feb 4 Reflections:

Who Am I In Computer Science?

Iniyaa: I can build a Python/Flask website, I am working on Python programming and am working to become more experienced and knowledgeable, I have worked briefly on setting up a RasberryPi, I know the concepts of HTML forms, exchanign data between frontend and backend using Flask Framework and Jinja variables.

Ketki: I am competent in Python programming and am working on becoming an expert, I can build a Python/Flast web server, I can develop web frontends uisng HTML, CSS, and BootSTrap, I understand REST APIs capabilities Flask request and parsin resulting data from JSON, I am now learning concepts of curating data, searchign data, and starting to become competent in concepts like Data Analytics.

Lucas: I can develop web frontends usin HTML, CSS< and Bootstrap, I know the conepts of HTML forms, building Jinja templates, I can do backend work with SQL databases, specifically SQLite, and SQLalchemy utilizing the Flask framework, I know database concepts like establishing tables to setup and manage user accounts, I know Flask services like login_reuired

Dayita: I can build a Python/FLask web server, I can do the DevOps on Linux, namely settin gup a Python/Flask server using services like Guniorn, and Nginx, I have worked with Internet Service Provider DNS records to setup my own Domain.

## Tickets Progress: 6 week mark

- Began framework for US Map by Ketki<br>
--> followed tutorial from https://leafletjs.com/examples/choropleth/ <br>
--> map also utilizes api, it takes a map from another api website.<br>
--> can zoom in and out on map<br>
--> code for map was in java script, so it was a challenge to figure out how to call that code in our project, which is HTML and python<br>
--> Goal is to have data from table visible on map when hovering on a state<br>

- Begun to work to create a session for the website by Lucas <br>
--> Using this tutorial from https://www.youtube.com/watch?v=2Zz97NVbH0U <br>
--> The session will attach to the database to allow users to access the website<br>
--> Uses SQLite<br>
--> No CSS yet<br>
--> Also linked the easter egg through the picture click<br>

- Compeleted deploying the website and all forms with it by Dayita <br>
--> Made on the virtual box<br>
--> Completes all the requirements for the deploy process<br>
--> Can be assessed through link<br>

- Iniyaa <br>
--> Embedded links to college board<br> 
--> Also embedded links to Ap prep materials such as weekly tests and journals<br> 
--> Used the same design to make it look just like the other parts of our website<br>
--> Links through the California page<br>
--> Rethink ticket idea, previous idea doesn't have hardcore data to go with it<br>
--> Changed idea - check boxes or choose button and result is likelyhood of catching covid<br>
Research: https://www.nature.com/articles/d41586-020-03637-y, https://www.webmd.com/lung/news/20201109/whats-my-risk-of-covid, 
https://www.mdlinx.com/article/what-are-the-odds-online-calculators-predict-death-covid-19-cancer-and-more/TTxcCN0OSNTMU5eINtlOk


