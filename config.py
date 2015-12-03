WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess' 
#The SECRET_KEY setting is only needed when CSRF is enabled, 
#and is used to create a cryptographic token that is used to validate 
#a form. When you write your own apps make sure to set the secret key 
#to something that is difficult to guess.

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


#import os
#asedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Whoosh does not work on Heroku
#WHOOSH_ENABLED = os.environ.get('HEROKU') is None