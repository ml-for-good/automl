package com.automl.api.entity;

import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
@Data
public class DatasetVO {
    @ApiModelProperty(value = "id")
    private long id;
    @ApiModelProperty(value = "name")
    private String name;
    @ApiModelProperty(value = "description")
    private String description;
    @ApiModelProperty(value = "namespaceId")
    private long namespaceId;
    @ApiModelProperty(value = "uri")
    private String uri;
    @ApiModelProperty(value = "createTime")
    private String createTime;
}
