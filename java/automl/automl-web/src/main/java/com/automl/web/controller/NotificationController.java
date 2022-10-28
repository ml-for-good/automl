package com.automl.web.controller;

import com.automl.api.entity.EmailContent;
import com.automl.service.impl.NotificationServiceImpl;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@Slf4j
@RequestMapping("/notify")
@Api("automl Notification")
public class NotificationController {
    @Autowired
    private NotificationServiceImpl notificationService;

    @PostMapping("/sendEmail")
    @ApiOperation(value = "sendSimpleEmail",notes = "send Simple Email")
    public void sendSimpleEmail(@RequestBody EmailContent emailContent){
        log.debug("send Simple Email");
        notificationService.sendMiMeEmail(emailContent);
    }
}
