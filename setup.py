#!/usr/bin/env python
import subprocess
from distutils.core import setup

version = subprocess.check_output(['git', 'describe', '--always', '--tag'])\
                    .strip()

setup(
    name='planecrash',
    description='Celebrity Planecrash',
    version=version,
    author='Matt DeBoard',
    author_email='matt.deboard@gmail.com',
    url='http://celebrityplanecrash.com',
    license='Other/Proprietary License',
    data_files=(
        ('/home/matt/planecrash/requirements', ['prod.txt']),
    ),
    packages=[
        'planecrash',
        'fuselage'
    ],
    package_data={
        'fuselage': [
            'templates/*.html',
            'templatetags/*.py',
        ],
        'planecrash': [
            'settings/*.py',
        ]
    }
)
