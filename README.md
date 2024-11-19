# Election simulator
The goal of this project is to simulate applying paillier encyrption into elections. With this goal in mind we can also 
simulate some flaws with this and explore solutions to flaws.

# Scenario
The country of Skyrim is having an election in the year 20XX AD. Skyrim is broken up into 9 holds and follows the electoral 
college system of voting. There is numerous polling locations however each polling location is attached to a central 
count system where they pass their information towards. The election is between the two major parties and third party
canidates will not be considered. We have the West Party whose running candiate Jarl Balgruuf the greater and the 
East party whose candiate is Funny Valentine. For this scenario their policies or any real world political affiliation 
does not matter.

We will simulate this network as a series of sockets connected. There will be 9 sockets each of which connected to a 
central processing location. We will have the biases towards each region assigned within a text file. Skyrim will 
have a rather low population of less than 10,000 thus we can generate keys which are workable within that range. 
This is mainly done so we can speed up the speed of encryption as paillier is VERY SLOW especially with the use of 
python as a language.

# Scenario 1.1
No malicous actors exist within the network.
