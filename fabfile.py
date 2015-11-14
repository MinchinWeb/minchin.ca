from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '../minchinweb.github.io-master'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    print("You'll have to manually delete the output folder")
    #if os.path.isdir(DEPLOY_PATH):
    #    local('rm -rf {deploy_path}'.format(**env))
    #    local('mkdir {deploy_path}'.format(**env))


def build():
    local('pelican -s pelicanconf.py')


def rebuild():
    clean()
    build()


def regenerate():
    local('start pelican -r -s pelicanconf.py')


def serve():
    local('cd {deploy_path} && start python -m SimpleHTTPServer'.format(**env))
    # in Python3000, use  python -m http.server


def reserve():
    build()
    serve()


def preview():
    local('pelican -s publishconf.py')


def upload():
    publish()
    local('cd {deploy_path}')
    local('git add -A')
    local('git commit')
    local('git push')


@hosts(production)
def publish():
    local('pelican -s publishconf.py')


# Add devsever
# only works on Windows
#  need to kill the second window manually
def devserver():
    regenerate()
    serve()


def less():
    #run('lessc theme\\burst-energy\\less\\bootstrap.burst-energy.less > ' +
    #    env_deploy_path + '\\css\\style.css')
    #   lessc themes\pelican-minchin-ca\static\less\bootstrap.minchin-ca.min.less > themes\pelican-minchin-ca\static\css\bootstrap.minchin-ca.min.css
    pass
