# Michelle's Mini Project

Hi! Welcome to my Mini Café ☕️ Project. This is a Command Line Interface project built using Python, Docker, and PostgreSQL. It uses a Tabulate module from Python for Cafe menu displays, as well as Psycopg2 for managing the database and Pytest for running Unit Tests. The project was created over a 6 week period while learning Python and with each week we were given a new set of MVP requirements. The week-6 directory contains the most up to date version.

## Client requirements

As a user I want to:

- create a product, courier, or order and add it to a table
- view all products, couriers, or orders
- update the status of an order
- persist my data in a database
-  _STRETCH_ delete or update a product, order, or courier


## How to run the app

#### Create a virtual environment
#Mac/Unix <br>
`$ python3 -m venv .venv`<br>
or<br>
#Windows<br>
`$ py -m venv .venv`


#### Activate virtual environment
#Mac/Unix<br>
`$ source .venv/bin/activate`<br>
or<br>
#Windows<br>
`$ .venv\Scripts\activate.bat`<br>
or<br>
`$ .venv\Scripts\activate.ps1`

#### Install requirements
#Mac/Unix<br>
`(.venv) $ python3 -m pip install -r requirements.txt`<br>
or<br>
#Windows<br>
`(.venv) $ py -m pip install -r requirements.txt`<br>

#### Run Docker
Make sure Docker is open and, in the src directory, run <br>
`(.venv) $ docker compose up -d`<br>
-create a table called 'miniproject'
-use sql-backup.sql to input data in database

#### Run the application
In the src directory, run <br>
#Mac/Unix<br>
`(.venv) $ python3 app.py`<br>
or<br>
#Windows<br>
`(.venv) $ py app.py`

## How to run Unit Tests

In the src directory run<br>
#Mac/Unix<br>
`(.venv) $ python3 -m pytest`<br>
or<br>
#Windows<br>
`(.venv) $ py -m pytest`

## Project Reflections

#### Design and Project Requirements
It was interesting, as weeks progressed; sometimes I would change very little, and sometimes I changed a lot. Week 3-4 was the most tricky for me, as I was blocked for a few days trying to get my application to run smoothly. I realized I had implemented things that weren't actually required, therefore making other requirements harder to implement. Once I realized this, I was able to make necessary changes. I learned a lot in this time. 

#### Guaranteeing Project Requirments
I guaranteed project requirements by following the guidelines set for us. We were graciously provided sudo-code which was easy to interpret and to follow. 

#### Improvements
To improve the app, I would make more robust Unit Tests, and also ensure the Unit Tests are working accurately. I also would have implemented classes where possible, and done more of the bonus challenges instead of just the stretch goals. 

#### What I most enjoyed implementing
What I enjoyed implementing the most was the persistence of the data. We first did this using txt files, then csv files, and eventually databases. I also enjoyed using the Tabulate module in python to make my cafe menus look pretty✨ Overall, I also enjoyed seeing the entire project come together. 