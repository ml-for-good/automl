package com.automl.web.controller;

import com.automl.api.entity.Test;
import com.automl.api.service.AutomlTestService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api("auto ml test")
@RestController
@RequestMapping("/test")
@Slf4j
@Service
public class AutoMlTestController {

    @Autowired
    private AutomlTestService<Test> testService;

    @PostMapping("/insert")
    @ApiOperation(value = "create test", notes = "create test api")
    public int insert(@RequestBody Test test) {
        log.info("Entering insert test");
        return testService.insert(test);
    }
}
