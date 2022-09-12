#-*- coding:utf-8 -*-

import setuptools
from sphinxcontrib import youtube


setuptools.setup(
    name='sphinxcontrib.youtube',
    version=youtube.__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'sphinx'
        ],
    url='https://github.com/ArduPilot/sphinxcontrib-youtube',
    description='''embedding youtube videos into sphinx''',
    long_description=youtube.__doc__,
    namespace_packages=['sphinxcontrib'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
        ]
)
