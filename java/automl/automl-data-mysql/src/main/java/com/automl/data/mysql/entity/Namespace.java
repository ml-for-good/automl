package com.automl.data.mysql.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
@TableName("ml_namespace")
@Data
public class Namespace {
    private long id;
    private String name;
    private String description;
    private long creatorId;
    private long createTime;
    private long updaterId;
    private long updateTime;
}
