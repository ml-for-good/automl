package com.automl.cms.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @author wangqingwei
 * Created on 2022-08-09
 */
@SpringBootApplication(scanBasePackages = "com.automl")
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
