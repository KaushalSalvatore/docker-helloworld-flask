#### docker-helloworld-flask
Created simple flask with application then containers application in Docker container image and create a docker repository.


#### Steps for create flask project

1. Create virtual environment
```bash
  virtualenv env_name
  env_name = virtual environment name.
```
2. Create requirements.txt file
```bash
Requirements files serve as a list of items to be installed by pip
```
3. intall flask
```bash
    pip install Flask
```
3. Create app.py file  
```bash
    app.py : this file store application route and entry point of application
```

## Steps for start docker container and deploy in docker hub Repository 
1. create a docker file (Dockerfile)
```bash
   Dockerfile : A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image 
   command : 
            FROM 
            COPY
            WORKDIR
            RUN
            CMD
        ```
2. create a docker image
```bash
  docker build -t flask-helloworld .
  flask-helloworld >> docker image name
```
3. run docker image as a container
```bash
  docker run -p 5000:5000 flask-helloworld
  (5000:5000 > host port:container port)  
```

#### deploy docker image in docker hub 
1. docker login in docker hub 
```bash
   docker login
```
2. docker image name should be with your docker user name (kaushalpandey/flask-helloworld)
2.1 rename docker image first method      
```bash
  docker rm -f flask-helloworld
  (remove old docker image)

  docker build -t kaushalpandey/flask-helloworld . 
  (again create new docker image)
```
2.2 rename docker image second  method  
```bash
    docker tag flask-helloworld kaushalpandey/flask-helloworld
				(old name)			(new name)
```
3. push to docker hub 
```bash
docker push kaushalpandey/flask-helloworld:latest
```
```bash
  
```

```bash
 
```

