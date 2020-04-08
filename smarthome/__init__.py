# -*- coding: utf-8 -*-
# @Author  : zhu

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy



# 数据库
db = SQLAlchemy()


# 配置日志信息
# 设置日志的记录等级
# logging.basicConfig(level=logging.INFO)
# # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
# file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
# formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# # 为刚创建的日志记录器设置日志记录格式
# file_log_handler.setFormatter(formatter)
# # 为全局的日志工具对象（flask app使用的）添加日记录器
# logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str  配置模式的模式的名字 （"develop",  "product"）
    :return:
    """
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    # 注册蓝图
    # 注册SDK内部处理https请求的蓝图
    from smarthome.PushMessageReceiver import receiver
    app.register_blueprint(receiver)

    # 注册主模块蓝图
    from smarthome.views import app_main
    app.register_blueprint(app_main)

    return app
