# Docker Tutorial
Docker Tutorial for data domain

### 1. Basic commands with image tags

* docker build -t fastapi_image:0.0.1 . [. if you're in same directory else folder name to be provided where dockerfile is. 0.0.1 is the tag]
* docker run -dp 8000:8000 --name fastapi_container fastapi_image:0.0.1 [create app container]

### 2. Creating Container in Interactive mode
* docker run -it -dp 8000:8000 fastapi_container fastapi_image:0.0.1 (with deattach and interactive mode)

* docker run -it [IMAGE_NAME] [COMMAND]
* eg: docker run -it fastapi_image /bin/sh

### 3. Basic Command for deleting and listing containers & images
* docker ps -a
* docker image ls
* docker stop <container_name>
          [OR]
* docker stop <containe_id>

##### Deleting container
* docker rm <container_name> OR docker rm <container_id>
##### Deleting image
* docker rmi <image_id> OR docker rmi <image_name> (if tag provided, then image:tag_name should be mentioned)

### 4. Network
Important for running various services running on same network
###### List all the availabe networks
* docker network ls
* docker network create <NETWORK_NAME>
* docker network rm <NETWORK_NAME>

##### Removing All Unused Networks (docker network prune)
* docker network prune

##### Force remove all unused networks without a prompt
* docker network prune -f
* docker system prune
* docker system prune --volumes


### 5. Running container on network

Running fastapi container on port 8000
* docker run -dp 8000:8000 --name <container_name> --network <network_name> <image_name>
* (IMAGE) docker build -t fastapi_image:0.0.1 .
* (CONTAINER) docker run -dp 8000:8000 --name fastapi_container --network harry_network fastapi_image:0.0.1

* (IMAGE) docker build -t mysql_image:0.0.1 .
* (CONTAINER) docker run --name mysql_container --network harry_network mysql_image


### 6. Docker Compose
* docker compose up --build (for updating image)
* docker compose up
* docker compose down -v

#### building image for pushing to docker hub
1. docker build -t <USERNAME/IMAGE_NAME> .
2. docker login
3. docker push

#### pulling the image from hub
1. docker run -d --name <container_name> <USERNAME/IMAGE_NAME>

