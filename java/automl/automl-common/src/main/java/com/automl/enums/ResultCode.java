package com.automl.enums;

import io.github.qingguox.enums.IntDescValue;

/**
 * @author wangqingwei
 * Created on 2022-08-14
 */
public enum ResultCode implements IntDescValue {

    UNKNOWN_ERROR(0, "未知错误"),
    SUCCESS(200, "数据正常"),
    PARAM_INVALID(400, "无效参数"),

    ;

    private int code;
    private String msg;

    ResultCode(int code, String msg) {
        this.code = code;
        this.msg = msg;
    }

    @Override
    public String getDesc() {
        return msg;
    }

    @Override
    public int getValue() {
        return code;
    }
}
