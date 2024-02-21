from setuptools import setup, find_packages

setup(
    name = 'mypackage1',
    version = '0.1',
    packages = find_packages(exclude = ['tests*']),
    license = 'COR',
    description = 'COR example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/Cyrillerandy/mypackage1',
    author = 'Cyrillerandy',
    author_email = 'omondi309@gmail.com'
)