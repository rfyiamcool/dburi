# dburi

use python parse database uri address, return format

什么是uri ?  简单说uri是配置地址的一种表达方式，可以在一行里详细的描述出host,port,user,passwd,database,tablename,other field 。 

我发现python社区里，没发现能用的database uri的解析模块 


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

```
from dburi import parse_db_str
print parse_db_str('mysql://buzz:123@localhost/buzz_master?option=open&charset=utf8&table=test')
print parse_db_str('mysql://buzz:123@localhost/buzz_master')
print parse_db_str("mongo://127.0.0.1:27017/buzz_master")
print parse_db_str('redis://127.0.0.1:6379')
print parse_db_str('elasticsearch://127.0.0.1:9200')
print parse_db_str('hbase://127.0.0.1:9090/buzz')
print parse_db_str('memcached://127.0.0.1:11211')
```
