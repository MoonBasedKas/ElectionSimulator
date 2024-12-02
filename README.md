# Election simulator
The goal of this project is to simulate applying paillier encyrption into elections. With this goal in mind we can also 
simulate some flaws with this and explore solutions to flaws.

# Scenario
Tech students must always ask the question Taco or Pizza so to put a definitive end to this we've decided to simulate a vote. 
The vote will use random buildings from tech as provences and tally it. Encryption using paillier and to showcase how it works.
Each building is worth 1 electoral vote and is what decides the winner of this contest rather than the popular vote.

# Starting

To start the simulation you must first have a few packages installed. mysql connector, flask, mysql or mariadb, a web browser (obviously) and python of course.
You'll want to set up an env file in the same folder as website.py first line will be the user=x and then second line password=y.
Finally to run you will use the following command:

flask --app website run

To run the website you'll want to visit localhost:5000 and fill out the form. Once you've filled out the form it'll take you to a confirmation page.
Click the hyperlink and you'll be able to see the start of the election simulator.

# Technical set up
The simulator uses 3 parts. A database, a flask servlet, and vote generators. Vote generators will send their voting information
directly to the database while the flask servlet will collect the data from the database and use jinja templates to showcase the information 
we've generated and passed on. When running you'll visit the website localhost:5000 and it'll direct you to the set up page. Once it's started 
it'll direct you to another page where you can click start and advance to the actual simulator. To view updates you'll want to refresh the page.

# Scenario 1.1
No malicous actors exist within the network.


# Gui
Gui will be implemented using a python flask server. This is to give more immersion as election results as they are
tallied will be posted to a website the actual results will only be posted during regular intervals of time. 

In the back ground there will also be an option that shows the central polling station's count as well 
as the encrypted values coming into it.

