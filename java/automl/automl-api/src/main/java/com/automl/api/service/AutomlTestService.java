package com.automl.api.service;

import org.springframework.stereotype.Service;

@Service
public interface AutomlTestService<T> {

    int insert(T t);
}
