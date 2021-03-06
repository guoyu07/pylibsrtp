import os.path
import sys

import setuptools

root_dir = os.path.abspath(os.path.dirname(__file__))
readme_file = os.path.join(root_dir, 'README.rst')
with open(readme_file, encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='pylibsrtp',
    version='0.4.0',
    description='Python wrapper around the libsrtp library',
    long_description=long_description,
    url='https://github.com/jlaine/pylibsrtp',
    author='Jeremy Lainé',
    author_email='jeremy.laine@m4x.org',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['pylibsrtp'],
    install_requires=['cffi'],
)
