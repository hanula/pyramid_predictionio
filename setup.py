# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='pyramid_predictionio',
    version='0.1.0',
    description='PredictionIO pyramid integration example.',
    long_description=readme,

    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
    ],
    author='Sebastian Hanula',
    author_email='sebastian.hanula@gmail.com',
    url='https://github.com/hanula/pyramid_predictionio',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    zip_safe=False,
    entry_points="""
      # -*- Entry points: -*-
    """,
)
