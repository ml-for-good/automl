package com.automl.web;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@ComponentScan({"com.automl.*"})
@MapperScan("com.automl.data.mysql.mapper")
@EnableWebMvc
@EnableSwagger2
@SpringBootApplication
public class AutomlApplication {

    public static void main(String[] args) {
        SpringApplication.run(AutomlApplication.class, args);
    }

}
