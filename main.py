from wsgiref.simple_server import make_server
import falcon

from fh.aalen.animal.AnimalController import AnimalController
from fh.aalen.animal.AnimalRessource import AnimalRessource

from fh.aalen.location.LocationController import LocationController
from fh.aalen.location.LocationRessource import LocationController

#create the falcon app
app = application = falcon.App()

#Instantiate the Ressources
ares = AnimalRessource()
lres = LocationRessource()

#Initalize the controllers
ac = AnimalController(app, ares)
lc = LocationController(app, lres)

#Start a webserver on port 8080
if __name__ == '__main__':
    with make_server('', 8080, app) as httpd:
        print('Serving on port 8080...')
# Run as server until process is killed
        httpd.serve_forever()