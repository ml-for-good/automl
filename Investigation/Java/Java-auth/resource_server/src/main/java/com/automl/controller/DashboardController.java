package com.automl.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DashboardController {

    Logger logger = LoggerFactory.getLogger(DashboardController.class.getName());

    @GetMapping("/dashboard")
    public String getDashboard() {
        logger.info("call to GET /dashboard");
        return "Welcome to the dashboard GET";
    }

    @PostMapping("/dashboard")
    public String postDashboard() {
        logger.info("call to POST /dashboard");
        return "Welcome to the dashboard POST";
    }
}
