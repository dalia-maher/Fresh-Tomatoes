# Fresh Tomatoes Movie Trailer Website 

This webiste aims to display a list of movies with their related info such as (title, poster, trailer, ... etc.) using a Python data structure. A list of movies are displayed and by clicking on any of the listed movies for that movie a trailer opens in a popup window. This project was done as a part of the Full Stack Web Developer Nanodegree on [Udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Setup
--------

To set up the environment for the project, you must download [Python](https://www.python.org/downloads) and make sure it is
version 2.7 or above, as any other version may not be compatible with the code. It's supported for Windows, Linux/UNIX, Mac OS X, and other operating systems.

Once Python is installed, you can download the project ZIP file or clone it to your local machine by clicking on the green "Clone or download" button on the upper right side of the page
`or`
clone it to your local machine using Git's command line
```
git clone https://github.com/dalia-maher/Fresh-Tomatoes
```

## To run this project
----------------------

1. Open the unzipped / cloned directory of the repo in your local machine
2. Open the file "entertainment_center.py" from Python IDLE or press right-click -> Edit with IDLE
3. Run the module (Run -> Run Module) or Press F5
4. The website will be opened in your default browser

`or`
- By running this command from Windows/Linux command line after changing directory to the unzipped or cloned directory:
    ```
    python entertainment_center.py
    ```
`or`

- If you just want to run the project without editing, you can open the html file "fresh_tomatoes.html" in your browser


## Project Functionalities
-----------------------

1. You can find a list of nine movie titles and posters rendered on the page in the browser
2. Clicking on the movie should open a popup window that shows the trailer of the movie.
3. Clicking on the "x" button in the upper right corner of the trailer preview should close the popup.


## Project Contents
-------------------

### entertainment_center.py:
Python module that instantiates movie objects, adds them into an array and calls the fresh_tomatoes.py module to generate the web page and load it into the default browser. You can use it to define and add more movies to the list or change the current list

### fresh_tomatoes.py:
Python module used to dynamically generate the web page from a given array of movie objects

### fresh_tomatoes.html:
HTML file that is dynamically generated by the fresh_tomatoes.py Python module

### media .py:
This file contains a Movie class used for defining movie objects that include 6 attributes (title, description, duration, poster, trailer and release year) and inherits from Video class that defines any video object consisting of title and duration.
