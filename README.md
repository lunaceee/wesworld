# Wes World
# <img src="static/css/images/binocular-big.png">

Descriptions


## Table of Contents

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#installation)
* [To-Do](#future)

## <a name="tech-stack"></a>Tech Stack
__Frontend:__ HTML5, Javascript, jQuery, Materialize <br/>
__Backend:__ Python, Flask, PostgreSQL, SQLAlchemy <br/>
__APIs:__ Etsy <br/>


## <a name="features"></a>Features


## <a name="installation"></a>Setup/Installation

#### Requirements:

- PostgreSQL
- Python 2.7
- Etsy API key

To have this app running on your local computer, please follow the below steps:

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

## <a name="future"></a>TODO
* 
* 
* 
* 
* 

