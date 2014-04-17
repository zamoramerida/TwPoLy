"""A simple webapp2 server."""
import webapp2
import logging
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    if "name" not in self.request.POST:
        self.response.write('Name not in form')
    else:
        self.response.write(self.request.POST["name"]) 
        
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render())


application = webapp2.WSGIApplication([('/', MainPage)],debug=True)