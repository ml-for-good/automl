package com.automl.api.entity;

import java.util.Collections;
import java.util.List;

/**
 * @author wangqingwei
 * Created on 2022-08-14
 */
public class PageVO<T> {
    private List<T> results;
    private long totalCount;

    public PageVO(Builder<T> builder) {
        setResults(builder.list);
        setTotalCount(builder.totalCount);
    }

    public static <T> Builder<T> newBuilder() {
        return new Builder<>();
    }

    public List<T> getResults() {
        return results;
    }

    public void setResults(List<T> results) {
        this.results = results;
    }

    public long getTotalCount() {
        return totalCount;
    }

    public void setTotalCount(long totalCount) {
        this.totalCount = totalCount;
    }

    public static <T> PageVO<T> getNewInstance() {
        return PageVO.<T>newBuilder().setList(Collections.emptyList()).build();
    }

    public static final class Builder<T> {
        private long totalCount;
        private List<T> list;

        public Builder() {
        }

        public Builder<T> setTotalCount(long val) {
            totalCount = val;
            return this;
        }

        public Builder<T> setList(List<T> val) {
            list = val;
            return this;
        }

        public PageVO<T> build() {
            return new PageVO<>(this);
        }
    }
}
