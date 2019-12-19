# Todo-list
A simple todo-list web application server.
## Dependencies
* Docker
* Flask
* SQLAlchemy
* JWT
* Nginx
## How to build
* install latest docker hub
* download this project and cd to it's base dir
* run build command:
    >     docker build -t todo-list:latest .
## How to run
if you have only one docker node, run following command to start/stop services on your node with _deploy_ key being ignored:
>     #start service
>     docker-compose up
>     #stop service
>     docker-compose down
if you have multiple node within current swarm, run following command to deploy/remove services to you cluster:
>     #start service
>     docker stack deploy --compose-file=docker-compose.yml todo-list
>     #stop service
>     docker stack rm todo-list
visit http://localhost:80/admin/init to initialize DB. (TODO: using manager.py)
## How to test
import json file under test dir to postman, modify headers and bodies to test.
## Features
* user register
* user login
* user logout(not complete)
* todo-list modification(one element each request)
## TODO
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
[Microsoft REST guides](https://docs.microsoft.com/en-us/azure/architecture/guide/)  
[How to run flask on docker swarm](https://testdriven.io/blog/running-flask-on-docker-swarm/)  
[Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)  
[Flask Tutorial](http://www.patricksoftwareblog.com/all-posts/)  
[API design best practices](https://www.moesif.com/blog/api-guide/api-design-guidelines/#general-best-practices)  
[REST vs RPC](https://www.smashingmagazine.com/2016/09/understanding-rest-and-rpc-for-http-apis/)  
[Why REST](https://medium.com/@suhas_chatekar/why-you-should-use-the-recommended-http-methods-in-your-rest-apis-981359828bf7)  
[REST auth](https://stackoverflow.com/questions/319530/restful-authentication)  
[OAuth2.0 Doc](https://tools.ietf.org/html/rfc6749#section-7)  
