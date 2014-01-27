from fabric.api import *
from fabric.decorators import roles

env.roledefs.update({
    'prod': ['54.201.248.175'],
})


@roles('prod')
def push_code():
    sudo('supervisorctl stop planecrash')
    put('../*', '/opt/apps/planecrash')
    sudo('supervisorctl start planecrash')
