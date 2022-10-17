package com.automl.data.mysql.repository;

import com.automl.data.mysql.entity.Dataset;

import java.util.List;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
public interface DatasetRepository {

    long insert(Dataset dataset);

    long getCountByNamespace(long namespaceId);

    List<Dataset> getByNamespaceAndLimit(long id, int offset, int limit);

    Dataset getById(long datasetId);

    int update(Dataset dataset);

    int delete(int datasetId);
}
