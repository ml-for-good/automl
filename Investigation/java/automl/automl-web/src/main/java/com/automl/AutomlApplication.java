package com.automl;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan({"com.automl.*"})
public class AutomlApplication {

  public static void main(String[] args) {
    SpringApplication.run(AutomlApplication.class, args);
  }

}
