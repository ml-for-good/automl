package com.automl.web.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.config.annotation.PathMatchConfigurer;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * 配置统一的后台接口访问路径的前缀
 */
@Configuration
public class PathConfig implements WebMvcConfigurer {
    @Autowired
    private PathProperties pathProperties;

    @Override
    public void configurePathMatch(PathMatchConfigurer configurer) {
        configurer
            .addPathPrefix(pathProperties.globalPrefix, c -> c.isAnnotationPresent(RestController.class));
    }
}
