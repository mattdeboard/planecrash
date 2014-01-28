import os

from fabric.api import env, put, run, sudo
from fabric.decorators import roles

env.roledefs.update({
    'prod': ['54.201.248.175'],
})


@roles('prod')
def push_code(filepath):
    filename = os.path.basename(filepath)
    put(filepath, '/tmp')
    run('tar -xzf /tmp/%s -C /opt/apps/planecrash --strip 1' % filename)
    sudo('touch /opt/apps/planecrash/uwsgi-planecrash.ini')
