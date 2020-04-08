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


class SignalDeliveryTest(object):

    def postDeviceCommandInfo(self):
        pdcInDTO = PostDeviceCommandInDTO()
        pdcInDTO.deviceId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        pdcInDTO.expireTime = 0

        # pdcInDTO.command = {
        #     pdcInDTO.command.method: "home_mode",
        #     pdcInDTO.command.serviceId: "my_home"}

        paras_dict = {"open": "O"}
        paras = json.dumps(paras_dict)

        pdcInDTO.command = {
            pdcInDTO.command.method: "home_mode",
            pdcInDTO.command.serviceId: "my_home",
            pdcInDTO.command.paras: paras_dict}

        print(pdcInDTO.command)

        return pdcInDTO

    # def updateDeviceCommandInfo(self):
    #     udcInDTO = UpdateDeviceCommandInDTO()
    #     udcInDTO.status = "CANCELED"
    #     return udcInDTO
    #
    # def queryDeviceCommandInfo(self):
    #     qdcInDTO = QueryDeviceCommandInDTO()
    #     qdcInDTO.deviceId = "bd6394ed-b41d-430d-85f8-5d0290cfee24"
    #     qdcInDTO.pageSize = "2"
    #     return qdcInDTO
    #
    # def createDeviceCmdCancelTaskInfo(self):
    #     cdcctInDTO = CreateDeviceCmdCancelTaskInDTO()
    #     cdcctInDTO.deviceId = deviceId
    #     return cdcctInDTO
    #
    # def queryDeviceCmdCancelTaskInfo(self):
    #     qdcctInDTO = QueryDeviceCmdCancelTaskInDTO()
    #     qdcctInDTO.deviceId = deviceId
    #     return qdcctInDTO


if __name__ == "__main__":
    sdTest = SignalDeliveryTest()
    authentication = Authentication()
    signalDelivery = SignalDelivery()

    # get accessToken at first
    result = authentication.getAuthToken(Constant().clientInfo())
    authOutDTO = AuthOutDTO()
    authOutDTO.setAccessToken(json.loads(result)['accessToken'])
    accessToken = authOutDTO.getAccessToken()

    # post an NB-IoT device command
    sp = signalDelivery.postDeviceCommand(sdTest.postDeviceCommandInfo(), None, accessToken)
    print("====== post an NB-IoT device command ======")
    print("result:", sp + "\n")

    # # get commandId And deviceId
    # pdcOutDTO = PostDeviceCommandOutDTO()
    # pdcOutDTO.setCommandId(json.loads(sp)['commandId'])
    # commandId = pdcOutDTO.getCommandId()
    # pdcOutDTO.setDeviceId(json.loads(sp)['deviceId'])
    # deviceId = pdcOutDTO.getDeviceId()
    # print("commandId==", commandId)
    # print("deviceId==", deviceId + "\n")

    # # update device command
    # su = signalDelivery.updateDeviceCommand(sdTest.updateDeviceCommandInfo(), commandId, None, accessToken)
    # print("====== update device command ======")
    # print("result:", su + "\n")
    #
    # # query device commands
    # sq = signalDelivery.queryDeviceCommand(sdTest.queryDeviceCommandInfo(), accessToken)
    # print("====== query device commands ======")
    # print("result:", sq + "\n")
    #
    # # cancel all device commands of the device
    # sc = signalDelivery.createDeviceCmdCancelTask(sdTest.createDeviceCmdCancelTaskInfo(), None, accessToken)
    # print("====== cancel all device commands of the device ======")
    # print("result:", sc + "\n")
    #
    # # query device command cancel tasks of the device
    # sc = signalDelivery.queryDeviceCmdCancelTask(sdTest.queryDeviceCmdCancelTaskInfo(), accessToken)
    # print("====== query device command cancel tasks of the device ======")
    # print("result:", sc + "\n")
