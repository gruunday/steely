from setuptools import setup, find_packages


with open('README.md') as file:
    readme = file.read()


with open('LICENSE') as file:
    license = file.read()


setup(
    name='steely',
    version='0.0.0',
    description='CPSSD Facebook bot',
    long_description=readme,
    author='Senan Kelly',
    author_email='senan@senan.xyz',
    url='https://github.com/sentriz/steely',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
