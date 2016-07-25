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

INVOKE_SHELL = 'C:\Windows\system32\cmd.EXE'

p = Path.cwd()
deploy_path = p.parents[0] / 'minchinweb.github.io-master'


def clean(ctx):
    print("You'll have to manually delete the output folder")
    #if os.path.isdir(DEPLOY_PATH):
    #    local('rm -rf {deploy_path}'.format(**env))
    #    local('mkdir {deploy_path}'.format(**env))


@task
def build(ctx):
    run('pelican -s pelicanconf.py', shell=INVOKE_SHELL)


@task
def rebuild(ctx):
    clean(ctx)
    build(ctx)


@task
def regenerate(ctx):
    run('start pelican -r -s pelicanconf.py', shell=INVOKE_SHELL)


@task
def serve(ctx):
    # local('cd {deploy_path} && start python -m SimpleHTTPServer'.format(**env))
    # in Python3000, use  python -m http.server
    run('cd {} && start python -m http.server'.format(deploy_path), shell=INVOKE_SHELL)


@task
def serve_on(ctx, port):
    # local('cd {deploy_path} && start python -m SimpleHTTPServer'.format(**env))
    # in Python3000, use  python -m http.server
    run('cd {} && start python -m http.server {}'.format(deploy_path, port), shell=INVOKE_SHELL)


@task
def reserve(ctx):
    build(ctx)
    serve(ctx)


@task
def preview(ctx):
    run('pelican -s publishconf.py', shell=INVOKE_SHELL)


@task
def upload(ctx):
    publish(ctx)
    run('cd {deploy_path}', shell=INVOKE_SHELL)
    run('git add -A', shell=INVOKE_SHELL)
    run('git commit', shell=INVOKE_SHELL)
    run('git push', shell=INVOKE_SHELL)


@task
def publish(ctx):
    run('pelican -s publishconf.py', shell=INVOKE_SHELL)


# Add devsever
# only works on Windows
#  need to kill the second window manually
@task
def devserver(ctx):
    regenerate(ctx)
    serve(ctx)

@task
def less(ctx):
    #run('lessc theme\\burst-energy\\less\\bootstrap.burst-energy.less > ' +
    #    env_deploy_path + '\\css\\style.css')
    #   lessc themes\pelican-minchin-ca\static\less\bootstrap.minchin-ca.min.less > themes\pelican-minchin-ca\static\css\bootstrap.minchin-ca.min.css
    source = p / 'themes\pelican-minchin-ca\static\less\\bootstrap.minchin-ca.min.less'
    dest = p / 'themes\pelican-minchin-ca\static\css\\bootstrap.minchin-ca.min.css'
    run('lessc {} > {}'.format(source, dest), shell=INVOKE_SHELL)
