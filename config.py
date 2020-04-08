# coding:utf-8

class Config(object):
    """配置数据库参数"""
    SQLALCHEMY_DATABASE_URI = 'mysql://root:338471@127.0.0.1:3306/flask_iot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """配置SECRET_KEY"""
    SECRET_KEY = "zhushfalihglaksh"

    # 解决中文乱码问题
    JSON_AS_ASCII = False

    """定时任务"""
    # 任务1：间隔:15s刷新SDK的token
    # 任务2：定时每天6：30获取token
    JOBS = [
        {
            'id': 'job1',
            'func': 'scheduler_tasks:scheduler_refresh_token',
            'args': '',
            'trigger': 'interval',
            'seconds': 10
        }
    ]

    SCHEDULER_API_ENABLED = True


class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}
