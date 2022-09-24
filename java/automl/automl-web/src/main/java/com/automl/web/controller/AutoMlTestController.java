package com.automl.web.controller;

import com.automl.api.entity.Test;
import com.automl.api.service.AutomlTestService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;

@Api("auto ml test")
@RestController
@RequestMapping("/test")
@Service
public class AutoMlTestController {

    private static final Logger logger = LoggerFactory.getLogger(AutoMlTestController.class);
    @Autowired
    private AutomlTestService<Test> testService;

    @PostMapping("/insert")
    @ApiOperation(value = "create test", notes = "create test api")
    public int insert(@RequestBody Test test) {
        logger.info("Entering insert test");
        return testService.insert(test);
    }
}
