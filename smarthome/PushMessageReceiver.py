import logging

from flask import Flask, request
from requests import RequestException
from flask import Blueprint

# import db,models
from . import db, models

from huawei_sdk.utils.LogUtil import Log

# app = Flask(__name__)  #

# 将该视图从华为SDK中移出，统一处理
# 使用蓝图的方式将这里注册成一个app蓝图
from .models import HomeData, HomeData_Bedroom, HomeData_Kitchen

receiver = Blueprint("push_receiver", __name__)


@receiver.route('/v1.0.0/messageReceiver', methods=['POST'])
@receiver.route('/v1.0.0/messageReceiver/cmd', methods=['POST'])
def receive():
    log = Log()
    log.setLogConfig()

    pmr = PushMessageReceiver()
    try:
        if request.json['notifyType'] == "deviceAdded":
            logging.info(request.json)
            pmr.handleDeviceAdded()
            return "ok"

        if request.json['notifyType'] == "bindDevice":
            logging.info(request.json)
            pmr.handleBindDevice()
            return "ok"

        if request.json['notifyType'] == "deviceInfoChanged":
            logging.info(request.json)
            pmr.handleDeviceInfoChanged()
            return "ok"

        if request.json['notifyType'] == "deviceDataChanged":
            logging.info(request.json)
            pmr.handleDeviceDataChanged()
            return "ok"

        if request.json['notifyType'] == "deviceDatasChanged":
            logging.info(request.json)
            pmr.handleDeviceDatasChanged()
            return "ok"

        if request.json['notifyType'] == "serviceInfoChanged":
            logging.info(request.json)
            pmr.handleServiceInfoChanged()
            return "ok"

        if request.json['notifyType'] == "deviceDeleted":
            logging.info(request.json)
            pmr.handleDeviceDeleted()
            return "ok"

        if request.json['notifyType'] == "messageConfirm":
            logging.info(request.json)
            pmr.handleMessageConfirm()
            return "ok"

        if request.json['notifyType'] == "commandRsp":
            logging.info(request.json)
            pmr.handleCommandRsp()
            return "ok"

        if request.json['notifyType'] == "deviceEvent":
            logging.info(request.json)
            pmr.handleDeviceEvent()
            return "ok"

        if request.json['notifyType'] == "deviceModelAdded":
            logging.info(request.json)
            pmr.handleDeviceModelAdded()
            return "ok"

        if request.json['notifyType'] == "deviceModelDeleted":
            logging.info(request.json)
            pmr.handleDeviceDeleted()
            return "ok"

        if request.json['notifyType'] == "ruleEvent":
            logging.info(request.json)
            pmr.handleRuleEvent()
            return "ok"

        if request.json['notifyType'] == "deviceDesiredPropertiesModifyStatusChanged":
            logging.info(request.json)
            pmr.handleDeviceDesiredStatusChanged()
            return "ok"

        if request.json['notifyType'] == "swUpgradeStateChangeNotify":
            logging.info(request.json)
            pmr.handleSwUpgradeStateChanged()
            return "ok"

        if request.json['notifyType'] == "swUpgradeResultNotify":
            logging.info(request.json)
            pmr.handleSwUpgradeResult()
            return "ok"

        if request.json['notifyType'] == "fwUpgradeStateChangeNotify":
            logging.info(request.json)
            pmr.handleFwUpgradeStateChanged()
            return "ok"

        if request.json['notifyType'] == "fwUpgradeResultNotify":
            logging.info(request.json)
            pmr.handleFwUpgradeResult()
            return "ok"
        else:
            return "notifyType doesn't exist or notifyType is not right."
    except RequestException as e:
        logging.error(e)
        raise RequestException(e)


class PushMessageReceiver(object):

    def handleDeviceAdded(self):
        print("deviceAdded ==> ", request.json)
        pass

    def handleBindDevice(self):
        print("bindDevice ==> ", request.json)
        pass

    def handleDeviceInfoChanged(self):
        print("deviceInfoChanged ==> ", request.json)
        pass

    def handleDeviceDataChanged(self):
        # 将数据存入数据库
        data = request.json

        serviceId = data['service']['serviceId']

        if serviceId == 'my_home':
            # 获取数据
            temperature = data['service']['data']['temperature_parlour_room']
            humidity = data['service']['data']['humidity_parlour_room']
            smoke = data['service']['data']['smoke_parlour_room']
            time = data['service']['eventTime']

            temperature_bedroom = data['service']['data']['temperature_bedroom']
            humidity_bedroom = data['service']['data']['humidity_bedroom']
            smoke_bedroom = data['service']['data']['smoke_bedroom']
            time_bedroom = data['service']['eventTime']

            temperature_kitchen= data['service']['data']['temperature_kitchen']
            humidity_kitchen = data['service']['data']['humidity_kitchen']
            smoke_kitchen = data['service']['data']['smoke_kitchen']
            time_kitchen = data['service']['eventTime']

            # 赋值到模型对象
            data_bean = HomeData()
            data_bean.temperature = temperature
            data_bean.humidity = humidity
            data_bean.smoke = smoke
            data_bean.time = time

            bedroom_data = HomeData_Bedroom()
            bedroom_data.temperature = temperature_bedroom
            bedroom_data.humidity = humidity_bedroom
            bedroom_data.smoke = smoke_bedroom
            bedroom_data.time = time_bedroom

            kitchen_data = HomeData_Kitchen()
            kitchen_data.temperature = temperature_kitchen
            kitchen_data.humidity = humidity_kitchen
            kitchen_data.smoke = smoke_kitchen
            kitchen_data.time = time_kitchen

            print(data_bean.temperature)

            db.session.add(data_bean)
            db.session.add(bedroom_data)
            db.session.add(kitchen_data)
            db.session.commit()

        else:
            # 如果是测试订阅请求就直接返回ok
            pass

        print("deviceDataChanged ==> ", request.json)


    def handleDeviceDatasChanged(self):
        print("deviceDatasChanged ==> ", request.json)
        pass

    def handleServiceInfoChanged(self):
        print("serviceInfoChanged ==> ", request.json)
        pass

    def handleDeviceDeleted(self):
        print("deviceDeleted ==> ", request.json)
        pass

    def handleMessageConfirm(self):
        print("messageConfirm ==> ", request.json)
        pass

    def handleCommandRsp(self):
        print("commandRsp ==> ", request.json)
        pass

    def handleDeviceEvent(self):
        print("deviceEvent ==> ", request.json)
        pass

    def handleDeviceModelAdded(self):
        print("deviceModelAdded ==> ", request.json)
        pass

    def handleDeviceModelDeleted(self):
        print("deviceModelDeleted ==> ", request.json)
        pass

    def handleRuleEvent(self):
        print("ruleEvent ==> ", request.json)
        pass

    def handleDeviceDesiredStatusChanged(self):
        print("deviceDesiredPropertiesModifyStatusChanged ==> ", request.json)
        pass

    def handleSwUpgradeStateChanged(self):
        print("swUpgradeStateChangeNotify ==> ", request.json)
        pass

    def handleSwUpgradeResult(self):
        print("swUpgradeResultNotify ==> ", request.json)
        pass

    def handleFwUpgradeStateChanged(self):
        print("fwUpgradeStateChangeNotify ==> ", request.json)
        pass

    def handleFwUpgradeResult(self):
        print("fwUpgradeResultNotify ==> ", request.json)
        pass
