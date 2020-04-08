# coding:utf-8

from huawei_sdk.client.dto.SubDeviceBusinessDataInDTO import SubDeviceBusinessDataInDTO
from huawei_sdk.client.dto.SubDeviceManagementDataInDTO import SubDeviceManagementDataInDTO


class Subscription(object):

    def __init__(self, notifyType, callbackUrl):
        self.notifyType = notifyType
        self.callbackUrl = callbackUrl

    def subDeviceBusinessData(self):
        sdbdInDTO = SubDeviceBusinessDataInDTO()
        sdbdInDTO.notifyType = self.notifyType
        sdbdInDTO.callbackUrl = self.callbackUrl
        return sdbdInDTO

    def subDeviceManagementData(self):
        sdmdInDTO = SubDeviceManagementDataInDTO()
        sdmdInDTO.notifyType = self.notifyType
        sdmdInDTO.callbackurl = self.callbackUrl
        return sdmdInDTO


