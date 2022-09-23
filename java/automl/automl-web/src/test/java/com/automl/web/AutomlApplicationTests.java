package com.automl.web;

import com.automl.data.mysql.entity.AutomlTest;
import com.automl.data.mysql.mapper.TestMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@ComponentScan({"com.automl.*"})
@SpringBootApplication
class AutomlApplicationTests implements CommandLineRunner {

    @Autowired
    private TestMapper testMapper;

    void insertIntoTest() {
        AutomlTest automlTest = new AutomlTest();
        automlTest.setId(102);
        automlTest.setName("sss");
        int count = testMapper.insert(automlTest);
        System.out.println("insert count : {}" + count);
    }

    @Override
    public void run(String... args) throws Exception {
        insertIntoTest();
    }

    public static void main(String[] args) {
        SpringApplication.run(AutomlApplicationTests.class, args);
    }
}
