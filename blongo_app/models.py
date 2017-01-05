from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from blongo_proj.settings.production import _MONGODB_NAME, _MONGODB_DATABASE_HOST
# from blongo_proj.settings.production import MONGO_DATABASE_NAME

# connect(MONGO_DATABASE_NAME)	# Connecting to MongoDB named as "MONGO_DATABASE_NAME" in settings.py
# connect(username='nitesh',
#     	password='niteshp123',
#     	host='mongodb://nitesh:niteshp123@ds119748.mlab.com:19748/blongo_db')

connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)


class BlogCollection(Document):
	'''
		class which creates Collection named as 'blog_collection' in Database 'blongo_db'
		as well as created Document with fields 'title', 'content', 'last_updated'
	'''
	title = StringField(max_length=100, required=True)
	content = StringField(max_length=500, required=True)
	last_updated = DateTimeField(required=True)