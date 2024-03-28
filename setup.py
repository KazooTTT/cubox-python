from setuptools import setup
from setuptools import find_packages

VERSION = '0.1.0'

setup(
    name='cubox-python',  # package name
    version=VERSION,  # package version
    description='a cubox python sdk',  # package description
    packages=find_packages(),
    zip_safe=False,
    author_email='yjwang.echo@gmail.com',
    author='kazoottt',
    license='MIT',
    url='https://github.com/kazoottt/cubox-python',
    install_requires=[
        'requests',
    ],
)
