shell 语法规范：
1.变量名统一用大写
2.方法名统一用小写

使用说明：

发布：
main_admin.sh  publish.sh status.sh

启动：
main_admin.sh start.sh status.sh

停止：
stop.sh  应用名称，如后台—admin
ex: stop.sh admin

一键回滚(上一版本)：
main_admin.sh rollback.sh status.sh

修改配置：

if 公共变量：
       public_config
else(私有变量):
        main_xx.sh(main_admin.sh)
