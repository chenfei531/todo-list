Todo-list
=====

A simple todo-list web application server.


Dependencies
----------

* Docker
* Flask
* SQLAlchemy
* JWT


How to build
----------

* install latest docker hub
* download this project and cd to it's base dir
* run build command:

.. code-block:: text

    docker build -t todo-list:latest .


How to run
----------

if you have only one docker node, run:

.. code-block:: text

    docker-compose up

if you have multiple node within current swarm, run:

.. code-block:: text

    docker stack deploy --compose-file=docker-compose.yml todo-list

visit http://localhost:80/admin/init to initialize DB.(TODO: using manager.py)


How to test
----------

import json file under test dir to postman, modify headers and bodies to test.


Features
----------

* user register
* user login
* user logout(not complete)
* todo-list modification(one element each request)


TODO
----------

* specify correct http return code (currently not specified)
* add manager.py to maintain the services instead of endpoints that anyone can access
* CRUD of multiple items can be operated within one API call
* modify swagger.yaml file to generate API Docs
* improve logging
* API version control
* add unit test
* cache supports
* pagination
* using ssl


References
----------
(TODO)
