from fabric.api import *
from fabric.decorators import roles

env.roledefs.update({
    'prod': ['54.201.248.175'],
})


@roles('prod')
def push_code():
    local('find ../ -name "*.pyc" -type f -print0 | xargs -0 rm')
    put('../*', '/opt/apps/planecrash')
    sudo('touch /opt/apps/planecrash/uwsgi-planecrash.ini')
