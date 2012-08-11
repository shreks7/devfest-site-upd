from lib.view import FrontendPage
from google.appengine.api import users
from datamodel import Event

class EventListPage(FrontendPage):
  def show(self):
    user = users.get_current_user()
    self.template = 'locations'

   