package com.automl.service.impl;


import com.automl.api.entity.Test;
import com.automl.api.service.AutomlTestService;
import com.automl.data.mysql.entity.AutomlTest;
import com.automl.data.mysql.mapper.TestMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class AutoMlTestServiceImpl implements AutomlTestService<Test> {

    @Autowired
    private TestMapper mapper;

    @Override
    public int insert(Test test) {
        log.info("Entering insert test:{}", test);

        AutomlTest automlTest = new AutomlTest();
        BeanUtils.copyProperties(test, automlTest);
        return mapper.insert(automlTest);
    }
}
