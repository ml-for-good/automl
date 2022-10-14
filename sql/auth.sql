create table ml_group
(
    id         bigint auto_increment
        primary key,
    group_name varchar(64) null comment '分组名称'
)
    comment '分组表';

create table ml_menu
(
    id        bigint auto_increment
        primary key,
    menu_name varchar(64)  not null comment '菜单名称',
    menu_url  varchar(256) null comment '菜单url',
    parent_id bigint       null comment '父级id'
)
    comment '菜单表';

create table ml_menu_scope
(
    id       bigint auto_increment
        primary key,
    menu_id  bigint not null,
    scope_id bigint not null
)
    comment '菜单与接口关联表';

create table ml_role
(
    id          bigint auto_increment
        primary key,
    code        varchar(64)              not null comment 'code, 管理员-admin',
    name        varchar(256)             null,
    description varchar(2048) default '' null comment '描述',
    constraint ml_role_pk
        unique (code)
)
    comment '角色表';

create table ml_role_group
(
    id       bigint auto_increment
        primary key,
    group_id bigint not null,
    role_id  bigint not null
)
    comment '角色分组表';

create table ml_role_scope
(
    id       bigint not null
        primary key,
    role_id  bigint not null,
    scope_id bigint not null
)
    comment '角色与API功能关联表';

create table ml_role_user
(
    id      bigint auto_increment
        primary key,
    user_id bigint null,
    role_id bigint null
)
    comment '用户角色表';

create table ml_scope
(
    id          bigint auto_increment
        primary key,
    code        varchar(64)      null comment 'function code',
    url         varchar(256)     null comment '接口api地址，规则为ant path',
    create_time bigint default 0 null,
    update_time bigint default 0 null
)
    comment 'API功能表';

create table ml_user
(
    id            bigint auto_increment
        primary key,
    email         varchar(256)         null,
    fullName      varchar(64)          null comment '姓名',
    password      varchar(64)          null comment '密码',
    init_password tinyint(1) default 0 null comment '是否修改过初始化密码',
    create_id     bigint     default 0 null,
    create_time   bigint     default 0 null,
    update_id     bigint     default 0 null,
    update_time   bigint     default 0 null
)
    comment '用户表';

create table ml_user_group
(
    id       bigint auto_increment
        primary key,
    user_id  bigint not null,
    group_id bigint not null
)
    comment '用户分组表';

