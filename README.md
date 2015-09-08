# dburi

### 安装

```
pip install dburi
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
