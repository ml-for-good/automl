package com.automl.data.mysql.repository.impl;

import com.automl.data.mysql.entity.Dataset;
import com.automl.data.mysql.mapper.DatasetMapper;
import com.automl.data.mysql.repository.DatasetRepository;
import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * 做Repository的目的：
 * 屏蔽数据存储模型
 * @author wangqingwei
 * Created on 2022-10-17
 */
@Lazy
@Service
public class DatasetRepositoryImpl implements DatasetRepository {

    @Autowired
    private DatasetMapper datasetMapper;


    @Override
    public long insert(Dataset dataset) {
        return datasetMapper.insertAndGetId(dataset);
    }

    @Override
    public long getCountByNamespace(long namespaceId) {
        return datasetMapper.getCountByNamespace(namespaceId);
    }

    @Override
    public List<Dataset> getByNamespaceAndLimit(@Param("namespaceId") long namespaceId, @Param("offset")int offset, @Param("limit")int limit) {
        return datasetMapper.getByNamespaceAndLimit(namespaceId, offset, limit);
    }

    @Override
    public Dataset getById(long datasetId) {
        return datasetMapper.selectById(datasetId);
    }

    @Override
    public int update(Dataset dataset) {
        return datasetMapper.updateById(dataset);
    }

    @Override
    public int delete(int datasetId) {
       return datasetMapper.deleteById(datasetId);
    }
}
