from setuptools import setup, find_packages

with open('README.MD', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ToDo_App',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/qrave1/ToDo_Web_App',
    license='MIT',
    author='qrave1',
    author_email='liveartem@yandex.ru',
    description='My ToDo web application',
    long_description=long_description,
    install_requires=requirements,
    scripts=['main.py']
)
