# Copyright (c) 2015, OLogN Technologies AG. All rights reserved.
#
# Redistribution and use of this file in source and compiled
# forms, with or without modification, are permitted
# provided that the following conditions are met:
#     * Redistributions in source form must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in compiled form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the OLogN Technologies AG nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL OLogN Technologies AG BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE

from setuptools import find_packages, setup

from smartanthill import (__author__, __description__, __email__, __license__,
                          __title__, __url__, __version__)

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=open("README.rst").read(),
    author=__author__,
    author_email=__email__,
    url=__url__,
    license=__license__,
    install_requires=[
        "platformio",
        "pyserial",
        "twisted"
    ],
    packages=find_packages()+["twisted.plugins"],
    package_data={"smartanthill": ["*.json"]},
    entry_points={
        "console_scripts": [
            "smartanthill = smartanthill.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Twisted",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Topic :: Adaptive Technologies",
        "Topic :: Communications",
        "Topic :: Home Automation",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol"
        "Translator",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Networking",
        "Topic :: Terminals :: Serial"
    ]
)