#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(
    name="restcountries",
    version="1.1.3",
    description="A Python client for the RestCountries API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/restcountries.git",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "requests==2.20.0",
        "six==1.11.0",
    ],
    keywords="restcountries library countries",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=True,
)
