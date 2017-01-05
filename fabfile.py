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
from contextlib import contextmanager

env.hosts = ["webwerks@10.0.11.109"]
# env.hosts = ["webwerks@206.183.111.25"]

code_dir = '/home/webwerks/fabistrano_test'
owner = 'root'
# VENV_DIR = os.path.join('/home/webwerks', '.venv')



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

def pull_remote_test():
	# code_dir = '/home/webwerks/fabistrano_test'
	with cd(code_dir):
		run('git pull')
	# run('cd /home/webwerks/fabistrano_test')
	# rmdirun('ls')
	# run('git pull')

def new_check():
	print "TESTTTT"

# def run_tests():
def test():
	# local("python manage.py test blongo_app")
	local("python manage.py test blongo_app")
    # local("./manage.py test blongo_app")
	# local("./manage.py test blongo_app")
	# local('coverage run manage.py test blongo_app')

def local_deploy():
    local("python manage.py runserver")
    # local("git add -p && git commit")
    # local("git push")

# @contextmanager
# def source_virtualenv():  
#     with prefix('source ' + os.path.join(VENV_DIR, 'bin/activate')):
#         yield



def remote_deploy():
	with cd(code_dir):
		run('git pull')

		# with cd(code_dir):
		# sudo('apt-get install virtualenv')
		v_env_command = 'virtualenv DjangoFabric'
		v_actv_command = 'source DjangoFabric/bin/activate'
		sudo('%s && %s' % (v_env_command, v_actv_command), user=owner)
		pip_command = 'pip install -r requirements.txt'
		#sudo('%s && %s' % (venv_command, pip_command), user=owner)
		sudo('%s' % pip_command, user=owner)
		# run_command = 'python manage.py runserver'
		sudo( 'python manage.py runserver' , user=owner)
















		# pip_command = 'pip install -r requirements.txt'
		# sudo(pip_command)
		# with source_virtualenv():
	 #            with prefix('export DJANGO_SETTINGS_MODULE={}.settings.{}'.format(PROJECT_NAME, env.environment)):
	 #                run('source .env/bin/activate && pip install -r requirements/production.txt')
	 #                run('./manage.py migrate')
	 #                run('./manage.py collectstatic --noinput')


