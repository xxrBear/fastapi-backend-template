# FastAPI 快速后端模板

![Static Badge](https://img.shields.io/badge/build-_python_3.13+-blue)
![Static Badge](https://img.shields.io/badge/FastAPI_-green)
![Static Badge](https://img.shields.io/badge/SQLModel-8A2BE2)
![Static Badge](https://img.shields.io/badge/Pydantic2-red)

## 简介

基于 FastAPI + PostgreSQL + SQLModel 等，搭建的服务端应用，用于快速开发

## 快速开始

- 设置虚拟环境
```shell
uv sync
```

- 根目录下创建并设置`.env`文件
```
SECRET_KEY=
POSTGRES_SERVER=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```

- 迁移数据表
```shell
alembic upgrade head
```

- 创建管理员用户
```shell
python -m scripts.init_superuser
```
