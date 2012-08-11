from lib.view import FrontendPage
from google.appengine.api import users
from lib.forms import EventForm


class EventCreatePage(FrontendPage):
    def show(self):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url("/event/create"))
        
        form = EventForm()
        self.values['form'] = form
        self.template = 'event_create'
        