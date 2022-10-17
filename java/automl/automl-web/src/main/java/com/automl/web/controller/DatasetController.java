package com.automl.web.controller;

import com.automl.api.entity.DatasetVO;
import com.automl.api.service.DatasetOperatorService;
import io.github.qingguox.json.JacksonUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * @author wangqingwei
 * Created on 2022-08-10
 */
@RestController
@RequestMapping("/namespaces/{namespace}/datasets")
public class DatasetController {
    private static final Logger logger = LoggerFactory.getLogger(DatasetController.class);

    @Autowired
    private DatasetOperatorService datasetOperatorService;

    @PostMapping(value = "/")
    public Object putDataset(@PathVariable(value = "namespace") long namespaceId,
                             @RequestBody DatasetVO datasetVO) {
        logger.info("putDataset req namespaceId : {}, datasetVO : {}",
                namespaceId, JacksonUtils.toJSON(datasetVO));
        return datasetOperatorService.insert(datasetVO, namespaceId);
    }

    @GetMapping(value = "/")
    public Object getDatasetList(@PathVariable(value = "namespace") long namespaceId,
                                 @RequestParam(value = "offset", required = false, defaultValue = "0") int offset,
                                 @RequestParam(value = "limit", required = false, defaultValue = "100") int limit) {
        logger.info("getDatasetList namespaceId : {}, offset : {}, limit : {}", namespaceId, offset, limit);
        return datasetOperatorService.getByNamespaceAndLimit(namespaceId, offset, limit);
    }

    @GetMapping(value = "/{dataset}")
    public Object getDatasetById(@PathVariable(value = "namespace") long namespaceId,
                                 @PathVariable(value = "dataset") int datasetId) {
        logger.info("getDatasetById datasetId : {}", datasetId);
        return datasetOperatorService.getById(datasetId);
    }

    @PatchMapping(value = "/{dataset}")
    public Object patchDataset(@PathVariable(value = "namespace") long namespaceId,
                                 @PathVariable(value = "dataset") int datasetId, @RequestBody DatasetVO datasetVO) {
        datasetVO.setId(datasetId);
        logger.info("patchDataset datasetId : {}, datasetVO : {}", datasetId, JacksonUtils.toJSON(datasetVO));
        return datasetOperatorService.update(datasetVO);
    }

    @DeleteMapping(value = "/{dataset}")
    public void deleteById(@PathVariable(value = "namespace") long namespaceId,
                                 @PathVariable(value = "dataset") int datasetId) {
        logger.info("deleteById datasetId : {}", datasetId);
        datasetOperatorService.delete(datasetId);
    }
}
