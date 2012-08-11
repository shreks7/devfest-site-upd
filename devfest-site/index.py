import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
from pages.EventPages import EventPage
from pages.EventPages import EventListPage
from pages.StartPage import *
from pages.LoginPage import *
from lib.view import FrontendPage
from pages.EventCreatePage import EventCreatePage

app = webapp2.WSGIApplication([
                              ('^/logout$', LogoutPage),
                              ('^/login$', LoginPage),
                              ('^/$', StartPage),
                              ('^/event/create$', EventCreatePage),
                              ('^/events$', EventListPage),
                              ('^/event/(.*)$', EventPage),
                              ],
                              debug=True)
def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()

