import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='comtrend_stats',
    version='0.1',
    packages=['contrend_stats'],
    include_package_data=True,
    license='BSD License',
    description='Command to retrieve Comtrend Stats, as the router P401-402TLF-C04_R05 does not have SNMP',
    long_description=README,

    url='http://jpardobl.com',
    author='Javier Pardo Blasco(jpardobl)',
    author_email='jpardo@digitalhigh.es',
    install_requires = (
      #"simplejson==2.6.2",
      "BeautifulSoup==3.2.1",
      "requests==2.1.0",
      "simplejson==3.3.1",
    ),
    test_suite='contrend_stats.tests.main',
    #tests_require=("selenium", "requests"),
    classifiers=[
        'Environment :: Home Automation',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

)
