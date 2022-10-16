package com.automl.helper;

import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Service;

/**
 * 上下文环境切换
 * @author wangqingwei
 * Created on 2022-08-10
 */
@Lazy
@Service
public class HostInfoHelper {
    private static final String TEST_ACTIVE = "test";

    @Value("${spring.profiles.active}")
    private String active;

    public HostInfoHelper() {
        active = StringUtils.defaultIfBlank(active, TEST_ACTIVE);
    }

    public boolean debugTest() {
        return TEST_ACTIVE.equals(active);
    }

    public String active() {
        return active;
    }
}
