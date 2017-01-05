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


from fabric.api import *

env.hosts = ["webwerks@10.0.11.109"]
# env.hosts = ["webwerks@206.183.111.25"]

def mytask():
	print "HHHHHHH"
	# run('ls /var/')


def hello(name="abcd"):
	run('rmdir -p /home/webwerks/pear2')
# 	run("uptime")
# 	print "HIIIII"
    # print "Hello %s" % (name)https://github.com/nitesh-neosoft/fabistrano_test.git

def remote_pull():
	run('cd /home/webwerks/pear')
	run('git clone https://github.com/nitesh-neosoft/fabistrano_test.git')

def new_check():
	print "TESTTTT"
