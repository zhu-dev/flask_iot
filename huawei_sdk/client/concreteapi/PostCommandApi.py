import json

from huawei_sdk.client.concreteapi.PostCommand import PostCommand
from huawei_sdk.client.dto.AuthOutDTO import AuthOutDTO
from huawei_sdk.client.dto.PostDeviceCommandOutDTO import PostDeviceCommandOutDTO
from huawei_sdk.client.invokeapi.Authentication import Authentication
from huawei_sdk.client.invokeapi.SignalDelivery import SignalDelivery
from huawei_sdk.client.invokeapiTest.SignalDeliveryTest import SignalDeliveryTest
from huawei_sdk.constant.Constant import Constant


def postCommand(method, paras):
    sdTest = PostCommand()
    sdTest.method = method
    sdTest.paras = paras

    authentication = Authentication()
    signalDelivery = SignalDelivery()

    # get accessToken at first
    result = authentication.getAuthToken(Constant().clientInfo())
    authOutDTO = AuthOutDTO()
    authOutDTO.setAccessToken(json.loads(result)['accessToken'])
    accessToken = authOutDTO.getAccessToken()

    # post an NB-IoT device command
    sp = signalDelivery.postDeviceCommand(sdTest.postDeviceCommandInfo(), None, accessToken)
    # print("====== post an NB-IoT device command ======")
    # print("result:", sp + "\n")
    return sp


if __name__ == "__main__":
    postCommand()
