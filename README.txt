===========
Open Ducats
===========
-----------------------------
Open Source Currency Platform
-----------------------------

Introduction
============

Open Ducats is an open source currency platform built using django, the popular python web framework. The goal is to allow people to make minting and managing virtual currencies as easy and accessible as blogging.

Installation
============

Open Ducats is a set of django apps that adhers to best practices as much as possible. You can install it and run it the same as other django applications. 

* Create a django project.
* Make sure the requirements are in your python path>
* Add the apps to your ``INSTALLED_APPS`` in settings.py. 
* Create a local_settings.py with your choice of database configuration
* ``python manage.py syncdb``
* ``python manage.py migrate``

The apps are provided in a sample project to make things easier. You should be able to just edit the settings.py, start the development server, and go.

Requirements
------------

I personally use a bunch of development tools to make my life easier, but they are not strictly necessary to get this code up and running. If you like, I have provided a pip-dependencies.txt file that will make it easier to duplicate my development environment. However, the only actual dependencies are as follows.

* python ( I use version 2.5.2 )
* django 1.0 
* south 0.5

Notes
=====

This project is hosted on github at http://github.com
