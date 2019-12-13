#author: Chenfei.Jia(jchenfei@fortinet.com)
#Alpha version
A simple todo-list app-server using flask, SQLAlchemy, jwt
features:
    - user register
    - user login
    - user logout(uncomplete)
    - todo-list modification(one element each request)
Possible improvements in the future:
    - separate app-server and DB into different containers
    - batch modification on todo-list
    - build index for better todo-list lookup
            (can be query by keywords in title and context)

#Modification form Alpha
how to build:
    docker-compose build
how to run:
    docker-compose run
how to test:
    import postman test cases in test folder, remember setting the token in header
