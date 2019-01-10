"""flask-serial Setup."""
from setuptools import setup
from flask_serial import __version__

setup(
    name='flask-serial',
    version=__version__,
    url='https://github.com/RedFalsh/flask-serial.git',
    license='MIT',
    author='Redfalsh',
    author_email='13693421942@163.com',
    description='Flask extension for the Serial',
    long_description="https://github.com/RedFalsh/flask-serial/blob/master/README.md",
    long_description_content_type='text/markdown',
    packages=['flask_serial'],
    platforms='any',
    install_requires=[
        'Flask',
        'typing',
        'pyserial'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)