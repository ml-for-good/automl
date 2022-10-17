package com.automl.data.mysql.mapper;

import com.automl.data.mysql.entity.Dataset;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
@Mapper
public interface DatasetMapper extends BaseMapper<Dataset> {
    long insertAndGetId(Dataset dataset);

    long getCountByNamespace(long namespaceId);

    List<Dataset> getByNamespaceAndLimit(long namespaceId, int offset, int limit);
}
