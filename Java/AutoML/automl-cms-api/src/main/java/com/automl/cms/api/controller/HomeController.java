package com.automl.cms.api.controller;


import static com.automl.cms.api.model.Result.ok;
import static org.springframework.web.bind.annotation.RequestMethod.GET;
import static org.springframework.web.bind.annotation.RequestMethod.HEAD;
import static org.springframework.web.bind.annotation.RequestMethod.POST;

import java.net.InetAddress;
import java.net.UnknownHostException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.automl.cms.api.config.IpConfiguration;
import com.google.common.collect.Maps;

@RestController
@RequestMapping("/")
public class HomeController {

    private static final Logger logger = LoggerFactory.getLogger(HomeController.class);

    @Autowired
    IpConfiguration ip;

    @RequestMapping(value = "/", method = {HEAD, GET, POST})
    public String heathCheck() throws UnknownHostException {
        InetAddress address = InetAddress.getLocalHost();
        logger.info("IP : {}, PORT : {}", address.getHostAddress(), ip.getPort());
        return "ok";
    }

    @RequestMapping(value = "/check", method = {POST, GET, HEAD})
    private Object healthCheck() {
        return ok(Maps.newHashMap());
    }
}
