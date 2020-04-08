import configparser
import os

from huawei_sdk.client.dto.ClientInfo import ClientInfo
from huawei_sdk.utils.DictUtil import DictUtil

cf = configparser.ConfigParser()


class Constant(object):
    workPath = os.path.join('E:/Flask_projects/flask_iot_1/huawei_sdk') # sdk的路径

    def readCertificate(self):
        certFilePath = os.path.join(Constant.workPath, 'cert/client.crt')
        certFilePath2 = os.path.join(Constant.workPath, 'cert/client.key')
        cert = (certFilePath, certFilePath2)
        return cert

    def readConfFile(self):
        configFilePath = os.path.join(Constant.workPath, 'resources/application.ini')
        cf.read(configFilePath)
        platformIp = cf.get("CLIENT_INFO", "platformIp")
        platformPort = cf.get("CLIENT_INFO", "platformPort")
        appId = cf.get("CLIENT_INFO", "appId")
        secret = cf.get("CLIENT_INFO", "secret")
        return platformIp, platformPort, appId, secret

    def clientInfo(self):
        clientInfo = ClientInfo()
        clientInfo.setPlatformIp((Constant().readConfFile())[0])
        clientInfo.setPlatformPort((Constant().readConfFile())[1])
        clientInfo.setAppId((Constant().readConfFile())[2])
        clientInfo.setSecret((Constant().readConfFile())[3])
        clientInfo = DictUtil.dto2dict(clientInfo)
        return clientInfo

    # def clientInfo(self):
    #     clientInfo = ClientInfo()
    #     clientInfo.platformIp = (Constant().readConfFile())[0]
    #     clientInfo.platformPort = (Constant().readConfFile())[1]
    #     clientInfo.appId = (Constant().readConfFile())[2]
    #     clientInfo.secret = (Constant().readConfFile())[3]
    #     clientInfo = DictUtil.dto2dict(clientInfo)
    #     return clientInfo

    ######################################------------ Authentication ------------######################################
    #####################################------------ DeviceManagement ------------#####################################
    #######################################------------ BatchProcess ------------#######################################
    ######################################------------ RuleEngine ------------##########################################
    #################################------------ SubscriptionManagement ------------###################################
    #################################------------ DeviceServiceInvocation ------------##################################
    ####################################------------ SignalDelivery ------------########################################
    ######################################------------ DataCollection ------------######################################
    ##################################------------ DeviceGroupManagement ------------###################################
    ######################################------------ DeviceUpgrade ------------#######################################
    ###################################------------ PushMessageReceiver ------------####################################
