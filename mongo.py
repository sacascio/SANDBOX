#!/usr/bin/env python

from __future__ import print_function
from pymongo import MongoClient
import sys

client = MongoClient()

db = client.mydb

data = db.movie.find()

for document in data:
	for k in document:
		print (k,document['_id'],sep=",")

exists = db.movie.find_one({'_id':12})

if not  bool(exists):
    newdata = {'_id' : 12, 'adult' : 'yes'}
    db.movie.insert(newdata)


client.close()
