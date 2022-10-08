package com.automl.service.impl;

import com.automl.api.entity.EmailContent;
import com.automl.api.service.NotificationService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;

import javax.mail.MessagingException;
import javax.mail.internet.MimeMessage;

@Service
@Slf4j
public class NotificationServiceImpl implements NotificationService {

    @Value("${spring.mail.username}")
    private String emailSender;
    @Autowired
    private JavaMailSender javaMailSender;

    /**
     * 发送MIME邮件，使用HTML模版填充内容
     *
     * @param emailContent
     */
    @Override
    public void sendMiMeEmail(EmailContent emailContent) {
        MimeMessage mimeMessage = javaMailSender.createMimeMessage();
        try {
            MimeMessageHelper mimeMessageHelper = new MimeMessageHelper(mimeMessage, MimeMessageHelper.MULTIPART_MODE_MIXED_RELATED, "UTF-8");
            mimeMessageHelper.setFrom(emailSender);
            mimeMessageHelper.setTo(emailContent.getReceiver());
            mimeMessageHelper.setSubject(emailContent.getSubject());
            mimeMessageHelper.setText(emailContent.getContent(), true);
            javaMailSender.send(mimeMessage);
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
        log.debug("send email success");
    }

    /**
     * TODO：发送短信
     */
    @Override
    public void sendSMS() {

    }
}
