package com.automl.web.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

/**
 * 接口路径前缀配置
 */
@Component
@ConfigurationProperties(prefix = "server.path")
public class PathProperties {
    String globalPrefix = "";

    public String getGlobalPrefix() {
        return globalPrefix;
    }

    public void setGlobalPrefix(String globalPrefix) {
        this.globalPrefix = globalPrefix;
    }
}
