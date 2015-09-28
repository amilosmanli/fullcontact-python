from distutils.core import setup
from fullcontact import VERSION

setup(
    name='fullcontact-python',
    version=VERSION,
    packages=['fullcontact'],
    url='https://github.com/cyberlake/fullcontact-python',
    license='MIT',
    long_description=open('README.md', 'r').read(),
    author='Amil Osmanli',
    author_email='amil@birdleaf.io',
    description='FullContact API SDK for Python',
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
