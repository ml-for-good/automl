package com.automl.web.controller;

import com.automl.api.service.DatasetOperatorService;
import com.google.common.collect.Maps;
import io.github.qingguox.json.JacksonUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

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
        @RequestBody Map<String, String> map) {
        logger
            .info("putDataset req namespaceId : {}, map : {}",
                namespaceId, JacksonUtils.toJSON(map));
        final String name = map.get("name");
        final String description = map.get("description");
        final String uri = map.get("uri");
//        return datasetOperatorService.insertDataset(namespaceId, name, description, uri);
        return new Object();
    }

    @GetMapping(value = "/")
    public Object getDatasetList(@PathVariable(value = "namespace") long namespaceId,
        @RequestParam(value = "offset", required = false, defaultValue = "0") int offset,
        @RequestParam(value = "limit", required = false, defaultValue = "100") int limit) {
//        return datasetOperatorService.getByNamespaceAndLimit(namespaceId, offset, limit);
        return Maps.newHashMap();
    }
}
