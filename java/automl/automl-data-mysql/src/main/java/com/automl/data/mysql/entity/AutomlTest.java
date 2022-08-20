package com.automl.data.mysql.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;


@TableName("automl_test")
@Data
public class AutomlTest {

    private int id;
    private String name;

}
