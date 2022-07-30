package com.automl.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    Logger logger = LoggerFactory.getLogger(HelloController.class.getName());

    @GetMapping("/hello")
    public String getHello() {
        logger.info("call to /hello");
        return "Hello world";
    }
}
