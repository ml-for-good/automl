package com.automl.data.mysql.repository;

import com.automl.data.mysql.entity.Namespace;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
public interface NamespaceRepository {

    Namespace getById(long id);
}
