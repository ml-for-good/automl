package com.automl.configuration;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;


/**
 *
 */
@Configuration
@MapperScan("com.automl.data.mysql.mapper")
public class MyBatisPlusConfig {

}
