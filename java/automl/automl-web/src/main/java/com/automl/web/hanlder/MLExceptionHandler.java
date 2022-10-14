package com.automl.web.hanlder;

import com.automl.enums.ResultCode;
import com.automl.execption.MLException;
import com.google.common.collect.ImmutableMap;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.Collections;

/**
 * global exception Handler
 *
 * @author wangqingwei
 * Created on 2022-08-12
 */
@ControllerAdvice
public class MLExceptionHandler {

    @ResponseBody
    @ExceptionHandler({MLException.class})
    public Object exceptionHandler(MLException exception) {
        return ImmutableMap.of("error", ImmutableMap.of(
            "code", exception.getCode().getValue(),
            "message", exception.getMessage(),
            "details", exception.getDetails()));
    }

    @ResponseBody
    @ExceptionHandler({Exception.class})
    public Object exceptionHandler(Exception exception) {
        return ImmutableMap.of("error", ImmutableMap.of(
            "code", ResultCode.UNKNOWN_ERROR.getValue(),
            "message", exception.getMessage(),
            "details", Collections.emptyList()));
    }
}
