try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My First Python Project',
    'author': 'Kim Dokyun',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['helloworldweb'],
    'scripts': [],
    'name': 'helloworld'
}

setup(**config)