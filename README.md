# Posts Peeling API
API made to serve the posts made from a specified user.

You can try the API [here](https://sallve-posts-peeling.herokuapp.com), use one of this e-mails to obtain a valid response:

 - Sincere@april.biz
 - Shanna@melissa.tv
 - Nathan@yesenia.net
 - Julianne.OConner@kory.org

## Requirements
- [docker-compose](https://docs.docker.com/compose/install/)
- [git](https://git-scm.com/)


## Usage
#### Build
```
$ git clone git@github.com:LucasSRocha/posts-peeling-api.git


$ cd posts-peeling-api
```
You can build the docker image and then start it (or do it all at once)
```
$ docker-compose build

$ docker-compose up
```
or
```
$ docker-compose up --build
```
##### You can access image bash and manipulate files inside the container using:

```
 $ docker-compose exec web bash
```

#### Run tests
```
$ docker-compose -f docker-tests.yml run tests
```

#### Usage
There are two ways to obtain the posts related to a user e-mail:

- GET METHOD
    ```
  $ curl -X GET http://localhost:5000/?email=<user_email>
  ```
  it will return the body of the response
  
- POST METHOD
    ```
    $ curl -d "email=<user_email>" -X POST http://localhost:5000/
  ```
  it will return a json response
    
 
## Thought Process
The idea was to build some lightweight and yet robust enough to satisfy the projects requirements.

At first the idea was to deploy the application at AWS lambda but for practicality I ended up deploying at Heroku.
The serverless idea was encouraging because of the easy of use, deploy and maintenance ,using [zappa](https://github.com/Miserlou/Zappa), therefore it would
 be an excellent choice for this application because it would ease some of the worries about concurrent connections and 
 server maintenance.
 
 In the end i've chosen Flask for this project over Django, FastAPI and some other options for the ease of use and fast development
  seeing as it's a lightweight framework I wouldn't be overshooting for some unnecessarily features.
 
 
 - Docker:
    
    I think dockerizing this application will facilitate the development and the testing of the application by sustaining 
    a continuous and constant environment. 
  
  - UnitTest
  
    since the focus was to keep the application lightweight I choose to use Python's built-in test module, although I do 
    think it would be good to do some functional testing with selenium to guarantee the end-user experience.