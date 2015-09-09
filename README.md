# dburi

use python parse database uri address, return format

什么是uri ?  简单说uri是配置地址的一种表达方式，可以在一行里详细的描述出host,port,user,passwd,database,tablename,other field 

原本是想在python社区里淘淘，结果没发现能用的database uri解析模块，就自己搞了一个。


new version :

解决了dburi兼容python 2.6 3.x的问题

增加了常见数据库的端口补充

增加了ini配置文件的解析


[更多文档](http://xiaorui.cc  "更多db uri")

### 安装

```
pip install dburi
```


```
git clone git@github.com:rfyiamcool/dburi.git
cd dburi
python setup.py install
```

### 方法

mysql://xiaorui:123@localhost/xiaorui_master?option=open&charset=utf8&table=test'

```
mysql标示位表明是哪个数据库
        xiaorui:123 表明的是账号和密码
                @localhost 表明的是数据库HOST地址
                          /xiaorui_master 表明的是数据库名字
                                            ?k=v&k=v 这堆传参是作为扩展字段使用的
```

开始测试,端口可以不填写，但是数据库要写全称
```
from dburi import parse_db_str
print parse_db_str('mysql://xiaorui:123@localhost/xiaorui_master?option=open&charset=utf8&table=test')
print parse_db_str('mysql://xiaorui:123@localhost/xiaorui_master')
print parse_db_str("mongo://127.0.0.1:27017/xiaorui_master")
print parse_db_str('redis://127.0.0.1:6379')
print parse_db_str('elasticsearch://127.0.0.1:9200')
print parse_db_str('hbase://127.0.0.1:9090/xiaorui')
print parse_db_str('memcached://127.0.0.1:11211')
```

Result 结果
```
{'name': 'mysql', 'extra': 'option=open&charset=utf8&table=test', 'passwd': '123', 'charset': 'utf8', 'db': 'xiaorui_master', 'host': 'localhost', 'user': 'xiaorui', 'table': 'test', 'port': 3306, 'option': 'open'}
{'name': 'mysql', 'passwd': '123', 'db': 'xiaorui_master', 'host': 'localhost', 'user': 'xiaorui', 'port': 3306}
{'host': '127.0.0.1', 'db': 'xiaorui_master', 'name': 'mongo', 'port': 27017}
{'host': '127.0.0.1', 'name': 'redis', 'port': 6379}
{'host': '127.0.0.1', 'name': 'elasticsearch', 'port': 9200}
{'host': '127.0.0.1', 'db': 'xiaorui', 'name': 'hbase', 'port': 9090}
{'host': '127.0.0.1', 'name': 'memcached', 'port': 11211}
```
