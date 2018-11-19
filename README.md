# django
a django study project

## 目录

* [运行](#运行)
* [项目文件介绍](#项目文件介绍)

### 运行

```text
   py manage.py runserver 
```

### 项目文件介绍

```
django
│   README.md
│   db.sqlite3
│   manage.py
│
└───mysite
│   │   __init__.py
│   │   settings.py
│   │   urs.py
│   │   wsgi.py
└───blog
│   │   __init__.py
│   │   views.py               （应用对应的页面)
│   │   apps.py
│   │   models.py               （数据库相关）
│   │   admin.py                (管理数据库后台的)
│   │   tests.py
```