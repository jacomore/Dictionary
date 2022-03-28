from setuptools import setup 


setup(
    name = 'Dictionary',
    version = '0.1.0',
    packages = ['app'],
    install_requires = ["numpy","pandas" ],
    entry_points = {
        'console_scripts': [
            'myapp = app.__main__:main',
        ]
    })
