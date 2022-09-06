# Getting Started

### project modules

| module   | function                                    |
| --------------------------- | ---------------------------------------- |
|automl-api|the definition of the entity or interface|
|automl-common|tool class|
|automl-core|core|
|automl-data-mysql|mysql dao, mapper|
|automl-web|supply restful api|

### environment

jdk-17
maven
idea
lombok plugin

### Guides

The following guides illustrate how to run the project:

#### install mysql and create database and test table

* install docker
* docker images
* docker pull mysql
* docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d mysql
* docker ps
* docker exec -it fa9a47b8a1260ed1f3fff8532a1f91d4b15cef9794ef685769fda54477c ba4a2 /bin/sh
* mysql -uroot -p
* execute command - create database automl
* execute command - CREATE TABLE `automl_test` (
  `id` int DEFAULT NULL,
  `name` varchar(10000) DEFAULT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

| username   | password                                    |
| --------------------------- | ---------------------------------------- |
|root|123456|

#### run java project

* VM options: -Dspring.profiles.active=dev
* default server port 8080
* run com.automl.web.AutomlApplication in local env
* swagger url: http://localhost:8080/swagger-ui/index.html
* curl -X POST "http://localhost:8080/test/insert" -H "accept: */*" -H "Content-Type: application/json" -d "{ \"id\":
  444, \"name\": \"333\"}"

#### Build docker image

build image
```bash
 docker build --build-arg  JAR_FILE=automl-web/target/automl-web-0.0.1-SNAPSHOT.jar -t automl/automl:v1 .
```
The option -t specifies the image name and optionally a username and tag in the ‘username/imagename:tag’ format.
list  image
```bash
docker image ls
```
run
```bash
docker run -d -p 8081:8081 --name automl automl/automl:v1
```
