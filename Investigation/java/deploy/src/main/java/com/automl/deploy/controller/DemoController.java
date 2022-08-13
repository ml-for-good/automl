package com.automl.deploy.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author <a href="mailto:cqmike0315@gmail.com">chenqi</a>
 * @version 1.0
 */
@RequestMapping("/demo")
@RestController
public class DemoController {

    /**
     * 测试demo方法
     *
     * @author cqmike
     * @since 1.0.0
     * @return
     */
    @GetMapping("/test")
    public String demo() {
        return "true";
    }
}
