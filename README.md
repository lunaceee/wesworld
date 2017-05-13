# <img src="static/css/images/binocular-big.png">
 
# Wes World 
## Descriptions
Welcome to Wes World - the unbearable awesomeness of clours. 
Wes World aims to create a simple and fun online shopping experience based on curated color palettes from Wes Anderson movies. 🎨 It funnels active Etsy listings into a view of an ensemble of clothing items via Etsy API. A user can click on a movie button to view a randomly chosen set of clothing items. User can also save the ensemble by creating a user account. 

Credits to the following artists for the incredible design elements:
Lea Lafleur
Alejandro Giraldo
Hexagonall

## Table of Contents

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#installation)
* [Wes World 3.0](#future)

## <a name="tech-stack"></a>Tech Stack
__Frontend:__ HTML5, CSS3, JavaScript, jQuery, Materialize (UI) <br/>
__Backend:__ Python, Flask, PostgreSQL, SQLAlchemy <br/>
__APIs:__ Etsy <br/>

#### About the Search Algorithm:
I created a caching layer to improve speed performance and a blacklist to allow a superuser account to remove irelevant search results.

## <a name="features"></a>Features


## <a name="installation"></a>Setup/Installation

#### Requirements:

- PostgreSQL
- Python 2.7
- Etsy API key

You can run this app on your local computer via the following steps:

Clone repository:
```
$ git clone https://github.com/lunaceee/wesworld.git
```
Create a virtual environment:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Get your own secret keys for [Etsy](). Save them to a file `secret.sh`. Your file should look something like this:
```
export API_KEY='<your api key here>'
```
Create database 'wesworld'.
```
$ createdb wesworld
```
Create your database tables and seed example data.
```
$ python seed.py
```
Run the app from the command line.
```
$ python server.py
```
If you want to use SQLAlchemy to query the database, run in interactive mode
```
$ python -i model.py
```

## <a name="future"></a>Wes World 3.0
* Figure out scalable solution for high traffic
* 
* 
* 
* 

