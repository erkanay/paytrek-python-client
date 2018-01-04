from distutils.core import setup

setup(
    name='paytrek',
    version='0.1',
    description='Python client library for Paytrek API',
    author='Erkan Ay',
    author_email='erkanaycom@gmail.com',
    url='https://github.com/paytrek/paytrek-python-client',
    keywords=['paytrek', 'client', 'payment', 'gateway'],
    install_requires=[
        "requests",
    ],
)
