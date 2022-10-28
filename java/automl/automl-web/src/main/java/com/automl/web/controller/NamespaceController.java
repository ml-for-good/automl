package com.automl.web.controller;

import com.automl.enums.ResultCode;
import com.automl.execption.MLException;
import com.google.common.collect.ImmutableMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

/**
 * @author wangqingwei
 * Created on 2022-10-17
 */
@RestController
@RequestMapping("/namespaces/{namespace}")
public class NamespaceController {

    private static final Logger logger = LoggerFactory.getLogger(NamespaceController.class);

    @PostMapping(value = "/files/{filename}", consumes = MediaType.APPLICATION_OCTET_STREAM_VALUE)
    public Object putFile(@PathVariable(value = "namespace") long namespaceId,
                             @PathVariable(value = "filename") String filename, @RequestParam MultipartFile file) {
        logger.info("putFile req namespaceId : {}, filename : {}",
            namespaceId, filename);
        if (file.isEmpty()) {
            throw new MLException(ResultCode.PARAM_INVALID, "文件不能为空");
        }
        // uploadFile
        String uri = "";
        return ImmutableMap.of("uri", uri);
    }
}
