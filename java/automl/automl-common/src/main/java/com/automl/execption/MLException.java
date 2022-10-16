package com.automl.execption;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import com.automl.enums.ResultCode;

/**
 * @author wangqingwei
 * Created on 2022-08-14
 */
public class MLException extends RuntimeException {
    private ResultCode code;
    private String message;
    private List<Object> details;

    public MLException(ResultCode code) {
        super(code.getDesc());
        this.code = code;
        this.message = code.getDesc();
    }

    public MLException(ResultCode code, String message) {
        super(message);
        this.code = code;
        this.message = message;
    }

    public MLException(ResultCode code, String message, Object... detail) {
        super(message);
        this.code = code;
        this.message = message;
        this.details = Arrays.asList(detail);
    }

    public MLException(ResultCode code, Throwable cause) {
        super(code.getDesc(), cause);
        this.code = code;
        this.message = code.getDesc();
    }


    public MLException(ResultCode code, String msg, Throwable cause) {
        super(msg, cause);
        this.code = code;
        this.message = message;
    }

    public MLException(ResultCode code, String message, Throwable cause, Object... detail) {
        super(message, cause);
        this.code = code;
        this.message = message;
        this.details = Arrays.asList(detail);
    }

    public ResultCode getCode() {
        return code;
    }

    public String getMessage() {
        return message;
    }

    public List<Object> getDetails() {
        if (details == null) {
            details = Collections.emptyList();
        }
        return details;
    }
}
