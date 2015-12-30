from invoke import run, task
from pathlib import Path

# from fabric.api import *
# import fabric.contrib.project as project
# import os

# Local path configuration (can be absolute or relative to fabfile)
#env.deploy_path = '../minchinweb.github.io-master'
#DEPLOY_PATH = env.deploy_path

# Remote server configuration
#production = 'root@localhost:22'
#dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
#env.cloudfiles_username = 'my_rackspace_username'
#env.cloudfiles_api_key = 'my_rackspace_api_key'
#env.cloudfiles_container = 'my_cloudfiles_container'

p = Path.cwd()
deploy_path = p.parents[0] / 'minchinweb.github.io-master'


def clean():
    print("You'll have to manually delete the output folder")
    #if os.path.isdir(DEPLOY_PATH):
    #    local('rm -rf {deploy_path}'.format(**env))
    #    local('mkdir {deploy_path}'.format(**env))


@task
def build():
    run('pelican -s pelicanconf.py')


@task
def rebuild():
    clean()
    build()


@task
def regenerate():
    run('start pelican -r -s pelicanconf.py')


@task
def serve():
    # local('cd {deploy_path} && start python -m SimpleHTTPServer'.format(**env))
    # in Python3000, use  python -m http.server
    run('cd {} && start python -m http.server'.format(deploy_path))


@task
def reserve():
    build()
    serve()


@task
def preview():
    run('pelican -s publishconf.py')


@task
def upload():
    publish()
    run('cd {deploy_path}')
    run('git add -A')
    run('git commit')
    run('git push')


@task
def publish():
    run('pelican -s publishconf.py')


# Add devsever
# only works on Windows
#  need to kill the second window manually
@task
def devserver():
    regenerate()
    serve()

@task
def less():
    #run('lessc theme\\burst-energy\\less\\bootstrap.burst-energy.less > ' +
    #    env_deploy_path + '\\css\\style.css')
    #   lessc themes\pelican-minchin-ca\static\less\bootstrap.minchin-ca.min.less > themes\pelican-minchin-ca\static\css\bootstrap.minchin-ca.min.css
    source = p / 'themes\pelican-minchin-ca\static\less\\bootstrap.minchin-ca.min.less'
    dest = p / 'themes\pelican-minchin-ca\static\css\\bootstrap.minchin-ca.min.css'
    run('lessc {} > {}'.format(source, dest))
