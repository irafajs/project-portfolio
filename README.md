THIS IS A GUIDE TO THE CODE THAT RUN WEBSITE NAMED MEDICINE NEAR YOU
___________________________________________________________________________

IN THIS PROJECT WE USED BELOW TECH:
   FRONT-END
   ____________
 
	HTML
	CSS
	JAVASCRIPT

    BACK-NED
   _____________
	PYTHON
	FLASK 
	MYSQL

APPLICATION STRUCTURE
__________________________
   Every directory inside the source directory has an __init__ file to create python packages.

   app.py file is starting the application
   TEMPLATES directory has all the html files that are running in the front-end
   STATIC dicectory contains all the styling files and the script(javascript)
   SOURCE directory contains 
       auth file that has the route for sign-in, sign-up and logout
       MODELS directory contains:
           user file that contains the structure of the user table
           medecine file that contains the structuer of medecine table
           STORAGE directory contains:
               connectdb file conntain command that connect to us using sqlAchemy
      API->V1->VIEWS contains files:
          addstock file contains code that adds the new medecine to teh stock of the pharmacy owner
          deletestock has code that delete the stock that is no longer into the stock or not available on the market
          homepage contains code that run the homepage contents
          userdetails contains the code that runs the admin side of the pharmacy, like adding new medecine and deleting the medecine no longer in the stock...
          

HOW THE APPLICATION WORKS:

In general the website works like a search engine, but this one works for a close group of data saved into 
our SQL database.

> User can access it and search by keyworkd, at the seach, result will come with 
  medecine name, madecine description and owning pharmacy name, address number so 
  that the user(sick person in this case or the one helping) can have the nearest 
  pharmacy with required medecine.

> There is admin side of the Pharmacie owner, once registered, and logged in the owner can add stock of 
  medecines they have in real time, if the medecine is no
  longer available in their pharmacy they can delete it where it no longer availbale for the end-user..

>IINSTALLATION
_________________

flask
Flask-SQLAlchemy
flask-login
PYTHON

To run the app clone it fron this git hub and running using the app file by doing ./app
