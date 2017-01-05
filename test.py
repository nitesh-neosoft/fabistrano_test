import falcon

'''Falcon follows REST architectural style.
Means you can think of Resources and State Transitions,
which maps to HTTP verbs.'''

'''to run Falcon API. type the following command,
gunicorn filename:falcon api instance name
in our case, gunicorn test:app_inst '''


class ThingsResource(object):
	def on_get(self, req, resp):
		'''Handles GET request'''
		resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')


# falcon.API instances are callable WSGI-apps.
app_inst = falcon.API()

#  Class-instance represents resources.
things_inst = ThingsResource()

# All requests to "/things" URL path are handled by "things_inst".
app_inst.add_route("/things", things_inst)