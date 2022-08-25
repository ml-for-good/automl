# syntax=docker/dockerfile:1

FROM busybox as builder
WORKDIR /target
ARG JAR_FILE
ADD ${JAR_FILE} ./app.jar
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

FROM eclipse-temurin:17.0.4_8-jre-jammy
WORKDIR /app
EXPOSE 8080
COPY --from=builder target/app.jar ./app.jar
ENTRYPOINT exec java -Dspring.profiles.active=dev -jar /app/app.jar
