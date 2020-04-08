# coding:utf-8


# 导入db对象
from . import db


# 定义模型类
class HomeData(db.Model):
    """NB上报数据的实体类"""
    __tablename__ = 'home_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperature = db.Column(db.String(5), nullable=False)
    humidity = db.Column(db.String(5), nullable=False)
    smoke = db.Column(db.String(5), nullable=False)
    time = db.Column(db.String(32), nullable=False)

    # 重写__repr__
    def __repr__(self):
        return ("homeData:%s time:%s temperature:%s humidity:%s smoke:%s",
                self.id, self.time, self.temperature, self.humidity, self.smoke)

# 定义卧室模型类
class HomeData_Bedroom(db.Model):
    """NB上报卧室数据的实体类"""
    __tablename__ = 'home_bedroom_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperature = db.Column(db.String(5), nullable=False)
    humidity = db.Column(db.String(5), nullable=False)
    smoke = db.Column(db.String(5), nullable=False)
    time = db.Column(db.String(32), nullable=False)

    # 重写__repr__
    def __repr__(self):
        return ("home_bedroom_data:%s time:%s temperature:%s humidity:%s smoke:%s",
                self.id, self.time, self.temperature, self.humidity, self.smoke)


# 定义厨房模型类
class HomeData_Kitchen(db.Model):
    """NB上报厨房数据的实体类"""
    __tablename__ = 'home_kitchen_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperature = db.Column(db.String(5), nullable=False)
    humidity = db.Column(db.String(5), nullable=False)
    smoke = db.Column(db.String(5), nullable=False)
    time = db.Column(db.String(32), nullable=False)

    # 重写__repr__
    def __repr__(self):
        return ("home_kitchen_data:%s time:%s temperature:%s humidity:%s smoke:%s",
                self.id, self.time, self.temperature, self.humidity, self.smoke)