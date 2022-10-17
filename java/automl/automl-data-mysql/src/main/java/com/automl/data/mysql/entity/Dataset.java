package com.automl.data.mysql.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
@TableName("ml_dataset")
@Data
public class Dataset {

    private long id;
    private String name;
    private String description;
    private long namespaceId;
    private String uri;
    private long creatorId;
    private long createTime;
    private long updaterId;
    private long updateTime;
}
