from lib.view import FrontendPage
from google.appengine.api import users
from datamodel import Event

class EventPage(FrontendPage):
    def show(self):
        self.template = 'location'
        user = users.get_current_user()

