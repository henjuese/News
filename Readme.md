## About This Project

  这个Repo主要用于新闻管理系统的毕业设计，没有任何实用及使用价值。

## Python模块依赖
  * [Python 3.2.2](http://python.org)
  * [psycopg2 2.4.4](http://initd.org/psycopg)
  * [PostgreSql 9.1](http://postgresql.org)
  * [mako 0.6.2](http://makotemplates.org)
  * [tornado 2.2](https://github.com/facebook/tornado.git)
  * [redis 2.4.5 (for windows)](https://github.com/dmajkic/redis.git)
  * [redis-py](https://github.com/dcolish/redis-py.git)
  * [anyjson](http://pypi.python.org/pypi/anyjson/0.3.1)
  * [doctuils]()
  * [Markdown]()
  
## 参考
  * [session redis](http://tornadogists.org/1735032/) 原文使用 pickle 序列化，现改为JSON。
  * [Admin Template]() 本系统后台完全使用其代码模板
  
## 开发日志
  * [2012-05-08 13:08:12]
    - 修复但没有用户登录时，无法看到评论的BUG
  * [2012-05-07 01:34:01]
    - 预计功能全部已经完成
    - 计划添加
      1. 添加新闻与修改新闻时支持更多的语法(目前仅支持Markdown)
      2. 管理后台显示当前登录的用户与用户头像
      3. 新闻的Tag管理
      4. 新闻概要的显示(目前仅在数据库中添加了字段)
  * [2012-04-25 16:07:07]
    - 修正评论分页的显示问题
    - 添加Gravatar的评论头像
    - 修正Session存储使用pickle的Unicode编码错误，使用JSON解决
  * [2012-04-18 周三]    使用Redis存储Session，评论添加完成，评论与新闻分页待完善
  * [2012-04-15 周一]    添加了简单的Mako模板分页defs(未测试)，下一步：评论添加与显示
  * [2012-04-15 周日]    大幅度修改网站风格，完成了新闻分类请求，以及新闻内容查看
  * [2012-04-09 周六]    修改导航
  * [2012-04-09 周一]    确定网址样式，mako 模板调试完成
  * [2012-04-07 周六]    VS2010调试失败
  * [2012-04-06 周五]    完善CSS的组织等
  * [2012-04-05 周四]    确定基本框架，以及以前已经写好的数据表

## TODO
  -[ ] 用户修改密码
  -[ ] 用户重置密码(未登录时)
  -[ ] 新闻的搜索
  -[ ] 新闻概要的显示
