# guiCalc

### a simple web-based GUI Calculator

### designed using python language and flask framework

#Docker Image Repo: 
https://hub.docker.com/r/mtadese/guicalculator

### Run as a Docker Container
#create Dockerfile
#build Dockerfile 
$ docker build .
#tag docker image 
$ docker tag image-ID guicalc:v1
#run docker container 
$ docker container run -itd --name guicalc -p 7000:7000 guicalc:v1

#test app on browser
$ curl host-IP:7000


