package com.automl.data.mysql.repository.impl;

import com.automl.data.mysql.entity.Namespace;
import com.automl.data.mysql.mapper.NamespaceMapper;
import com.automl.data.mysql.repository.NamespaceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Service;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
@Lazy
@Service
public class NamespaceRepositoryImpl implements NamespaceRepository {

    @Autowired
    private NamespaceMapper namespaceMapper;

    @Override
    public Namespace getById(long id) {
        return namespaceMapper.selectById(id);
    }
}
