from pathlib import Path
import time

from invoke import run, task

# INVOKE_SHELL = 'C:\Windows\system32\cmd.EXE'

p = Path.cwd()
# used for local testing
deploy_path = p.parents[0] / 'minchinweb.github.io-temp'
# used for the version to be put on the wider internet
publish_path = p.parents[0] / 'minchinweb.github.io-master'


def clean(ctx):
    print("You'll have to manually delete the output folder")
    #if os.path.isdir(DEPLOY_PATH):
    #    local('rm -rf {deploy_path}'.format(**env))
    #    local('mkdir {deploy_path}'.format(**env))


@task
def build(ctx):
    """Build a local version of the blog."""
    ctx.run('pelican -s pelicanconf.py')


@task
def build_debug(ctx):
    """Use debug output to build a local version of the blog."""
    ctx.run('pelican -s pelicanconf.py --debug')


@task
def rebuild(ctx):
    """clean and build."""
    clean(ctx)
    build(ctx)


@task
def regenerate(ctx):
    """Rebuild a local version of the blog if files change."""
    ctx.run('start pelican -r -s pelicanconf.py')


@task
def serve(ctx):
    """Serve the local blog output on port 8000."""
    ctx.run('cd {} && start python -m http.server'.format(deploy_path))


@task
def serve_on(ctx, port):
    """Serve the local blog output on a port of your choosing."""
    ctx.run('cd {} && start python -m http.server {}'.format(deploy_path, port))

@task
def reserve(ctx):
    """build and serve."""
    build(ctx)
    serve(ctx)


@task
def upload(ctx):
    """publish and then push the result to GitHub."""
    publish(ctx)
    ctx.run('cd {} && git add -A && git commit -m "[Generated] {}" && git push'\
            .format(publish_path, time.strftime("%Y-%m-%d")))


@task
def publish(ctx):
    """Build a publication version of the blog."""
    ctx.run('pelican -s publishconf.py')


@task
def publish_carefully(ctx):
    """(Carefully) Build a publication version of the blog.

    i.e. fail on any warnings from pelican."""
    ctx.run('pelican -s publishconf.py --fatal=warnings')


# Add devsever
# only works on Windows
#  need to kill the second window manually
@task
def devserver(ctx):
    """regeneration and serve."""
    regenerate(ctx)
    serve(ctx)


@task
def test(ctx):
    """Test invoke is working."""
    #print(ctx)
    print(run)
    ctx.run('dir')
    #run('dir', shell=INVOKE_SHELL)
