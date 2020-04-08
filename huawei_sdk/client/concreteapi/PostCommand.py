import json

from huawei_sdk.client.invokeapi.Authentication import Authentication
from huawei_sdk.client.invokeapi.SignalDelivery import SignalDelivery

from huawei_sdk.client.dto.AuthOutDTO import AuthOutDTO
from huawei_sdk.client.dto.CreateDeviceCmdCancelTaskInDTO import CreateDeviceCmdCancelTaskInDTO
from huawei_sdk.client.dto.PostDeviceCommandInDTO import PostDeviceCommandInDTO
from huawei_sdk.client.dto.PostDeviceCommandOutDTO import PostDeviceCommandOutDTO
from huawei_sdk.client.dto.QueryDeviceCmdCancelTaskInDTO import QueryDeviceCmdCancelTaskInDTO
from huawei_sdk.client.dto.QueryDeviceCommandInDTO import QueryDeviceCommandInDTO
from huawei_sdk.client.dto.UpdateDeviceCommandInDTO import UpdateDeviceCommandInDTO
from huawei_sdk.constant.Constant import Constant


class PostCommand(object):
    def __init__(self):
        self.method = ""
        self.paras = None

    def postDeviceCommandInfo(self):
        pdcInDTO = PostDeviceCommandInDTO()
        pdcInDTO.deviceId = "d9a11d86-636f-431a-8769-9b0dd90e9140"
        pdcInDTO.expireTime = 0

        pdcInDTO.command = {
            pdcInDTO.command.method: self.method,
            pdcInDTO.command.serviceId: "my_home",
            pdcInDTO.command.paras: self.paras}

        print("method:", self.method)
        print("paras:", self.paras)

        return pdcInDTO

    def queryDeviceCommandInfo(self):
        qdcInDTO = QueryDeviceCommandInDTO()
        qdcInDTO.deviceId = "d9a11d86-636f-431a-8769-9b0dd90e9140"
        qdcInDTO.pageSize = "2"
        return qdcInDTO
