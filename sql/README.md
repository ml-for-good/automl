
## TODO
废弃掉以sql文件运行的方式.

## [进行中-待补充]数据存储在mysql

> 注意: 目前用的mysql-version:5.7
> 这个只是DB层面DataStore

> 本地DB中运行 sql/automl.sql 即可.

<b> 注意: 先用automl-test.sql执行, 上线之后我们再使用automl.sql @ALL </b>

## 关系图
![关系图-idea](https://img-blog.csdnimg.cn/2f92476c2e4f4bdbacaa93130af3a989.png)


## Some Table Design FAQ @ALL

### 1. ml_model模型表中其实可以不用有meta_data, 从version中取到即可.
> update default_version -> version
> delete meta_data, can reference  to get meta from version table.

### 2. ml_model中display_name: 命名空间下的名称, 需要唯一?
> I think reference namespace_id.

###
auth.sql中相关字段还需根据原型来完善。

