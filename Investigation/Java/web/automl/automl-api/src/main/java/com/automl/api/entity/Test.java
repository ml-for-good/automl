package com.automl.api.entity;

import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
@Data
public class Test {

    @ApiModelProperty(value = "id")
    private int id;

    @ApiModelProperty(value = "name")
    private String name;

}
