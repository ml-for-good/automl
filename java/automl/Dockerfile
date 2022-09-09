# syntax=docker/dockerfile:1
FROM maven:3.8.6-eclipse-temurin-17-focal as build
WORKDIR /opt/app
COPY automl-api/pom.xml automl-api/pom.xml
COPY automl-common/pom.xml automl-common/pom.xml
COPY automl-web/pom.xml automl-web/pom.xml
COPY automl-data-mysql/pom.xml automl-data-mysql/pom.xml
COPY automl-core/pom.xml automl-core/pom.xml
COPY pom.xml .

COPY automl-api/src automl-api/src
COPY automl-common/src automl-common/src
COPY automl-web/src automl-web/src
COPY automl-data-mysql/src automl-data-mysql/src
COPY automl-core/src automl-core/src

RUN mvn -f /opt/app/pom.xml clean package -Dmaven.test.skip=true

#FROM busybox as builder
#WORKDIR /target
#ARG JAR_FILE
#ADD ${JAR_FILE} ./app.jar
#RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

FROM busybox as builder
WORKDIR /target
COPY --from=build /opt/app/automl-web/target/automl-web-0.0.1-SNAPSHOT.jar  ./app.jar
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

FROM eclipse-temurin:17.0.4_8-jre-jammy
WORKDIR /app
EXPOSE 8080
COPY --from=builder target/app.jar ./app.jar
ENTRYPOINT exec java -Dspring.profiles.active=dev -jar /app/app.jar
