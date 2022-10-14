package com.automl.data.mysql.config;

import com.automl.helper.HostInfoHelper;
import com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionTemplate;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;

import javax.sql.DataSource;

/**
 * @author wangqingwei
 * Created on 2022-09-23
 */
@Configuration
public class DataSourceGenConfig {
    private static final Logger logger = LoggerFactory.getLogger(DataSourceGenConfig.class);
    @Value(value = "${mybatis-plus.mapper-locations}")
    private String mapperLocation;
    @Autowired
    private HostInfoHelper hostInfoHelper;
    @Autowired
    @Qualifier("primaryDataSource")
    private DataSource primaryDataSource;

    private DataSource getDataSource() {
        logger.info("dataSource load env : {}", hostInfoHelper.active());
        return primaryDataSource;
    }

    /**
     * 注意: 集成mybatis-plus时, SqlSessionFactory需要用MybatisSqlSessionFactoryBean构造,
     * 而不是SqlSessionFactoryBean
     */
    @Bean(name = "sqlSessionFactory")
    @Primary
    public SqlSessionFactory primarySqlSessionFactory() throws Exception {
        MybatisSqlSessionFactoryBean sqlSessionFactoryBean = new MybatisSqlSessionFactoryBean();
        sqlSessionFactoryBean.setDataSource(getDataSource());
        sqlSessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver()
            .getResources(mapperLocation));
        return sqlSessionFactoryBean.getObject();
    }

    @Bean(name = "transactionManager")
    @Primary
    public DataSourceTransactionManager primaryTransactionManager() {
        return new DataSourceTransactionManager(getDataSource());
    }

    @Bean(name = "sqlSessionTemplate")
    @Primary
    public SqlSessionTemplate primarySqlSessionTemplate(@Qualifier("sqlSessionFactory") SqlSessionFactory sqlSessionFactory) {
        return new SqlSessionTemplate(sqlSessionFactory);
    }
}
