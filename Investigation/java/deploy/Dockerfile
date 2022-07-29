FROM busybox as builder
WORKDIR /target
ARG JAR_FILE
ADD ${JAR_FILE} ./app.jar
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
EXPOSE 8080
COPY --from=builder target/app.jar ./app.jar
ENTRYPOINT ["java", "-jar","/app/app.jar"]

