# from fabistrano import deploy
# from fabric.api import *


# # env.hosts = ["10.0.11.111"] # Replace with your host name or IP
# env.base_dir = '/home/webwerks/NiteshPalankar/VirtualEnv/fabistrano_check/src' # Set to your app's directory
# env.app_name = 'app_name.com' # This will deploy the app to /www/app_name.com/
# # # env.git_clone = 'GIT_PATH' # Your git url

# # env.restart_cmd = 'kill -HUP `supervisorctl pid gunicorn`' # Restart command
# # or
# # env.wsgi_path = "app_name/apache.wsgi" # Relative path to the wsgi file to be touched on restart


# def hello():
#     print "Hello world!"

from fabric.api import run

def hello(name="abcd"):
    print "Hello %s" % (name)
