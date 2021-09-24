"""Seeds the database"""

import os #imports Python module from standard library
from datetime import datetime 
from random import choice, randint #for testing

import crud
import model
from model import User, Image, app


#drop and recreate the database
os.system('dropdb images')
os.system('createdb images')

model.connect_to_db(app, echo=False) #connect to the db through model.py
#echo=False to cut down on terminal output so it's easier to see error messages
model.db.create_all()

#create fake users to add to database
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)


#create fake images to add to the database
for n in range(10):
    image_name = f"{n} test image"
    image_description = f"{n} test image description"
    date_added = "2021-01-01"
    size_in_mb = n


    image = crud.create_image(image_name, image_description,
            date_added, size_in_mb)


