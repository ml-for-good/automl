package com.automl.api.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class EmailContent {
    /**
     * 接收方
     */
    private String[] receiver;
    /**
     * 标题
     */
    private String subject;
    /**
     * 正文
     */
    private String content;
    /**
     * 附件
     */
    private String attachment;
}
