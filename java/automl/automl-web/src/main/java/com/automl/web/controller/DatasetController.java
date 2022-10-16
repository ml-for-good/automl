package com.automl.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author wangqingwei
 * Created on 2022-08-10
 */
@RestController
@RequestMapping("/namespaces/{namespace}/datasets")
public class DatasetController {
    private static final Logger logger = LoggerFactory.getLogger(DatasetController.class);
}
