package com.automl.api.service;

import com.automl.api.entity.EmailContent;
import org.springframework.stereotype.Service;

@Service
public interface NotificationService {
    void sendMiMeEmail(EmailContent emailContent);

    void sendSMS();
}
