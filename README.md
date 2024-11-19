# Election simulator
The goal of this project is to simulate applying paillier encyrption into elections. With this goal in mind we can also 
simulate some flaws with this and explore solutions to flaws.

# Scenario
The country of Skyrim is having an election in the year 20XX AD. Skyrim is broken up into 9 holds and follows the electoral 
college system of voting; each provence follows the all or nothing system.
There is numerous polling locations however each polling location is attached to a central 
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

# Scenario 1.2
A single malicous actor exists within the network within a randomly assigned provence. To simulate this 
the malicous actor will be able to perform a rely attack.

# Scenario 1.3
A given malicous actor can generate a valid count and transmit over the network for a choosen political party.

# Hold weights
Whiterun: -
Falkreath: -
Winterhold: -
The Rift: -
Eastmarch: - 
Haafingar: -
The Pale: -
The Reach: - 
Hjaalmarch: -

Population is based off of a percentage of the total hold weights and an individual multiplied by the total 
population rounded down.

# Gui
Gui will be implemented using a python flask server. This is to give more immersion as election results as they are
tallied will be posted to a website the actual results will only be posted during regular intervals of time. 

In the back ground there will also be an option that shows the central polling station's count as well 
as the encrypted values coming into it.
