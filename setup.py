import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='django-payonline',
    version='1.0.0',
    license='ISC',
    description='A Django application for integration with PayOnline System',
    long_description=read('README.rst'),
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP'],
)
