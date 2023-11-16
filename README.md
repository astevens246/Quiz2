Quiz 2
SWAPI is the Star Wars API. It provides information about all of the characters, worlds, vehicles, and movies in the Star Wars universe.

Your goal is to make a Flask app that serves up information from SWAPI.

Take a look here: https://swapi.py4e.com

Read the documentation and test out the API.

The base URL is: https://swapi.py4e.com/api/

SWAPI supports these endpoints:

https://swapi.py4e.com/api/people
https://swapi.py4e.com/api/planets
https://swapi.py4e.com/api/vehicles
https://swapi.py4e.com/api/spaceships
https://swapi.py4e.com/api/films
https://swapi.py4e.com/api/species
Following any of these end points with an id will return a record from the database. For example:

https://swapi.py4e.com/api/people/1

Returns data about Luke Sky Walker

https://swapi.py4e.com/api/planets/3

Returns data for Yavin IV

https://swapi.py4e.com/api/films/4

Returns data for the The Phantom Menace

You need to form your query like this:

https://swapi.py4e.com/api//

Where category and id come from your form!

Challenge 1
Display the character data from SWAPI. You'll need to include an input that allows us to input the id of a character. Your code will request the data from the API and display it on the page.

For any character you should display:

name
height
mass
hair_color
eye_color
Stretch Challenge
Style your work. This is open ended put as much time into this as you like.

Style the form elements and the the output data.

Error Checking for bad requests
Some of the ids are missing or out of bounds. For example people/17 doesn't exist. Solve this challenge by checking for errors and displaying a message when there is a problem.

Stretch Challenge
The homeworld property is a URL to the homeworl at the SWAPI. Make another request and get the homeworld data and display the name of the hoemworld.

Displaying Lists
Every character has a films property that is a list of the films they appeared in. This list is a list of URLs to those films on SWAPI. Loop over this list, make a request to get the data for each film and display the name of each film.