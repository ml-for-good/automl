package com.automl.service.impl;

import com.automl.api.entity.DatasetVO;
import com.automl.api.entity.PageVO;
import com.automl.api.service.DatasetOperatorService;
import com.automl.data.mysql.entity.Dataset;
import com.automl.data.mysql.entity.Namespace;
import com.automl.data.mysql.repository.DatasetRepository;
import com.automl.data.mysql.repository.NamespaceRepository;
import com.automl.enums.ResultCode;
import com.automl.execption.MLException;
import io.github.qingguox.date.DateConvertUtils;
import io.github.qingguox.json.JacksonUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

import static com.automl.enums.ResultCode.UNKNOWN_ERROR;

/**
 * @author wangqingwei
 * Created on 2022-09-19
 */
@Lazy
@Service
public class DatasetOperatorServiceImpl implements DatasetOperatorService {

    @Autowired
    private DatasetRepository datasetRepository;
    @Autowired
    private NamespaceRepository namespaceRepository;

    @Override
    public PageVO<DatasetVO> getByNamespaceAndLimit(long namespaceId, int offset, int limit) {
        final Namespace namespace = namespaceRepository.getById(namespaceId);
        if (namespace == null) {
            throw new MLException(ResultCode.PARAM_INVALID, "not such namespace : " + namespaceId);
        }

        final List<Dataset> datasetList =
            datasetRepository.getByNamespaceAndLimit(namespace.getId(), offset, limit);
        final long totalCount = datasetRepository.getCountByNamespace(namespace.getId());
        final List<DatasetVO> datasetVOList =
            datasetList.stream().map(this::buildDatasetVO).collect(Collectors.toList());
        return PageVO.<DatasetVO>newBuilder().setList(datasetVOList).setTotalCount(totalCount).build();
    }

    @Override
    public DatasetVO getById(int datasetId) {
        Dataset dataset = datasetRepository.getById(datasetId);
        if (dataset == null) {
            throw new MLException(ResultCode.PARAM_INVALID, "not such dataset : " + datasetId);
        }
        return buildDatasetVO(dataset);
    }

    @Override
    public DatasetVO update(DatasetVO datasetVO) {
        long datasetId = datasetVO.getId();
        Dataset dataset = datasetRepository.getById(datasetId);
        if (dataset == null) {
            throw new MLException(UNKNOWN_ERROR, "no such dataset! vo : "  + JacksonUtils.toJSON(datasetVO));
        }

        dataset.setId(datasetId);
        dataset.setName(datasetVO.getName());
        dataset.setDescription(datasetVO.getDescription());
        dataset.setUri(datasetVO.getUri());
        dataset.setNamespaceId(datasetVO.getNamespaceId());
        // TODO updaterId is adminId or method input
        dataset.setUpdaterId(1);
        dataset.setUpdateTime(System.currentTimeMillis());

        int result = datasetRepository.update(dataset);
        if (result == 0) {
            throw new MLException(UNKNOWN_ERROR, "dataset update fail! vo : "  + JacksonUtils.toJSON(datasetVO));
        }
        return buildDatasetVO(dataset);
    }

    @Override
    public void delete(int datasetId) {
        int result = datasetRepository.delete(datasetId);
        if (result == 0) {
            throw new MLException(UNKNOWN_ERROR, "dataset delete fail! datasetId : "  + datasetId);
        }
    }

    @Override
    public DatasetVO insert(DatasetVO datasetVO, long namespaceId) {
        final Namespace namespace = namespaceRepository.getById(namespaceId);
        if (namespace == null) {
            throw new MLException(ResultCode.PARAM_INVALID, "not such namespaceId : " + namespaceId);
        }

        Dataset dataset = new Dataset();
        dataset.setName(datasetVO.getName());
        dataset.setDescription(datasetVO.getDescription());
        dataset.setUri(datasetVO.getUri());
        dataset.setNamespaceId(namespaceId);
        // TODO creatorId is adminId or method input
        dataset.setCreatorId(1);
        dataset.setCreateTime(System.currentTimeMillis());
        final long id = datasetRepository.insert(dataset);
        dataset.setId(id);
        return buildDatasetVO(dataset);
    }

    public DatasetVO buildDatasetVO(Dataset dataset) {
        DatasetVO datasetVO = new DatasetVO();
        datasetVO.setId(dataset.getId());
        datasetVO.setName(dataset.getName());
        datasetVO.setDescription(dataset.getDescription());
        datasetVO.setNamespaceId(dataset.getNamespaceId());
        datasetVO.setUri(dataset.getUri());
        datasetVO.setCreateTime(DateConvertUtils.getDefaultDateByTimeStamp(dataset.getCreateTime()));
        return datasetVO;
    }
}
