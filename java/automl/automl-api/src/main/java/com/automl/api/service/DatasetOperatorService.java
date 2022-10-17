package com.automl.api.service;

import com.automl.api.entity.DatasetVO;
import com.automl.api.entity.PageVO;

/**
 * @author wangqingwei
 * Created on 2022-09-19
 */
public interface DatasetOperatorService {

    DatasetVO insert(DatasetVO datasetVO, long namespace);

    PageVO<DatasetVO> getByNamespaceAndLimit(long namespaceId, int offset, int limit);

    DatasetVO getById(int datasetId);

    DatasetVO update(DatasetVO datasetVO);

    void delete(int datasetId);
}
